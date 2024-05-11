import os
import sys

dags_path = os.path.join(os.getcwd(), 'dags')  # Should be looks like '.../dags'
sys.path.append(dags_path)
import pandas as pd
from settings.global_config import READY_DATA_DB_URI
from sqlalchemy import create_engine
from utils.extract_stage import (
    get_data_taipei_api,
    get_data_taipei_file_last_modified_time
)
from utils.load_stage import save_geodataframe_to_postgresql
from utils.transform_geometry import add_point_wkbgeometry_column_to_df
from utils.transform_time import convert_str_to_time_format

# Config
RID = "9e0e6ad4-b9f9-4810-8551-0cffd1b915b3" # must be modified(resource)
PAGE_ID = "ca205b54-a06f-4d84-894c-d6ab5079ce79" # must be modified(url上面)
FROM_CRS = 4326
LOAD_BEHAVIOR = "current+history"
DEFAULT_TABLE = "toilet"
HISTORY_TABLE = "toilet_history"
GEOMETRY_TYPE = "Point"

# Extract
res = get_data_taipei_api(RID)
raw_data = pd.DataFrame(res)
raw_data["data_time"] = get_data_taipei_file_last_modified_time(PAGE_ID)

# Transform
# Rename
data = raw_data
data.columns = data.columns.str.lower()
# Rename columns
rename_map = {
    "行政區": "district",
    "公廁類別": "toilet_type",
    "公廁名稱": "toilet_name",
    "公廁地址": "toilet_address",
    "經度": "lng",
    "緯度": "lat",
    "管理單位": "management_unit",
    "座數": "seats",
    "特優級": "excellent",
    "優等級": "superior",
    "普通級": "normal",
    "改善級": "improved",
    "無障礙廁座數": "accessible_seats",
    "親子廁座數": "family_seats"
}
data = data.rename(columns=rename_map)
# Time
# Ready data with time information should always add time zone.
data["data_time"] = convert_str_to_time_format(data["data_time"])
# Geometry
# TUIC use wkb_geometry format to store geometry data, and use `wkb_geometry` as the column name.
# Ready data always in crs 4326 (WGS84) coordinate system.
gdata = add_point_wkbgeometry_column_to_df(
    data, x=data["lng"], y=data["lat"], from_crs=FROM_CRS
)
# Reshape
gdata = gdata.drop(columns=["geometry", "_id"])
#ready_col
ready_col = [
    "data_time",
    "district",
    "toilet_type",
    "toilet_name",
    "toilet_address",
    "management_unit",
    "seats",
    "excellent",
    "superior",
    "normal",
    "improved",
    "accessible_seats",
    "family_seats",
    "lng",
    "lat",
    "wkb_geometry"
]
ready_data = gdata[ready_col]

# Load
# Load data to DB
engine = create_engine(READY_DATA_DB_URI)
save_geodataframe_to_postgresql(
    engine,
    gdata=ready_data,
    load_behavior=LOAD_BEHAVIOR,
    default_table=DEFAULT_TABLE,
    history_table=HISTORY_TABLE,
    geometry_type=GEOMETRY_TYPE,
)
