import os
import sys

dags_path = os.path.join(os.getcwd(), 'dags')  # Should be looks like '.../dags'
sys.path.append(dags_path)
import pandas as pd
import geopandas as gpd

# use ready_data
table_name = "heal_hospital_beds"
path = os.path.join(dags_path, "proj_city_dashboard", "heal_hospital_beds", "ready_data.csv")
data = pd.read_csv(path)

# 將全部病床數量加總
data["total_beds"] = data.iloc[:, 8:].sum(axis=1)


# Convert to GeoJSON
gdf = gpd.GeoDataFrame(data, geometry=gpd.points_from_xy(data.lng, data.lat))
gdf = gdf.drop(columns=["lng", "lat"])

# Save GeoJSON
# C:\Users\h2408\GitHub\Taipei-City-Dashboard\Taipei-City-Dashboard-FE\public\mapData
save_path = "C:\\Users\\h2408\\GitHub\\Taipei-City-Dashboard\\Taipei-City-Dashboard-FE\\public\\mapData"
gdf.to_file(os.path.join(save_path, f"{table_name}.geojson"), driver="GeoJSON")

# key: col_name, name: display_name
key_map = [{"key": "name", "name": "名稱"}, {"key": "addr", "name": "地址"},{"key": "phone", "name": "電話"},{"key": "total_beds", "name": "總病床數"}]
