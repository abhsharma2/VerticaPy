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
import os, vertica_python
from typing import Literal, Union
import numpy as np

import verticapy._config.config as conf
from verticapy._utils._sql._collect import save_verticapy_logs
from verticapy._utils._gen import gen_tmp_name
from verticapy._utils._sql._format import quote_ident, schema_relation
from verticapy._utils._sql._sys import _executeSQL
from verticapy._utils._sql._vertica_version import check_minimum_version
from verticapy.connection import current_cursor

from verticapy.core.tablesample.base import TableSample
from verticapy.core.vdataframe.base import vDataFrame

from verticapy.machine_learning.vertica.base import (
    Clustering,
    MulticlassClassifier,
    Tree,
    vModel,
)
import verticapy.machine_learning.memmodel as mm
from verticapy.machine_learning.model_management.read import does_model_exist

from verticapy.sql.drop import drop


"""
Algorithms used for clustering.
"""


class KMeans(Clustering):
    """
Creates a KMeans object using the Vertica k-means algorithm on the data. 
k-means clustering is a method of vector quantization, originally from signal 
processing, that aims to partition n observations into k clusters in which 
each observation belongs to the cluster with the nearest mean (cluster centers 
or cluster centroid), serving as a prototype of the cluster. This results in 
a partitioning of the data space into Voronoi cells.

Parameters
----------
name: str
	Name of the the model. The model will be stored in the database.
n_cluster: int, optional
	Number of clusters
init: str / list, optional
	The method to use to find the initial cluster centers.
		kmeanspp : Uses the KMeans++ method to initialize the centers.
		random   : The centers are initialized randomly.
	It can be also a list with the initial cluster centers to use.
max_iter: int, optional
	The maximum number of iterations the algorithm performs.
tol: float, optional
	Determines whether the algorithm has converged. The algorithm is considered 
	converged after no center has moved more than a distance of 'tol' from the 
	previous iteration.
	"""

    @property
    def _vertica_fit_sql(self) -> Literal["KMEANS"]:
        return "KMEANS"

    @property
    def _vertica_predict_sql(self) -> Literal["APPLY_KMEANS"]:
        return "APPLY_KMEANS"

    @property
    def _model_category(self) -> Literal["UNSUPERVISED"]:
        return "UNSUPERVISED"

    @property
    def _model_subcategory(self) -> Literal["CLUSTERING"]:
        return "CLUSTERING"

    @property
    def _model_type(self) -> Literal["KMeans"]:
        return "KMeans"

    @check_minimum_version
    @save_verticapy_logs
    def __init__(
        self,
        name: str,
        n_cluster: int = 8,
        init: Union[Literal["kmeanspp", "random"], list] = "kmeanspp",
        max_iter: int = 300,
        tol: float = 1e-4,
    ):
        self.model_name = name
        self.parameters = {
            "n_cluster": n_cluster,
            "init": init,
            "max_iter": max_iter,
            "tol": tol,
        }

    def _compute_attributes(self) -> dict:
        """
        Computes the model's attributes.
        """
        centers = self.get_attr("centers")
        self.clusters_ = centers.to_numpy()
        self.p_ = 2
        self.metrics_ = self._compute_metrics()

    def _compute_metrics(self):
        metrics_str = self.get_attr("metrics").values["metrics"][0]
        metrics = {
            "index": [
                "Between-Cluster Sum of Squares",
                "Total Sum of Squares",
                "Total Within-Cluster Sum of Squares",
                "Between-Cluster SS / Total SS",
                "converged",
            ]
        }
        metrics["value"] = [
            float(
                metrics_str.split("Between-Cluster Sum of Squares: ")[1].split("\n")[0]
            ),
            float(metrics_str.split("Total Sum of Squares: ")[1].split("\n")[0]),
            float(
                metrics_str.split("Total Within-Cluster Sum of Squares: ")[1].split(
                    "\n"
                )[0]
            ),
            float(
                metrics_str.split("Between-Cluster Sum of Squares: ")[1].split("\n")[0]
            )
            / float(metrics_str.split("Total Sum of Squares: ")[1].split("\n")[0]),
            metrics_str.split("Converged: ")[1].split("\n")[0] == "True",
        ]
        return TableSample(metrics)

    def plot_voronoi(
        self, max_nb_points: int = 50, plot_crosses: bool = True, ax=None, **style_kwds,
    ):
        """
    Draws the Voronoi Graph of the model.

    Parameters
    ----------
    max_nb_points: int, optional
        Maximum number of points to display.
    plot_crosses: bool, optional
        If set to True, the centers are represented by white crosses.
    ax: Matplotlib axes object, optional
        The axes to plot on.
    **style_kwds
        Any optional parameter to pass to the Matplotlib functions.

    Returns
    -------
    Figure
        Matplotlib Figure
        """
        if len(self.X) == 2:
            from verticapy.plotting._matplotlib import voronoi_plot

            return voronoi_plot(
                clusters=self.clusters_,
                columns=self.X,
                input_relation=self.input_relation,
                plot_crosses=plot_crosses,
                ax=ax,
                max_nb_points=max_nb_points,
                **style_kwds,
            )
        else:
            raise Exception("Voronoi Plots are only available in 2D")

    def to_memmodel(self):
        """
        Converts the model to an InMemory object which
        can be used to do different types of predictions.
        """
        return mm.KMeans(self.clusters_, self.p_,)


