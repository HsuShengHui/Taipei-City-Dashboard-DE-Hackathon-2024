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
FROM_CRS = 4326
LOAD_BEHAVIOR = "current+history"
DEFAULT_TABLE = "di_park"
HISTORY_TABLE = "di_park_history"
GEOMETRY_TYPE = "Point"

# 匯入資料
path = os.path.join(dags_path, "proj_city_dashboard", "di_park", "di_park.csv")
data = pd.read_csv(path)

# Transform
# Rename
data.columns = data.columns.str.lower()


# Time
# Ready data with time information should always add time zone.
# data["data_time"] = convert_str_to_time_format(data["data_time"])


# Geometry
# TUIC use wkb_geometry format to store geometry data, and use `wkb_geometry` as the column name.
# Ready data always in crs 4326 (WGS84) coordinate system.
# gdata = add_point_wkbgeometry_column_to_df(
#     data, x=data["pm_longitude"], y=data["pm_latitude"], from_crs=FROM_CRS
# )
# # # Reshape
# gdata = gdata.drop(columns=["geometry", "pm_longitude", "pm_latitude"])


# # ready_data
# # ready_col = [
    
# # ]
# ready_data = gdata.copy()
# # # save .csv
# # save_path = os.path.join(dags_path, "proj_city_dashboard", "heal_hospital_beds", "ready_data.csv")
# # ready_data.to_csv(save_path, index=False)

# # Load
# # Load data to DB
engine = create_engine(READY_DATA_DB_URI)
save_geodataframe_to_postgresql(
    engine,
    gdata=data,
    load_behavior=LOAD_BEHAVIOR,
    default_table=DEFAULT_TABLE,
    history_table=HISTORY_TABLE,
    geometry_type=GEOMETRY_TYPE,
)
