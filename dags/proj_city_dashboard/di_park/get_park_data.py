# API
# 公園情報：https://parks.taipei/parks/api/
# 防災公園：https://parks.taipei/parks/json/

import requests
import json
import pandas as pd
import os
import sys
dags_path = os.path.join(os.getcwd(), 'dags')  # Should be looks like '.../dags'
sys.path.append(dags_path)

# 取得公園資料
url = "https://parks.taipei/parks/api/"
response = requests.get(url)
data = response.json()
df = pd.DataFrame(data)
use_cols = ['SeqNo', 'pm_name', 'pm_Longitude', 'pm_Latitude',
       'pm_unit', 'pm_location']
selected_df = df[use_cols]
# Save to csv
save_path = os.path.join(dags_path, "proj_city_dashboard", "di_park", "park_data.csv")
selected_df.to_csv(save_path, index=False)

# 取得防災公園資料
url = "https://parks.taipei/parks/json/"
response = requests.get(url)
data = response.json()
df = pd.DataFrame(data)
use_cols = ['pm_name', 'di_capacity', 'di_hospital', 'di_fire', 'di_police']
selected_df = df[use_cols]
# Save to csv
save_path = os.path.join(dags_path, "proj_city_dashboard", "di_park", "disaster_park_data.csv")
selected_df.to_csv(save_path, index=False)


############################################################################################################
# merge
dags_path = os.path.join(os.getcwd(), 'dags')  # Should be looks like '.../dags'
sys.path.append(dags_path)

# use ready_data
df_park = pd.read_csv(os.path.join(dags_path, "proj_city_dashboard", "di_park", "park_data.csv"))
df_disaster_park = pd.read_csv(os.path.join(dags_path, "proj_city_dashboard", "di_park", "disaster_park_data.csv"))

# merge two dataframes(以pm_name為key合併，只保留右邊的資料，即防災公園資料)
df = pd.merge(df_park, df_disaster_park, on='pm_name', how='right')
# str to numeric
df['capacity'] = pd.to_numeric(df['di_capacity'].str.replace(",", ""), errors='coerce')
# drop NA
df = df.dropna(subset=['capacity'])
df = df.drop(columns=["di_capacity"])

# save to csv
save_path = os.path.join(dags_path, "proj_city_dashboard", "di_park", "ready_data.csv")
df.to_csv(save_path, index=False)

# # Convert to GeoJSON
# gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.pm_Longitude, df.pm_Latitude))
# gdf = gdf.drop(columns=["pm_Longitude", "pm_Latitude"])

# # Save GeoJSON
# save_path = os.path.join(dags_path, "proj_city_dashboard", "di_park")
# gdf.to_file(os.path.join(save_path, "park.geojson"), driver="GeoJSON")

