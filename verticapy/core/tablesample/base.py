"""
(c)  Copyright  [2018-2023]  OpenText  or one of its
affiliates.  Licensed  under  the   Apache  License,
Version 2.0 (the  "License"); You  may  not use this
file except in compliance with the License.

You may obtain a copy of the License at:
http://www.apache.org/licenses/LICENSE-2.0

Unless  required  by applicable  law or  agreed to in
writing, software  distributed  under the  License is
distributed on an  "AS IS" BASIS,  WITHOUT WARRANTIES
OR CONDITIONS OF ANY KIND, either express or implied.
See the  License for the specific  language governing
permissions and limitations under the License.
"""
import copy, decimal, datetime, math, time
from typing import Literal, Union
import numpy as np

import pandas as pd

import verticapy._config.config as conf
from verticapy._utils._display import print_table
from verticapy._utils._sql._display import print_query, print_time
from verticapy._utils._sql._format import quote_ident
from verticapy._utils._sql._sys import _executeSQL
from verticapy._utils._sql._vertica_version import vertica_version
from verticapy.errors import ParameterError, MissingColumn

from verticapy.core.string_sql.base import StringSQL

from verticapy.jupyter._javascript import datatables_repr

from verticapy.sql.dtypes import vertica_python_dtype


class TableSample:
    """
The TableSample is the transition from 'Big Data' to 'Small Data'. 
This object allows you to conveniently display your results without any  
dependencies on any other module. It stores the aggregated result in memory
which can then be transformed into a pandas.DataFrame or vDataFrame.

Parameters
----------
values: dict, optional
	Dictionary of columns (keys) and their values. The dictionary must be
	similar to the following one:
	{"column1": [val1, ..., valm], ... "columnk": [val1, ..., valm]}
dtype: dict, optional
	Columns data types.
count: int, optional
	Number of elements if we had to load the entire dataset. It is used 
	only for rendering purposes.
offset: int, optional
	Number of elements that were skipped if we had to load the entire
	dataset. It is used only for rendering purposes.
percent: dict, optional
    Dictionary of missing values (Used to display the percent bars)
max_columns: int, optional
    Maximum number of columns to display.

Attributes
----------
The TableSample attributes are the same as the parameters.
	"""

    @property
    def _object_type(self) -> Literal["TableSample"]:
        return "TableSample"

    def __init__(
        self,
        values: dict = {},
        dtype: dict = {},
        count: int = 0,
        offset: int = 0,
        percent: dict = {},
        max_columns: int = -1,
    ) -> None:
        self.values = values
        self.dtype = dtype
        self.count = count
        self.offset = offset
        self.percent = percent
        self.max_columns = max_columns
        for column in values:
            if column not in dtype:
                self.dtype[column] = "undefined"
        return None

    def __iter__(self) -> tuple:
        return (elem for elem in self.values)

    def __getitem__(self, key) -> list:
        for x in self.values:
            if quote_ident(key).lower() == quote_ident(x).lower():
                return self.values[x]
        raise KeyError(f"'{key}'")

    def __repr__(self) -> str:
        if len(self.values) == 0:
            return ""
        n = len(self.values)
        dtype = self.dtype
        max_columns = (
            self.max_columns if self.max_columns > 0 else conf.get_option("max_columns")
        )
        if n < max_columns:
            data_columns = [[column] + self.values[column] for column in self.values]
        else:
            k = int(max_columns / 2)
            columns = [elem for elem in self.values]
            values0 = [[columns[i]] + self.values[columns[i]] for i in range(k)]
            values1 = [["..." for i in range(len(self.values[columns[0]]) + 1)]]
            values2 = [
                [columns[i]] + self.values[columns[i]]
                for i in range(n - max_columns + k, n)
            ]
            data_columns = values0 + values1 + values2
            dtype["..."] = "undefined"
        formatted_text = print_table(
            data_columns,
            is_finished=(self.count <= len(data_columns[0]) + self.offset),
            offset=self.offset,
            repeat_first_column=("index" in self.values),
            return_html=False,
            dtype=dtype,
            percent=self.percent,
        )
        start, end = self.offset + 1, len(data_columns[0]) - 1 + self.offset
        if (self.offset == 0) and (len(data_columns[0]) - 1 == self.count):
            rows = self.count
        else:
            if start > end:
                rows = f"0 of {self.count}" if (self.count > 0) else "0"
            else:
                count_str = f" of {self.count}" if (self.count > 0) else ""
                rows = f"{start}-{end}{count_str}"
        if len(self.values) == 1:
            column = list(self.values.keys())[0]
            if self.offset > self.count:
                formatted_text += f"Column: {column} | Type: {self.dtype[column]}"
            else:
                formatted_text += (
                    f"Rows: {rows} | Column: {column} | Type: {self.dtype[column]}"
                )
        else:
            if self.offset > self.count:
                formatted_text += f"Columns: {n}"
            else:
                formatted_text += f"Rows: {rows} | Columns: {n}"
        return formatted_text

    def _repr_html_(self, interactive: bool = False) -> str:
        if len(self.values) == 0:
            return ""
        n = len(self.values)
        dtype = self.dtype
        max_columns = (
            self.max_columns if self.max_columns > 0 else conf.get_option("max_columns")
        )
        if n < max_columns:
            data_columns = [[column] + self.values[column] for column in self.values]
        else:
            k = int(max_columns / 2)
            columns = [elem for elem in self.values]
            values0 = [[columns[i]] + self.values[columns[i]] for i in range(k)]
            values1 = [["..." for i in range(len(self.values[columns[0]]) + 1)]]
            values2 = [
                [columns[i]] + self.values[columns[i]]
                for i in range(n - max_columns + k, n)
            ]
            data_columns = values0 + values1 + values2
            dtype["..."] = "undefined"
        percent = self.percent
        for elem in self.values:
            if elem not in percent and (elem != "index"):
                percent = {}
                break
        formatted_text = ""
        # get interactive table if condition true
        if conf.get_option("interactive") or interactive:
            formatted_text = datatables_repr(
                data_columns,
                repeat_first_column=("index" in self.values),
                offset=self.offset,
                dtype=dtype,
            )
        else:
            formatted_text = print_table(
                data_columns,
                is_finished=(self.count <= len(data_columns[0]) + self.offset),
                offset=self.offset,
                repeat_first_column=("index" in self.values),
                return_html=True,
                dtype=dtype,
                percent=percent,
            )
        if conf.get_option("footer_on"):
            formatted_text += '<div style="margin-top:6px; font-size:1.02em">'
            if (self.offset == 0) and (len(data_columns[0]) - 1 == self.count):
                rows = self.count
            else:
                start, end = self.offset + 1, len(data_columns[0]) - 1 + self.offset
                if start > end:
                    rows = f"0 of {self.count}" if (self.count > 0) else "0"
                else:
                    of = f" of {self.count}" if (self.count > 0) else ""
                    rows = f"{start}-{end}{of}"
            if len(self.values) == 1:
                column = list(self.values.keys())[0]
                if self.offset > self.count:
                    formatted_text += (
                        f"<b>Column:</b> {column} | "
                        f"<b>Type:</b> {self.dtype[column]}"
                    )
                else:
                    formatted_text += (
                        f"<b>Rows:</b> {rows} | <b>Column:</b> {column} "
                        f"| <b>Type:</b> {self.dtype[column]}"
                    )
            else:
                if self.offset > self.count:
                    formatted_text += f"<b>Columns:</b> {n}"
                else:
                    formatted_text += f"<b>Rows:</b> {rows} | <b>Columns:</b> {n}"
            formatted_text += "</div>"
        return formatted_text

    def append(self, tbs: "TableSample") -> "TableSample":
        """
        Appends the input TableSample to a target TableSample.

        Parameters
        ----------
        tbs: TableSample
            Tablesample to append.

        Returns
        -------
        TableSample
            self
        """
        assert isinstance(tbs, TableSample), ParameterError(
            "TableSamples can only be appended to another TableSample."
        )
        n1, n2 = self.shape()[0], tbs.shape()[0]
        assert n1 == n2, ParameterError(
            "The input and target TableSamples must have the same number of columns."
            f" Expected {n1}, Found {n2}."
        )
        cols1, cols2 = [col for col in self.values], [col for col in tbs.values]
        for idx in range(n1):
            self.values[cols1[idx]] += tbs.values[cols2[idx]]
        return self

    def decimal_to_float(self):
        """
    Converts all the TableSample's decimals to floats.

    Returns
    -------
    TableSample
        self
        """
        for elem in self.values:
            if elem != "index":
                for i in range(len(self.values[elem])):
                    if isinstance(self.values[elem][i], decimal.Decimal):
                        self.values[elem][i] = float(self.values[elem][i])
        return self

    def merge(self, tbs):
        """
        Merges the input TableSample to a target TableSample.

        Parameters
        ----------
        tbs: TableSample
            Tablesample to merge.

        Returns
        -------
        TableSample
            self
        """
        assert isinstance(tbs, TableSample), ParameterError(
            "TableSamples can only be merged with other TableSamples."
        )
        n1, n2 = self.shape()[1], tbs.shape()[1]
        assert n1 == n2, ParameterError(
            "The input and target TableSamples must have the same number of rows."
            f" Expected {n1}, Found {n2}."
        )
        for col in tbs.values:
            if col != "index":
                if col not in self.values:
                    self.values[col] = []
                self.values[col] += tbs.values[col]
        return self

    def narrow(self, use_number_as_category: bool = False):
        """
        TODO
        """
        result = []
        d = copy.deepcopy(self.values)
        if use_number_as_category:
            categories_alpha = d["index"]
            categories_beta = [x for x in d]
            del categories_beta[0]
            bijection_categories = {}
            for idx, x in enumerate(categories_alpha):
                bijection_categories[x] = idx
            for idx, x in enumerate(categories_beta):
                bijection_categories[x] = idx
        for x in d:
            if x != "index":
                for idx, val_tmp in enumerate(d[x]):
                    try:
                        val = float(val_tmp)
                    except:
                        val = val_tmp
                    if not (use_number_as_category):
                        result += [[x, d["index"][idx], val]]
                    else:
                        result += [
                            [
                                bijection_categories[x],
                                bijection_categories[d["index"][idx]],
                                val,
                            ]
                        ]
        if use_number_as_category:
            return result, categories_alpha, categories_beta
        else:
            return result

    @classmethod
    def read_sql(
        cls,
        query: Union[str, StringSQL],
        title: str = "",
        max_columns: int = -1,
        sql_push_ext: bool = False,
        symbol: str = "$",
    ):
        """
    Returns the result of a SQL query as a TableSample object.

    Parameters
    ----------
    query: str, optional
        SQL Query.
    title: str, optional
        Query title when the query is displayed.
    max_columns: int, optional
        Maximum number of columns to display.
    sql_push_ext: bool, optional
        If set to True, the entire query is pushed to the external table. 
        This can increase performance but might increase the error rate. 
        For instance, some DBs might not support the same SQL as Vertica.
    symbol: str, optional
        One of the following:
        "$", "€", "£", "%", "@", "&", "§", "%", "?", "!"
        Symbol used to identify the external connection.
        See the connect.set_external_connection function for more information.

    Returns
    -------
    TableSample
        Result of the query.

    See Also
    --------
    TableSample : Object in memory created for rendering purposes.
        """
        if conf.get_option("sql_on"):
            print_query(query, title)
        start_time = time.time()
        cursor = _executeSQL(
            query, print_time_sql=False, sql_push_ext=sql_push_ext, symbol=symbol
        )
        description, dtype = cursor.description, {}
        for elem in description:
            dtype[elem[0]] = vertica_python_dtype(
                type_name=elem.type_name,
                display_size=elem[2],
                precision=elem[4],
                scale=elem[5],
            )
        elapsed_time = time.time() - start_time
        if conf.get_option("time_on"):
            print_time(elapsed_time)
        result = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        data_columns = [[item] for item in columns]
        data = [item for item in result]
        for row in data:
            for idx, val in enumerate(row):
                data_columns[idx] += [val]
        values = {}
        for column in data_columns:
            values[column[0]] = column[1 : len(column)]
        return cls(
            values=values, dtype=dtype, max_columns=max_columns,
        ).decimal_to_float()

    def shape(self):
        """
    Computes the TableSample shape.

    Returns
    -------
    tuple
        (number of columns, number of rows)
        """
        cols = [col for col in self.values]
        n, m = len(cols), len(self.values[cols[0]])
        return (n, m)

    def sort(self, column: str, desc: bool = False):
        """
        Sorts the TableSample using the input column.

        Parameters
        ----------
        column: str, optional
            Column used to sort the data.
        desc: bool, optional
            If set to True, the result is sorted in descending order.

        Returns
        -------
        TableSample
            self
        """
        column = column.replace('"', "").lower()
        columns = [col for col in self.values]
        idx = None
        for i, col in enumerate(columns):
            col_tmp = col.replace('"', "").lower()
            if column == col_tmp:
                idx = i
                column = col
        if idx is None:
            raise MissingColumn(f"The Column '{column}' doesn't exist.")
        n, sort = len(self[column]), []
        for i in range(n):
            tmp_list = []
            for col in columns:
                tmp_list += [self[col][i]]
            sort += [tmp_list]
        sort.sort(key=lambda tup: tup[idx], reverse=desc)
        for i, col in enumerate(columns):
            self.values[col] = [sort[j][i] for j in range(n)]
        return self

    def transpose(self):
        """
	Transposes the TableSample.

 	Returns
 	-------
 	TableSample
 		transposed TableSample
		"""
        index = [column for column in self.values]
        first_item = list(self.values.keys())[0]
        columns = [[] for i in range(len(self.values[first_item]))]
        for column in self.values:
            for idx, item in enumerate(self.values[column]):
                try:
                    columns[idx] += [item]
                except:
                    pass
        columns = [index] + columns
        values = {}
        for item in columns:
            values[item[0]] = item[1 : len(item)]
        return TableSample(values, self.dtype, self.count, self.offset, self.percent)

    def to_list(self):
        """
    Converts the TableSample to a list.

    Returns
    -------
    list
        Python list.
        """
        result = []
        all_cols = [elem for elem in self.values]
        if all_cols == []:
            return []
        for i in range(len(self.values[all_cols[0]])):
            result_tmp = []
            for elem in self.values:
                if elem != "index":
                    result_tmp += [self.values[elem][i]]
            result += [result_tmp]
        return result

    def to_numpy(self):
        """
    Converts the TableSample to a numpy array.

    Returns
    -------
    numpy.array
        Numpy Array.
        """
        return np.array(self.to_list())

    def to_pandas(self):
        """
	Converts the TableSample to a pandas DataFrame.

 	Returns
 	-------
 	pandas.DataFrame
 		pandas DataFrame of the TableSample.

	See Also
	--------
	TableSample.to_sql : Generates the SQL query associated to the TableSample.
	TableSample.to_vdf : Converts the TableSample to vDataFrame.
		"""
        if "index" in self.values:
            df = pd.DataFrame(data=self.values, index=self.values["index"])
            return df.drop(columns=["index"])
        else:
            return pd.DataFrame(data=self.values)

    def to_sql(self):
        """
    Generates the SQL query associated to the TableSample.

    Returns
    -------
    str
        SQL query associated to the TableSample.

    See Also
    --------
    TableSample.to_pandas : Converts the TableSample to a pandas DataFrame.
    TableSample.to_sql    : Generates the SQL query associated to the TableSample.
        """

        def get_correct_format_and_cast(val):
            if isinstance(val, str):
                val = "'" + val.replace("'", "''") + "'"
            elif val == None:
                val = "NULL"
            elif isinstance(val, bytes):
                val = str(val)[2:-1]
                val = f"'{val}'::binary({len(val)})"
            elif isinstance(val, datetime.datetime):
                val = f"'{val}'::datetime"
            elif isinstance(val, datetime.date):
                val = f"'{val}'::date"
            elif isinstance(val, datetime.timedelta):
                val = f"'{val}'::interval"
            elif isinstance(val, datetime.time):
                val = f"'{val}'::time"
            elif isinstance(val, datetime.timezone):
                val = f"'{val}'::timestamptz"
            elif isinstance(val, (np.ndarray, list)):
                vertica_version(condition=[10, 0, 0])
                val = f"""
                ARRAY[
                    {", ".join([str(get_correct_format_and_cast(k)) for k in val])}
                     ]"""
            elif isinstance(val, dict):
                vertica_version(condition=[11, 0, 0])
                all_elems = [
                    f"{get_correct_format_and_cast(val[k])} AS {k}" for k in val
                ]
                val = ", ".join(all_elems)
                val = f"ROW({val})"
            try:
                if math.isnan(val):
                    val = "NULL"
            except:
                pass
            return val

        sql = []
        n = len(self.values[list(self.values.keys())[0]])
        for i in range(n):
            row = []
            for column in self.values:
                val = get_correct_format_and_cast(self.values[column][i])
                column_str = '"' + column.replace('"', "") + '"'
                row += [f"{val} AS {column_str}"]
            sql += [f"(SELECT {', '.join(row)})"]
        sql = " UNION ALL ".join(sql)
        return sql

    def to_vdf(self):
        """
	Converts the TableSample to a vDataFrame.

 	Returns
 	-------
 	vDataFrame
 		vDataFrame of the TableSample.

	See Also
	--------
	TableSample.to_pandas : Converts the TableSample to a pandas DataFrame.
	TableSample.to_sql    : Generates the SQL query associated to the TableSample.
		"""
        from verticapy.core.vdataframe.base import vDataFrame

        return vDataFrame(self.to_sql())