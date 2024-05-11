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
RID = "5b1451b7-3be6-4d5e-97cd-97172d96ff3d"
PAGE_ID = "57080dc5-98da-4b5e-8f37-b10ca14d6ca2"
FROM_CRS = 4326
LOAD_BEHAVIOR = "current+history"
DEFAULT_TABLE = "heal_hospital_beds"
HISTORY_TABLE = "heal_hospital_beds_history"
GEOMETRY_TYPE = "Point"

# Extract
res = get_data_taipei_api(RID)
raw_data = pd.DataFrame(res)
raw_data["data_time"] = get_data_taipei_file_last_modified_time(PAGE_ID)

# Combine with heal_hospital_data
# Config
RID = "04a3d195-ee97-467a-b066-e471ff99d15d"
PAGE_ID = "ffdd5753-30db-4c38-b65f-b77892773d60"
FROM_CRS = 4326
# Extract
res = get_data_taipei_api(RID)
raw_heal_hospital_data = pd.DataFrame(res)
raw_heal_hospital_data = raw_heal_hospital_data[['機構名稱', 'x', 'y']]
# Combine two data with 機構名稱
data = pd.merge(raw_data, raw_heal_hospital_data, on="機構名稱", how="left")

# Extract district
data["district"] = data["地址"].str.split("區").str[0] + "區"
data["district"] = data["district"].str.split("市").str[-1]

# Transform
# Rename
data.columns = data.columns.str.lower()
# Rename columns
rename_map = {
    "機構名稱": "name",
    "地址": "addr",
    "x": "lng",
    "y": "lat",
    "電話": "phone",
    '急性一般病床數': 'acute_general_beds', 
    '急性精神病床數': 'acute_psychiatric_beds',
    '慢性一般病床數': 'chronic_general_beds',
    '慢性精神病床數': 'chronic_psychiatric_beds',
    '安寧病床數': 'palliative_beds',
    '加護病床（icu）': 'icu_beds',
    '急性呼吸照護病床': 'acute_respiratory_care_beds',
    '慢性呼吸照護病床': 'chronic_respiratory_care_beds',
    '燒傷病床': 'burn_beds',
    '急診觀察床': 'emergency_observation_beds',
    '其他觀察病床': 'other_observation_beds',
    '手術恢復床': 'surgical_recovery_beds',
    '嬰兒床': 'baby_beds',
    '嬰兒病床': 'baby_sick_beds',
    '血液透析病床': 'hemodialysis_beds',
    '腹膜透析病床': 'peritoneal_dialysis_beds',
    '精神科加護病床': 'psychiatric_icu_beds',
    '燒傷加護病床': 'burn_icu_beds',
    '普通隔離病床': 'general_isolation_beds',
    '正壓隔離病床': 'positive_pressure_isolation_beds',
    '負壓隔離病床': 'negative_pressure_isolation_beds',
    '骨髓移植病床': 'bone_marrow_transplant_beds'
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
# # Reshape
gdata = gdata.drop(columns=["geometry", "_id"])

# ready_data
ready_col = [
    "data_time", "name", "addr", "district", "lng", "lat", "wkb_geometry",
    "phone", "acute_general_beds", "acute_psychiatric_beds", "chronic_general_beds",
    "chronic_psychiatric_beds", "palliative_beds", "icu_beds", "acute_respiratory_care_beds",
    "chronic_respiratory_care_beds", "burn_beds", "emergency_observation_beds",
    "other_observation_beds", "surgical_recovery_beds", "baby_beds", "baby_sick_beds",
    "hemodialysis_beds", "peritoneal_dialysis_beds", "psychiatric_icu_beds",
    "burn_icu_beds", "general_isolation_beds", "positive_pressure_isolation_beds",
    "negative_pressure_isolation_beds", "bone_marrow_transplant_beds"
]
ready_data = gdata[ready_col]
# save .csv
save_path = os.path.join(dags_path, "proj_city_dashboard", "heal_hospital_beds", "ready_data.csv")
ready_data.to_csv(save_path, index=False)

# Load
# Load data to DB
# engine = create_engine(READY_DATA_DB_URI)
# save_geodataframe_to_postgresql(
#     engine,
#     gdata=ready_data,
#     load_behavior=LOAD_BEHAVIOR,
#     default_table=DEFAULT_TABLE,
#     history_table=HISTORY_TABLE,
#     geometry_type=GEOMETRY_TYPE,
# )
