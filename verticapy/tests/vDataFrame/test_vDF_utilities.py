# (c) Copyright [2018-2020] Micro Focus or one of its affiliates.
# Licensed under the Apache License, Version 2.0 (the "License");
# You may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pytest, os
from verticapy import vDataFrame


@pytest.fixture(scope="module")
def titanic_vd(base):
    from verticapy.learn.datasets import load_titanic

    titanic = load_titanic(cursor=base.cursor)
    yield titanic
    drop_table(name="public.titanic", cursor=base.cursor)


@pytest.fixture(scope="module")
def amazon_vd(base):
    from verticapy.learn.datasets import load_amazon

    amazon = load_amazon(cursor=base.cursor)
    yield amazon
    drop_table(name="public.amazon", cursor=base.cursor)


class TestvDFUtilities:
    @pytest.mark.skip(reason="test not implemented")
    def test_vDF_to_csv(self):
        pass

    @pytest.mark.skip(reason="test not implemented")
    def test_vDF_to_db(self):
        pass

    @pytest.mark.skip(reason="test not implemented")
    def test_vDF_to_json(self):
        pass

    def test_vDF_to_list(self, titanic_vd):
        result = (
            titanic_vd.select(["age", "survived"]).sort({"age": "desc"})[:2].to_list()
        )
        assert result == [[80.0, 1], [76.0, 1]]

    def test_vDF_to_pandas(self, titanic_vd):
        import pandas

        result = titanic_vd.to_pandas()
        assert isinstance(result, pandas.DataFrame)
        assert titanic_vd.to_pandas().shape == (1234, 14)

    def test_vDF_to_vdf(self, titanic_vd):
        session_id = get_session(titanic_vd._VERTICAPY_VARIABLES_["cursor"])
        titanic_vd.to_vdf("verticapy_test_{}".format(session_id))
        result = read_vdf(
            "verticapy_test_{}.vdf".format(session_id),
            cursor=titanic_vd._VERTICAPY_VARIABLES_["cursor"],
        )
        os.remove("verticapy_test_{}.vdf".format(session_id))
        assert isinstance(result, vDataFrame)
        assert result.shape() == (1234, 14)

    def test_vDF_del_catalog(self, titanic_vd):
        result = titanic_vd.copy()
        result.describe(method="numerical")
        assert "max" in result["age"].catalog
        assert "avg" in result["age"].catalog
        result.del_catalog()
        assert "max" not in result["age"].catalog
        assert "avg" not in result["age"].catalog

    def test_vDF_load(self, titanic_vd):
        result = titanic_vd.copy()
        result.save()
        assert len(result._VERTICAPY_VARIABLES_["saving"]) == 1
        result.filter("age < 40", print_info=False)
        result = result.load()
        assert len(result._VERTICAPY_VARIABLES_["saving"]) == 0
        assert result.shape() == (1234, 14)

    def test_vDF_save(self, titanic_vd):
        result = titanic_vd.copy()
        result.save()
        assert len(result._VERTICAPY_VARIABLES_["saving"]) == 1

    def test_vDF_set_cursor(self):
        result = titanic_vd.copy()
        cursor = titanic_vd._VERTICAPY_VARIABLES_["cursor"]
        result.set_cursor(cursor)
        assert isinstance(result._VERTICAPY_VARIABLES_["cursor"], type(cursor))

    def test_vDF_set_display_parameters(self, titanic_vd):
        result = titanic_vd.copy()
        result.set_display_parameters(rows=50, columns=5, percent_bar=True)
        assert result._VERTICAPY_VARIABLES_["display"]["rows"] == 50
        assert result._VERTICAPY_VARIABLES_["display"]["columns"] == 5
        assert result._VERTICAPY_VARIABLES_["display"]["percent_bar"] == True

    def test_vDF_set_schema_writing(self, titanic_vd):
        result = titanic_vd.copy()
        result.set_schema_writing("test")
        assert result._VERTICAPY_VARIABLES_["schema_writing"] == "test"

    def test_vDF_sql_on_off(self, titanic_vd):
        result = titanic_vd.copy()
        query_on = result._VERTICAPY_VARIABLES_["query_on"]
        result.sql_on_off()
        assert result._VERTICAPY_VARIABLES_["query_on"] != query_on

    def test_vDF_time_on_off(self, titanic_vd):
        result = titanic_vd.copy()
        time_on = result._VERTICAPY_VARIABLES_["time_on"]
        result.time_on_off()
        assert result._VERTICAPY_VARIABLES_["time_on"] != time_on

    def test_vDF_catcol(self, titanic_vd):
        result = [
            elem.replace('"', "") for elem in titanic_vd.catcol(max_cardinality=3)
        ]
        result.sort()
        assert result == [
            "boat",
            "cabin",
            "embarked",
            "home.dest",
            "name",
            "sex",
            "survived",
            "ticket",
        ]

    def test_vDF_category(self, titanic_vd):
        # test for category = float
        result = titanic_vd["age"].category()
        assert result == "float"

        # test for category = text
        result2 = titanic_vd["name"].category()
        assert result2 == "text"

        # test for category = int
        result3 = titanic_vd["pclass"].category()
        assert result3 == "int"

    def test_vDF_current_relation(self):
        result = titanic_vd.current_relation().split(".")[1].replace('"', "")
        assert result == "titanic"

    def test_vDF_datecol(self, amazon_vd):
        result = [elem.replace('"', "") for elem in amazon_vd.datecol()]
        result.sort()
        assert result == ["date"]

    def test_vDF_dtypes(self, amazon_vd):
        result = amazon_vd.dtypes()["dtype"]
        result.sort()
        assert result == ["date", "int", "varchar(32)"]

    def test_vDF_dtype(self, amazon_vd):
        # test of dtype on int
        result = amazon_vd["number"].dtype()
        assert result == "int"

        # test of dtype on date
        result2 = amazon_vd["date"].dtype()
        assert result2 == "date"

        # test of dtype on varchar(32)
        result3 = amazon_vd["state"].dtype()
        assert result3 == "varchar(32)"

        # verify ctype is the same
        assert result == amazon_vd["number"].ctype()
        assert result2 == amazon_vd["date"].ctype()
        assert result3 == amazon_vd["state"].ctype()

    def test_vDF_empty(self, amazon_vd):
        # test for non-empty vDataFrame
        result = amazon_vd.empty()
        assert result == False

        # test for empty vDataFrame
        result2 = amazon_vd.copy().drop(["number", "date", "state"]).empty()
        assert result2 == True

    def test_vDF_expected_store_usage(self):
        # test expected_size
        result = titanic_vd.expected_store_usage()["expected_size (b)"][-1]
        assert result == pytest.approx(85947.0)

        # test max_size
        result2 = titanic_vd.expected_store_usage()["max_size (b)"][-1]
        assert result2 == pytest.approx(504492.0)

    def test_vDF_explain(self, titanic_vd):
        # test with parameter digraph = False
        result = titanic_vd.explain(digraph=False)
        assert isinstance(result, str)

        # test with parameter digraph = True
        result2 = titanic_vd.explain(digraph=True)
        assert result2[0:7] == "digraph"

    def test_vDF_get_columns(self, titanic_vd):
        result = [
            elem.replace('"', "")
            for elem in titanic_vd.get_columns(exclude_columns=["sibsp", "age"])
        ]
        result.sort()
        assert result == [
            "boat",
            "body",
            "cabin",
            "embarked",
            "fare",
            "home.dest",
            "name",
            "parch",
            "pclass",
            "sex",
            "survived",
            "ticket",
        ]

    def test_vDF_head(self, titanic_vd):
        # testing vDataFrame[].head
        result = titanic_vd.copy().sort({"age": "desc"})["age"].head(2)
        assert result["age"] == [80.0, 76.0]

        # testing vDataFrame.head
        result = titanic_vd.copy().sort({"age": "desc"}).head(2)
        assert result["age"] == [80.0, 76.0]
        assert result["fare"] == [30.0, 78.85]

    def test_vDF_iloc(self):
        # testing vDataFrame[].iloc
        result = titanic_vd.copy().sort({"age": "desc"})["age"].iloc(2, 1)
        assert result["age"] == [76.0, 74.0]

        # testing vDataFrame.iloc
        result = titanic_vd.copy().sort({"age": "desc"}).iloc(2, 1, ["age", "fare"])
        assert result["age"] == [76.0, 74.0]
        assert result["fare"] == [78.85, 7.775]

    def test_vDF_info(self, titanic_vd):
        result = titanic_vd.copy().filter("age > 0", print_info=False)
        result["fare"].drop_outliers(print_info=False)
        result = len(result.info().split("\n")) - 1
        assert result == 2

    def test_vDF_isdate(self, amazon_vd):
        # test for date-like vcolumn
        result = amazon_vd["date"].isdate()
        assert result == True

        # test for non-date-like vcolumn
        result2 = amazon_vd["number"].isdate()
        assert result2 == False

    def test_vDF_isnum(self, titanic_vd):
        # test for numerical vcolumn
        result = titanic_vd["age"].isnum()
        assert result == True

        # test for non-numerical vcolumn
        result = titanic_vd["embarked"].isnum()
        assert result == False

    def test_vDF_memory_usage(self, amazon_vd):
        # testing vDataFrame[].memory_usage
        result = amazon_vd["number"].memory_usage()
        assert result == pytest.approx(1714, 0.01)

        # testing vDataFrame.memory_usage
        result2 = amazon_vd.memory_usage()
        assert result2["value"][0] == pytest.approx(1031, 0.01)
        assert result2["value"][1] == pytest.approx(1714, 0.01)
        assert result2["value"][2] == pytest.approx(1712, 0.01)
        assert result2["value"][3] == pytest.approx(1713, 0.01)
        assert result2["value"][4] == pytest.approx(6170, 0.01)

    def test_vDF_numcol(self, titanic_vd):
        result = [elem.replace('"', "") for elem in titanic_vd.numcol()]
        result.sort()
        assert result == ["age", "body", "fare", "parch", "pclass", "sibsp", "survived"]

    def test_vDF_tail(self, titanic_vd):
        # testing vDataFrame[].tail
        result = titanic_vd.copy().sort(["age"])["age"].tail(2)
        assert result["age"] == [76.0, 80.0]

        # testing vDataFrame.tail
        result = titanic_vd.copy().sort(["age"]).tail(2)
        assert result["age"] == [76.0, 80.0]
        assert result["fare"] == [78.85, 30.0]

    def test_vDF_store_usage(self, titanic_vd):
        result = titanic_vd["age"].store_usage()
        assert result == pytest.approx(5908, 0.01)

    def test_vDF_swap(self, titanic_vd):
        result = titanic_vd.copy()
        result.swap("sex", 0)
        result.swap("pclass", 1)
        assert result.get_columns()[0].replace('"', "") == "sex"
        assert result.get_columns()[1].replace('"', "") == "pclass"
        result.swap("pclass", "sex")
        assert result.get_columns()[0].replace('"', "") == "pclass"
        assert result.get_columns()[1].replace('"', "") == "sex"

    def test_vDF_version(self, titanic_vd):
        result = titanic_vd.version()
        assert 3 <= len(result) <= 4
        assert 0 < result[0] < 20
        assert 0 <= result[1] < 9