class BisectingKMeans(Clustering, Tree):
    """
Creates a BisectingKMeans object using the Vertica bisecting k-means 
algorithm on the data. k-means clustering is a method of vector quantization, 
originally from signal processing, that aims to partition n observations into 
k clusters. Each observation belongs to the cluster with the nearest 
mean (cluster centers or cluster centroid), which serves as a prototype of 
the cluster. This results in a partitioning of the data space into Voronoi
cells. Bisecting k-means combines k-means and hierarchical clustering.

Parameters
----------
name: str
    Name of the the model. The model will be stored in the DB.
n_cluster: int, optional
    Number of clusters
bisection_iterations: int, optional
    The number of iterations the bisecting KMeans algorithm performs for each 
    bisection step. This corresponds to how many times a standalone KMeans 
    algorithm runs in each bisection step. Setting to more than 1 allows 
    the algorithm to run and choose the best KMeans run within each bisection 
    step. Note that if you are using kmeanspp the bisection_iterations value is 
    always 1, because kmeanspp is more costly to run but also better than the 
    alternatives, so it does not require multiple runs.
split_method: str, optional
    The method used to choose a cluster to bisect/split.
        size        : Choose the largest cluster to bisect.
        sum_squares : Choose the cluster with the largest withInSS to bisect.
min_divisible_cluster_size: int, optional
    The minimum number of points of a divisible cluster. Must be greater than or 
    equal to 2.
distance_method: str, optional
    The measure for distance between two data points. Only Euclidean distance 
    is supported at this time.
init: str / list, optional
    The method to use to find the initial KMeans cluster centers.
        kmeanspp : Uses the KMeans++ method to initialize the centers.
        pseudo   : Uses "pseudo center" approach used by Spark, bisects given 
            center without iterating over points.
    It can be also a list with the initial cluster centers to use.
max_iter: int, optional
    The maximum number of iterations the KMeans algorithm performs.
tol: float, optional
    Determines whether the KMeans algorithm has converged. The algorithm is 
    considered converged after no center has moved more than a distance of 
    'tol' from the previous iteration.
    """

    @property
    def _vertica_fit_sql(self) -> Literal["BISECTING_KMEANS"]:
        return "BISECTING_KMEANS"

    @property
    def _vertica_predict_sql(self) -> Literal["APPLY_BISECTING_KMEANS"]:
        return "APPLY_BISECTING_KMEANS"

    @property
    def _model_category(self) -> Literal["UNSUPERVISED"]:
        return "UNSUPERVISED"

    @property
    def _model_subcategory(self) -> Literal["CLUSTERING"]:
        return "CLUSTERING"

    @property
    def _model_type(self) -> Literal["BisectingKMeans"]:
        return "BisectingKMeans"

    @check_minimum_version
    @save_verticapy_logs
    def __init__(
        self,
        name: str,
        n_cluster: int = 8,
        bisection_iterations: int = 1,
        split_method: Literal["size", "sum_squares"] = "sum_squares",
        min_divisible_cluster_size: int = 2,
        distance_method: Literal["euclidean"] = "euclidean",
        init: Union[Literal["kmeanspp", "pseudo", "random"], list] = "kmeanspp",
        max_iter: int = 300,
        tol: float = 1e-4,
    ):
        self.model_name = name
        self.parameters = {
            "n_cluster": n_cluster,
            "bisection_iterations": bisection_iterations,
            "split_method": str(split_method).lower(),
            "min_divisible_cluster_size": min_divisible_cluster_size,
            "distance_method": str(distance_method).lower(),
            "init": init,
            "max_iter": max_iter,
            "tol": tol,
        }

    def _compute_attributes(self):
        """
        Computes the model's attributes.
        """
        centers = self.get_attr("BKTree")
        self.clusters_ = centers.to_numpy()[:, 1 : len(self.X) + 1]
        self.children_left_ = np.array(centers["left_child"])
        self.children_right_ = np.array(centers["right_child"])
        self.cluster_size_ = np.array(centers["cluster_size"])
        wt, tot = centers["withinss"], centers["totWithinss"]
        n = len(wt)
        self.cluster_score_ = np.array([wt[i] / tot[i] for i in range(n)])
        self.p_ = 2
        self.metrics_ = self.get_attr("Metrics")

    def to_graphviz(
        self,
        round_score: int = 2,
        percent: bool = False,
        vertical: bool = True,
        node_style: dict = {"shape": "none"},
        arrow_style: dict = {},
        leaf_style: dict = {},
    ):
        """
        Returns the code for a Graphviz tree.

        Parameters
        ----------
        round_score: int, optional
            The number of decimals to round the node's score to. 
            0 rounds to an integer.
        percent: bool, optional
            If set to True, the scores are returned as a percent.
        vertical: bool, optional
            If set to True, the function generates a vertical tree.
        node_style: dict, optional
            Dictionary of options to customize each node of the tree. 
            For a list of options, see the Graphviz API: 
            https://graphviz.org/doc/info/attrs.html
        arrow_style: dict, optional
            Dictionary of options to customize each arrow of the tree. 
            For a list of options, see the Graphviz API: 
            https://graphviz.org/doc/info/attrs.html
        leaf_style: dict, optional
            Dictionary of options to customize each leaf of the tree. 
            For a list of options, see the Graphviz API: 
            https://graphviz.org/doc/info/attrs.html

        Returns
        -------
        str
            Graphviz code.
        """
        return self.to_memmodel().to_graphviz(
            round_score=round_score,
            percent=percent,
            vertical=vertical,
            node_style=node_style,
            arrow_style=arrow_style,
            leaf_style=leaf_style,
        )

    def plot_tree(
        self, pic_path: str = "", *argv, **kwds,
    ):
        """
        Draws the input tree. Requires the graphviz module.

        Parameters
        ----------
        pic_path: str, optional
            Absolute path to save the image of the tree.
        *argv, **kwds: Any, optional
            Arguments to pass to the 'to_graphviz' method.

        Returns
        -------
        graphviz.Source
            graphviz object.
        """
        return self.to_memmodel().plot_tree(pic_path=pic_path, *argv, **kwds,)

    def to_memmodel(self):
        """
        Converts the model to an InMemory object which
        can be used to do different types of predictions.
        """
        return mm.BisectingKMeans(
            self.clusters_,
            self.children_left_,
            self.children_right_,
            self.cluster_size_,
            self.cluster_score_,
            self.p_,
        )

    def get_tree(self):
        """
    Returns a table containing information about the BK-tree.
        """
        return self.get_attr("BKTree")


