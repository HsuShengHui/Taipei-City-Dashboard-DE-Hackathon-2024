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
RID = "42cfc382-f2b8-4c3a-87ad-37249634f78e"
PAGE_ID = "6fa3ed67-e60e-44d9-a366-ce7008e322de"
FROM_CRS = 4326
LOAD_BEHAVIOR = "current+history"
DEFAULT_TABLE = "medicine"
HISTORY_TABLE = "medicine_history"
GEOMETRY_TYPE = "Point"

# Extract
res = get_data_taipei_api(RID)
raw_data = pd.DataFrame(res)
raw_data["data_time"] = get_data_taipei_file_last_modified_time(PAGE_ID)

# Transform
# Rename
data = raw_data
data.columns = data.columns.str.lower()

# Extract district
data["district"] = data["地址"].str.split("區").str[0] + "區"
data["district"] = data["district"].str.split("市").str[-1]

# Rename columns
rename_map = {
    "序號": "id",
    "健保特約註記": "health_insurance_contract",
    "機構名稱": "name",
    "地址": "addr",
    "電話": "phone",
    "x": "lng",
    "y": "lat",
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

ready_columns = [
    "data_time",
    "name",
    "addr",
    "lng",
    "lat",
    "wkb_geometry",
    "district",
    "phone"
]
ready_data = gdata[ready_columns]
# save .csv
save_path = os.path.join(dags_path, "proj_city_dashboard", "medicine", "ready_data.csv")
ready_data.to_csv(save_path, index=False)

# # Load
# # Load data to DB
engine = create_engine(READY_DATA_DB_URI)
save_geodataframe_to_postgresql(
    engine,
    gdata=ready_data,
    load_behavior=LOAD_BEHAVIOR,
    default_table=DEFAULT_TABLE,
    history_table=HISTORY_TABLE,
    geometry_type=GEOMETRY_TYPE,
)
