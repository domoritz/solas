#  Copyright 2019-2020 The Solas Authors.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import pandas as pd
from .frame import SolasDataFrame
from .groupby import SolasDataFrameGroupBy, SolasSeriesGroupBy
from .loc import SolasLocIndexer, iSolasLocIndexer
from .series import SolasSeries

global originalDF
# Keep variable scope of original pandas df
originalDF = pd.core.frame.DataFrame
originalSeries = pd.core.series.Series


def setOption(overridePandas=True):
    if overridePandas:
        pd.DataFrame = (
            pd.io.json._json.DataFrame
        ) = (
            pd.io.parsers.DataFrame
        ) = (
            pd.io.sql.DataFrame
        ) = (
            pd.io.excel.DataFrame
        ) = (
            pd.io.formats.DataFrame
        ) = (
            pd.io.sas.DataFrame
        ) = (
            pd.io.clipboards.DataFrame
        ) = (
            pd.io.common.DataFrame
        ) = (
            pd.io.feather_format.DataFrame
        ) = (
            pd.io.gbq.DataFrame
        ) = (
            pd.io.html.DataFrame
        ) = (
            pd.io.orc.DataFrame
        ) = (
            pd.io.parquet.DataFrame
        ) = (
            pd.io.pickle.DataFrame
        ) = (
            pd.io.pytables.DataFrame
        ) = (
            pd.io.spss.DataFrame
        ) = pd.io.stata.DataFrame = pd.io.api.DataFrame = pd.core.frame.DataFrame = SolasDataFrame
        pd.Series = pd.core.series.Series = pd.core.groupby.ops.Series = pd._testing.Series = SolasSeries
        pd.core.groupby.generic.DataFrameGroupBy = SolasDataFrameGroupBy
        pd.core.groupby.generic.SeriesGroupBy = SolasSeriesGroupBy
        pd.core.indexing._LocIndexer = SolasLocIndexer
        pd.core.indexing._iLocIndexer = iSolasLocIndexer
    else:
        pd.DataFrame = pd.io.parsers.DataFrame = pd.core.frame.DataFrame = originalDF
        pd.Series = originalSeries


setOption(overridePandas=True)