class KPrototypes(KMeans):
    """
Creates a KPrototypes object by using the Vertica k-prototypes algorithm on 
the data. The algorithm combines the k-means and k-modes algorithms in order
to handle both numerical and categorical data.

Parameters
----------
name: str
    Name of the the model. The model is stored in the database.
n_cluster: int, optional
    Number of clusters.
init: str / list, optional
    The method used to find the initial cluster centers.
        random   : The centers are initialized randomly.
    You can also provide a list of initial cluster centers.
max_iter: int, optional
    The maximum number of iterations the algorithm performs.
tol: float, optional
    Determines whether the algorithm has converged. The algorithm is considered 
    converged when no center moves more than a distance of 'tol' from the 
    previous iteration.
gamma: float, optional
    Weighting factor for categorical columns. It determines the relative 
    importance of numerical and categorical attributes.
    """

    @property
    def _vertica_fit_sql(self) -> Literal["KPROTOTYPES"]:
        return "KPROTOTYPES"

    @property
    def _vertica_predict_sql(self) -> Literal["APPLY_KPROTOTYPES"]:
        return "APPLY_KPROTOTYPES"

    @property
    def _model_type(self) -> Literal["KPrototypes"]:
        return "KPrototypes"

    @check_minimum_version
    @save_verticapy_logs
    def __init__(
        self,
        name: str,
        n_cluster: int = 8,
        init: Union[Literal["random"], list] = "random",
        max_iter: int = 300,
        tol: float = 1e-4,
        gamma: float = 1.0,
    ):
        self.model_name = name
        self.parameters = {
            "n_cluster": n_cluster,
            "init": init,
            "max_iter": max_iter,
            "tol": tol,
            "gamma": gamma,
        }

    def _compute_attributes(self):
        """
        Computes the model's attributes.
        """
        centers = self.get_attr("centers")
        self.clusters_ = centers.to_numpy()
        self.p_ = 2
        self.gamma_ = self.parameters["gamma"]
        dtypes = centers.dtype
        self.is_categorical_ = [("char" in dtypes[key].lower()) for key in dtypes]
        self.metrics_ = self._compute_metrics()

    def to_memmodel(self):
        """
        Converts the model to an InMemory object which
        can be used to do different types of predictions.
        """
        return mm.KPrototypes(
            self.clusters_, self.p_, self.gamma_, self.is_categorical_
        )


