import os

# Immich API Configuration
IMMICH_URL = "http://192.168.0.217:2283"
API_KEY = "hAmOd1lwRTmvS2qnWkbumsWYDLYc6BQZ1ukCL9QfxSU"

# PostgreSQL Database Configuration
DB_CONFIG = {
    "dbname": "immich_db",
    "user": "root",
    "password": "Lekker@rm.8db_postgres",
    "host": "192.168.0.216",
    "port": "5432"
}

# Reverse Geocoding API
GEOCODING_URL = "https://nominatim.openstreetmap.org/reverse"

# Model Selection
MODEL_BLIP = "Salesforce/blip-image-captioning-base"
MODEL_SCENE = "nateraw/vit-base-beans"
MODEL_OBJECTS = "facebook/detr-resnet-50"

# Model Cache Directory
MODEL_CACHE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "models"))

# Clustering Parameters
TIME_CLUSTERING_EPS = 86400  # 1 day in seconds
TIME_CLUSTERING_MIN_SAMPLES = 3  # Minimum images per cluster
