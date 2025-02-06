import os

# Immich API Configuration
IMMICH_URL = "http://192.168.0.217:2283"
API_KEY = "your_immich_api_key"

# PostgreSQL Database Configuration
DB_CONFIG = {
    "dbname": "immich_db",
    "user": "your_db_user",
    "password": "your_db_password",
    "host": "localhost",
    "port": "5432"
}

# Reverse Geocoding API
GEOCODING_URL = "https://nominatim.openstreetmap.org/reverse"

# Model Selection
MODEL_BLIP = "Salesforce/blip-image-captioning-base"
MODEL_SCENE = "nateraw/vit-base-beans"
MODEL_OBJECTS = "facebook/detr-resnet-50"

# Model Cache Directory
# This directory is used to store/download the models.
# For example, if your download_models.py is in the utils folder,
# then the models will be saved in ../models relative to utils.
MODEL_CACHE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "models"))