class DBSCAN(vModel):
    """
[Beta Version]
Creates a DBSCAN object by using the DBSCAN algorithm as defined by Martin 
Ester, Hans-Peter Kriegel, Jörg Sander, and Xiaowei Xu. This object uses 
pure SQL to compute the distances and neighbors and uses Python to compute 
the cluster propagation (non-scalable phase).

\u26A0 Warning : This algorithm uses a CROSS JOIN during computation and
                 is therefore computationally expensive at O(n * n), where
                 n is the total number of elements.
                 This algorithm indexes elements of the table in order to be optimal 
                 (the CROSS JOIN will happen only with IDs which are integers). 
                 Since DBSCAN is uses the p-distance, it is highly sensitive to 
                 unnormalized data. However, DBSCAN is robust to outliers and can 
                 find non-linear clusters. It is a very powerful algorithm for 
                 outliers detection and clustering. A table will be created 
                 at the end of the learning phase.

Parameters
----------
name: str
    Name of the the model. This is not a built-in model, so this name will be used
    to build the final table.
eps: float, optional
    The radius of a neighborhood with respect to some point.
min_samples: int, optional
    Minimum number of points required to form a dense region.
p: int, optional
    The p of the p-distance (distance metric used during the model computation).
    """

    @property
    def _is_native(self) -> Literal[False]:
        return False

    @property
    def _vertica_fit_sql(self) -> Literal[""]:
        return ""

    @property
    def _vertica_predict_sql(self) -> Literal[""]:
        return ""

    @property
    def _model_category(self) -> Literal["UNSUPERVISED"]:
        return "UNSUPERVISED"

    @property
    def _model_subcategory(self) -> Literal["CLUSTERING"]:
        return "CLUSTERING"

    @property
    def _model_type(self) -> Literal["DBSCAN"]:
        return "DBSCAN"

    @save_verticapy_logs
    def __init__(self, name: str, eps: float = 0.5, min_samples: int = 5, p: int = 2):
        self.model_name = name
        self.parameters = {"eps": eps, "min_samples": min_samples, "p": p}

    def fit(
        self,
        input_relation: Union[str, vDataFrame],
        X: Union[str, list] = [],
        key_columns: Union[str, list] = [],
        index: str = "",
    ):
        """
    Trains the model.

    Parameters
    ----------
    input_relation: str / vDataFrame
        Training relation.
    X: str / list, optional
        List of the predictors. If empty, all the numerical vcolumns will be used.
    key_columns: str / list, optional
        Columns not used during the algorithm computation but which will be used
        to create the final relation.
    index: str, optional
        Index used to identify each row separately. It is highly recommanded to
        have one already in the main table to avoid creating temporary tables.

    Returns
    -------
    object
        self
        """
        if isinstance(key_columns, str):
            key_columns = [key_columns]
        if isinstance(X, str):
            X = [X]
        if conf.get_option("overwrite_model"):
            self.drop()
        else:
            does_model_exist(name=self.model_name, raise_error=True)
        if isinstance(input_relation, vDataFrame):
            if not (X):
                X = input_relation.numcol()
            input_relation = input_relation._genSQL()
        else:
            if not (X):
                X = vDataFrame(input_relation).numcol()
        X = [quote_ident(column) for column in X]
        self.X = X
        self.key_columns = [quote_ident(column) for column in key_columns]
        self.input_relation = input_relation
        schema, relation = schema_relation(input_relation)
        name_main = gen_tmp_name(name="main")
        name_dbscan_clusters = gen_tmp_name(name="clusters")
        try:
            if not (index):
                index = "id"
                drop(f"v_temp_schema.{name_main}", method="table")
                _executeSQL(
                    query=f"""
                    CREATE LOCAL TEMPORARY TABLE {name_main} 
                    ON COMMIT PRESERVE ROWS AS 
                    SELECT /*+LABEL('learn.cluster.DBSCAN.fit')*/
                        ROW_NUMBER() OVER() AS id, 
                        {', '.join(X + key_columns)} 
                    FROM {self.input_relation} 
                    WHERE {' AND '.join([f"{item} IS NOT NULL" for item in X])}""",
                    title="Computing the DBSCAN Table [Step 0]",
                )
            else:
                _executeSQL(
                    query=f"""
                        SELECT 
                            /*+LABEL('learn.cluster.DBSCAN.fit')*/ 
                            {', '.join(X + key_columns + [index])} 
                        FROM {self.input_relation} 
                        LIMIT 10""",
                    print_time_sql=False,
                )
                name_main = self.input_relation
            distance = [
                f"POWER(ABS(x.{X[i]} - y.{X[i]}), {self.parameters['p']})"
                for i in range(len(X))
            ]
            distance = f"POWER({' + '.join(distance)}, 1 / {self.parameters['p']})"
            table = f"""
                SELECT 
                    node_id, 
                    nn_id, 
                    SUM(CASE 
                          WHEN distance <= {self.parameters['eps']} 
                            THEN 1 
                          ELSE 0 
                        END) 
                        OVER (PARTITION BY node_id) AS density, 
                    distance 
                FROM (SELECT 
                          x.{index} AS node_id, 
                          y.{index} AS nn_id, 
                          {distance} AS distance 
                      FROM 
                      {name_main} AS x 
                      CROSS JOIN 
                      {name_main} AS y) distance_table"""
            if isinstance(conf.get_option("random_state"), int):
                order_by = "ORDER BY node_id, nn_id"
            else:
                order_by = ""
            graph = _executeSQL(
                query=f"""
                    SELECT /*+LABEL('learn.cluster.DBSCAN.fit')*/
                        node_id, 
                        nn_id 
                    FROM ({table}) VERTICAPY_SUBTABLE 
                    WHERE density > {self.parameters['min_samples']} 
                      AND distance < {self.parameters['eps']} 
                      AND node_id != nn_id {order_by}""",
                title="Computing the DBSCAN Table [Step 1]",
                method="fetchall",
            )
            main_nodes = list(
                dict.fromkeys([elem[0] for elem in graph] + [elem[1] for elem in graph])
            )
            clusters = {}
            for elem in main_nodes:
                clusters[elem] = None
            i = 0
            while graph:
                node = graph[0][0]
                node_neighbor = graph[0][1]
                if (clusters[node] == None) and (clusters[node_neighbor] == None):
                    clusters[node] = i
                    clusters[node_neighbor] = i
                    i = i + 1
                else:
                    if clusters[node] != None and clusters[node_neighbor] == None:
                        clusters[node_neighbor] = clusters[node]
                    elif clusters[node_neighbor] != None and clusters[node] == None:
                        clusters[node] = clusters[node_neighbor]
                del graph[0]
            try:
                f = open(f"{name_dbscan_clusters}.csv", "w")
                for c in clusters:
                    f.write(f"{c}, {clusters[c]}\n")
                f.close()
                drop(f"v_temp_schema.{name_dbscan_clusters}", method="table")
                _executeSQL(
                    query=f"""
                    CREATE LOCAL TEMPORARY TABLE {name_dbscan_clusters}
                    (node_id int, cluster int) 
                    ON COMMIT PRESERVE ROWS""",
                    print_time_sql=False,
                )
                query = f"""
                    COPY v_temp_schema.{name_dbscan_clusters}(node_id, cluster) 
                    FROM {{}} 
                         DELIMITER ',' 
                         ESCAPE AS '\\';"""
                if isinstance(current_cursor(), vertica_python.vertica.cursor.Cursor):
                    _executeSQL(
                        query=query.format("STDIN"),
                        method="copy",
                        print_time_sql=False,
                        path=f"./{name_dbscan_clusters}.csv",
                    )
                else:
                    _executeSQL(
                        query=query.format(f"LOCAL './{name_dbscan_clusters}.csv'"),
                        print_time_sql=False,
                    )
                _executeSQL("COMMIT;", print_time_sql=False)
            finally:
                os.remove(f"{name_dbscan_clusters}.csv")
            self.n_cluster_ = i
            _executeSQL(
                query=f"""
                    CREATE TABLE {self.model_name} AS 
                       SELECT /*+LABEL('learn.cluster.DBSCAN.fit')*/
                            {', '.join(self.X + self.key_columns)}, 
                            COALESCE(cluster, -1) AS dbscan_cluster 
                       FROM v_temp_schema.{name_main} AS x 
                       LEFT JOIN v_temp_schema.{name_dbscan_clusters} AS y 
                       ON x.{index} = y.node_id""",
                title="Computing the DBSCAN Table [Step 2]",
            )
            self.n_noise_ = _executeSQL(
                query=f"""
                    SELECT 
                        /*+LABEL('learn.cluster.DBSCAN.fit')*/ 
                        COUNT(*) 
                    FROM {self.model_name} 
                    WHERE dbscan_cluster = -1""",
                method="fetchfirstelem",
                print_time_sql=False,
            )
        finally:
            drop(f"v_temp_schema.{name_main}", method="table")
            drop(f"v_temp_schema.{name_dbscan_clusters}", method="table")
        return self

    def predict(self):
        """
    Creates a vDataFrame of the model.

    Returns
    -------
    vDataFrame
        the vDataFrame including the prediction.
        """
        return vDataFrame(self.model_name)


