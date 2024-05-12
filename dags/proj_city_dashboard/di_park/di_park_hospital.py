import pandas as pd
import os
import sys
import numpy as np
import json

dags_path = os.path.join(os.getcwd(), 'dags')  # Should be looks like '.../dags'
sys.path.append(dags_path)

# Import di_park data
path = os.path.join(dags_path, "proj_city_dashboard", "di_park", "di_park.csv")
data = pd.read_csv(path)

# Import hospital data
hospital_path = os.path.join(dags_path, "proj_city_dashboard", "heal_hospital_beds", "ready_data.csv")
hospital_data = pd.read_csv(hospital_path)

# Extract latitude and longitude data, handle NA values
di_lonlat = data[["pm_longitude", "pm_latitude"]].dropna()
hospital_lonlat = hospital_data[["lng", "lat"]].dropna()

# Calculate distances and find the nearest hospitals
nearest_hospital = []
for i in range(len(di_lonlat)):
    distances = []
    for j in range(len(hospital_lonlat)):
        distance = np.sqrt((di_lonlat.iloc[i, 0] - hospital_lonlat.iloc[j, 0])**2 + (di_lonlat.iloc[i, 1] - hospital_lonlat.iloc[j, 1])**2)
        distances.append(distance)
    nearest_hospital.append(np.argsort(distances)[0])

# Add the names of the nearest hospitals to the di_park data
hospital_names = hospital_data["name"].values
nearest_hospital_names = [hospital_names[i] for i in nearest_hospital]
data["nearest_hospital"] = nearest_hospital_names

# Create a geojson file
features = []
for i in range(len(nearest_hospital)):
    park_coords = (di_lonlat.iloc[i, 0], di_lonlat.iloc[i, 1])  # Longitude, Latitude
    hospital_coords = (hospital_lonlat.iloc[nearest_hospital[i], 0], hospital_lonlat.iloc[nearest_hospital[i], 1])  # Longitude, Latitude
    feature = {
        "type": "Feature",
        "properties": {
            "park_name": data.iloc[i, 0],
            "hospital_name": nearest_hospital_names[i]
        },
        "geometry": {
            "type": "LineString",
            "coordinates": [list(park_coords), list(hospital_coords)]
        }
    }
    features.append(feature)

geojson_data = {
    "type": "FeatureCollection",
    "features": features
}

# Write GeoJSON data to file
output_path = os.path.join(dags_path, "proj_city_dashboard", "di_park", "di_park_hospital.geojson")
with open(output_path, "w") as output_file:
    json.dump(geojson_data, output_file, default=str)

print("GeoJSON file has been created successfully.")
