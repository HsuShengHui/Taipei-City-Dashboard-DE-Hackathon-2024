import os
import sys

dags_path = os.path.join(os.getcwd(), 'dags')  # Should be looks like '.../dags'
sys.path.append(dags_path)
import pandas as pd
import geopandas as gpd

# use ready_data
table_name = "medicine"
path = os.path.join(dags_path, "proj_city_dashboard", "medicine", "ready_data.csv")
data = pd.read_csv(path)


# Convert to GeoJSON
gdf = gpd.GeoDataFrame(data, geometry=gpd.points_from_xy(data.lng, data.lat))
gdf = gdf.drop(columns=["lng", "lat"])

# Save GeoJSON
# C:\Users\h2408\GitHub\Taipei-City-Dashboard\Taipei-City-Dashboard-FE\public\mapData
save_path = "C:\\Users\\h2408\\GitHub\\Taipei-City-Dashboard\\Taipei-City-Dashboard-FE\\public\\mapData"
#gdf.to_file(os.path.join(save_path, f"{table_name}.geojson"), driver="GeoJSON")
#gdf.to_file(f"{table_name}.geojson", driver="GeoJSON")

# key: col_name, name: display_name
#[{"key": "name", "name": "名稱"}, {"key": "addr", "name": "地址"},{"key": "phone", "name": "電話"},{"key": "total_beds", "name": "總病床數"}]
[{"key": "name", "name": "名稱"}, {"key": "addr", "name": "地址"},{"key": "phone", "name": "電話"}]