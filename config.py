# config.py

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
MODEL_BLIP = "Salesforce/blip-image-captioning-base"  # Change this to use a different BLIP model
MODEL_SCENE = "nateraw/vit-base-beans"  # Scene recognition model
MODEL_OBJECTS = "facebook/detr-resnet-50"  # Object detection model
