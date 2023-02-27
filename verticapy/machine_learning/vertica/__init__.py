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
from verticapy.machine_learning.vertica.cluster import (
    BisectingKMeans,
    DBSCAN,
    KMeans,
    KPrototypes,
    NearestCentroid,
)
from verticapy.machine_learning.vertica.decomposition import MCA, PCA, SVD
from verticapy.machine_learning.vertica.automl.clustering import AutoClustering
from verticapy.machine_learning.vertica.automl.dataprep import AutoDataPrep
from verticapy.machine_learning.vertica.automl.supervised import AutoML
from verticapy.machine_learning.vertica.ensemble import (
    IsolationForest,
    RandomForestClassifier,
    RandomForestRegressor,
    XGBClassifier,
    XGBRegressor,
)
from verticapy.machine_learning.vertica.linear_model import (
    ElasticNet,
    Lasso,
    LinearRegression,
    LogisticRegression,
    Ridge,
)
from verticapy.machine_learning.vertica.naive_bayes import (
    BernoulliNB,
    CategoricalNB,
    GaussianNB,
    MultinomialNB,
    NaiveBayes,
)
from verticapy.machine_learning.vertica.neighbors import (
    KNeighborsClassifier,
    KernelDensity,
    KNeighborsRegressor,
    LocalOutlierFactor,
)
from verticapy.machine_learning.vertica.pipeline import Pipeline
from verticapy.machine_learning.vertica.preprocessing import (
    Balance,
    CountVectorizer,
    MinMaxScaler,
    Scaler,
    OneHotEncoder,
    RobustScaler,
    StandardScaler,
)
from verticapy.machine_learning.vertica.svm import LinearSVC, LinearSVR
from verticapy.machine_learning.vertica.tree import (
    DecisionTreeClassifier,
    DecisionTreeRegressor,
    DummyTreeClassifier,
    DummyTreeRegressor,
)