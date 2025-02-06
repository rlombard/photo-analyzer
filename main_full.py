import os
import requests
import datetime
import numpy as np
import psycopg2
from collections import Counter
from sklearn.cluster import DBSCAN
from PIL import Image
from io import BytesIO
from transformers import BlipProcessor, BlipForConditionalGeneration, ViTForImageClassification, ViTFeatureExtractor

# IMMICH API CONFIG
IMMICH_URL = "http://192.168.0.217:2283"
API_KEY = "your_immich_api_key"

# POSTGRES CONFIG
DB_CONFIG = {
    "dbname": "immich_db",
    "user": "your_db_user",
    "password": "your_db_password",
    "host": "localhost",
    "port": "5432"
}

# REVERSE GEOCODING API
GEOCODING_URL = "https://nominatim.openstreetmap.org/reverse"

### REVERSE GEOCODING (LOCATION NAME) ###
def get_location_name(latitude, longitude):
    """Get city and country from GPS coordinates using OpenStreetMap."""
    params = {
        "lat": latitude,
        "lon": longitude,
        "format": "json"
    }
    response = requests.get(GEOCODING_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        city = data.get("address", {}).get("city") or data.get("address", {}).get("town") or data.get("address", {}).get("village")
        country = data.get("address", {}).get("country")
        return (city, country)
    return (None, None)

### CLUSTER LOCATION-BASED ALBUMS ###
def generate_location_based_album(cluster_images):
    """Generate an appropriate album name based on clustered locations."""
    locations = [img["location"] for img in cluster_images if img["location"]]

    if not locations:
        return None  # No valid location data

    # Count occurrences of cities and countries
    city_counts = Counter([loc.split(",")[0] for loc in locations if loc])
    country_counts = Counter([loc.split(",")[-1] for loc in locations if loc])

    # Most common city and country
    most_common_city, city_freq = city_counts.most_common(1)[0] if city_counts else (None, 0)
    most_common_country, country_freq = country_counts.most_common(1)[0] if country_counts else (None, 0)

    # Determine naming pattern
    date_range = datetime.datetime.strptime(cluster_images[0]["takenAt"], "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%B %Y")
    
    if len(country_counts) == 1:
        if city_freq > 2:  # Multiple images in the same city
            return f"{most_common_city} - {date_range}"
        return f"{most_common_country} Trip - {date_range}"
    else:
        return f"Europe Trip - {date_range}"  # Multiple countries in the cluster

### ALBUM MANAGEMENT ###
def create_album(album_name):
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    response = requests.post(f"{IMMICH_URL}/api/albums", json={"albumName": album_name}, headers=headers)
    return response.json()["id"] if response.status_code == 200 else None

def add_images_to_album(album_id, image_ids):
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    response = requests.post(f"{IMMICH_URL}/api/albums/{album_id}/add", json={"assetIds": image_ids}, headers=headers)
    if response.status_code == 200:
        print(f"Added images to album {album_id}")

### LOCATION-BASED IMAGE CLUSTERING ###
def cluster_images(images):
    """Cluster images by time and location."""
    timestamps = np.array([datetime.datetime.strptime(img["takenAt"], "%Y-%m-%dT%H:%M:%S.%fZ").timestamp() for img in images]).reshape(-1, 1)
    clustering = DBSCAN(eps=86400, min_samples=3).fit(timestamps)  # 1-day separation

    clusters = {}
    for img, label in zip(images, clustering.labels_):
        if label != -1:
            if label not in clusters:
                clusters[label] = []
            clusters[label].append(img)
    return clusters

### IMAGE PROCESSING ###
def process_images(rerun=False):
    """Main processing function that fetches images, extracts metadata, and assigns albums."""
    images = get_images()

    for img in images:
        image_id = img["id"]
        if not rerun and get_existing_metadata(image_id):
            continue  # Skip already processed images unless rerun

        image_url = f"{IMMICH_URL}/api/assets/{image_id}/download"
        image = download_image(image_url)
        if not image:
            continue

        # Reverse geocoding
        latitude, longitude = img.get("latitude"), img.get("longitude")
        city, country = get_location_name(latitude, longitude) if latitude and longitude else (None, None)
        location_name = f"{city}, {country}" if city else country

        metadata = {
            "taken_at": img["takenAt"],
            "latitude": latitude,
            "longitude": longitude,
            "location": location_name,
            "albums": []  # To be assigned after clustering
        }

        save_metadata(image_id, metadata)

    # Cluster images and create albums
    clusters = cluster_images(images)
    for cluster_id, cluster_images in clusters.items():
        album_name = generate_location_based_album(cluster_images)
        if album_name:
            album_id = create_album(album_name)
            if album_id:
                image_ids = [img["id"] for img in cluster_images]
                add_images_to_album(album_id, image_ids)

# Run processing
if __name__ == "__main__":
    process_images(rerun=False)