"""
Algorithms used for classification.
"""


class NearestCentroid(MulticlassClassifier):
    """
[Beta Version]
Creates a NearestCentroid object using the k-nearest centroid algorithm. 
This object uses pure SQL to compute the distances and final score. 

\u26A0 Warning : Because this algorithm uses p-distances, it is highly 
                 sensitive to unnormalized data.

Parameters
----------
p: int, optional
    The p corresponding to the one of the p-distances (distance metric used
    to compute the model).
    """

    @property
    def _is_native(self) -> Literal[False]:
        return False

    @property
    def _vertica_fit_sql(self) -> Literal[""]:
        return ""

    @property
    def _vertica_predict_sql(self) -> Literal[""]:
        return ""

    @property
    def _model_category(self) -> Literal["SUPERVISED"]:
        return "SUPERVISED"

    @property
    def _model_subcategory(self) -> Literal["CLASSIFIER"]:
        return "CLASSIFIER"

    @property
    def _model_type(self) -> Literal["NearestCentroid"]:
        return "NearestCentroid"

    @save_verticapy_logs
    def __init__(self, name: str, p: int = 2):
        self.model_name = name
        self.parameters = {"p": p}

    def _compute_attributes(self):
        """
        Computes the model's attributes.
        """
        func = "APPROXIMATE_MEDIAN" if (self.parameters["p"] == 1) else "AVG"
        X_str = ", ".join([f"{func}({column}) AS {column}" for column in self.X])
        centroids = TableSample.read_sql(
            query=f"""
            SELECT 
                {X_str}, 
                {self.y} 
            FROM {self.input_relation} 
            WHERE {self.y} IS NOT NULL 
            GROUP BY {self.y} 
            ORDER BY {self.y} ASC""",
            title="Getting Model Centroids.",
        )
        self.clusters_ = centroids.to_numpy()[:, 0:-1]
        self.classes_ = self._array_to_int(centroids.to_numpy()[:, -1])
        self.p_ = self.parameters["p"]

    def fit(
        self,
        input_relation: Union[str, vDataFrame],
        X: Union[str, list],
        y: str,
        test_relation: Union[str, vDataFrame] = "",
    ):
        """
    Trains the model.

    Parameters
    ----------
    input_relation: str/vDataFrame
        Training relation.
    X: list
        List of the predictors.
    y: str
        Response column.
    test_relation: str/vDataFrame, optional
        Relation used to test the model.

    Returns
    -------
    object
        self
        """
        if isinstance(X, str):
            X = [X]
        if isinstance(input_relation, vDataFrame):
            self.input_relation = input_relation._genSQL()
        else:
            self.input_relation = input_relation
        if isinstance(test_relation, vDataFrame):
            self.test_relation = test_relation._genSQL()
        elif test_relation:
            self.test_relation = test_relation
        else:
            self.test_relation = self.input_relation
        self.X = [quote_ident(column) for column in X]
        self.y = quote_ident(y)
        self._compute_attributes()
        return self

    def to_memmodel(self):
        """
        Converts the model to an InMemory object which
        can be used to do different types of predictions.
        """
        return mm.NearestCentroid(self.clusters_, self.classes_, self.p_,)