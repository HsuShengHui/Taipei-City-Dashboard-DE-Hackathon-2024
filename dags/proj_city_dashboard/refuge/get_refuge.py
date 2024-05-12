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
RID = "e7aecde4-ef04-46e3-849b-1ee159ea6d5f"
PAGE_ID = "29a13836-028e-430d-bf5d-18ad3850f178"
FROM_CRS = 4326
# Extract
res = get_data_taipei_api(RID)
raw_refuge_data = pd.DataFrame(res)
print(raw_refuge_data)