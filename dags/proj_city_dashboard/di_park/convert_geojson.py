# convert di_park.csv to di_park_point.geojson
import pandas as pd
import geopandas as gpd
import os
import sys

dags_path = os.path.join(os.getcwd(), 'dags')  # Should be looks like '.../dags'
sys.path.append(dags_path)

# 匯入資料
path = os.path.join(dags_path, "proj_city_dashboard", "di_park", "di_park.csv")
data = pd.read_csv(path)

# convert to geojson
gdf = gpd.GeoDataFrame(data, geometry=gpd.points_from_xy(data.pm_longitude, data.pm_latitude))
gdf = gdf.drop(columns=["pm_longitude", "pm_latitude"])

# save
save_path = os.path.join(dags_path, "proj_city_dashboard", "di_park", "di_park_point.geojson")
# gdf.to_file(save_path, driver="GeoJSON")
print(gdf.columns)

# ## key: col_name, name: display_name
[{"key": "seqno", "name": "編號"},{"key": "pm_name", "name": "公園名稱"},{"key": "pm_unit", "name": "公園管理單位"},{"key":"district", "name":"行政區"}, {"key": "pm_location", "name": "公園位置"},{"key": "di_hospital", "name": "最近醫院"},{"key": "capacity", "name": "容納人數"}]