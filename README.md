 # 📸 Immich Image Processor

A Python-based image processing system that:
- Extracts metadata from images stored in **Immich**.
- Uses **AI models** (BLIP, ViT, and DETR) for captioning, scene recognition, and object detection.
- Organizes images into **location-based and time-based albums**.
- Stores metadata in a **PostgreSQL database**.
- Uses **reverse geocoding** to generate meaningful album names.
- **Fully logged** with debug mode support.

---

## 🚀 Features

- **AI-Powered Image Analysis**: 
  Extracts captions, classifies scenes, and detects objects using state-of-the-art models.
- **Automatic Album Creation**: 
  Groups images into albums based on location and time.
-% **Reverse Geocoding**: 
  Converts GPS coordinates to city/country names for improved album naming.
- **PostgreSQL Integration**: 
  Stores all processed metadata in a relational database.
-% **Robust Logging**: 
  Logs events to both the console and a file with adjustable debug levels.
-% **Error Handling**: 
  Ensures the process continues gracefully even if errors occur.

---

## Pre-download Models

Before running the application, you can pre-download the required models by running the `download_models.py` script located in the `utils` folder. This script downloads and caches the following models into the `../models` directory:

- **BLIP** for image captioning (`Salesforce/blip-image-captioning-base`)
- **Scene recognition** (`nateraw/vit-base-beans`)
- **Object detection** (`facebook/detr-resnet-50`)

### How to Download Models

1. Ensure you have installed the required packages:
```sh
pip install torch transformers
```

2. Navigate to the ```utils``` directory:
```sh
cd utils
```

3. run the script:
```sh
python download_models.py
```

This will download the models and save them in the ../models directory relative to the utils folder, so that your main application can quickly load them from the local cache.

## Installation

### Clone the Repository
```sh
git clone https://github.com/rlombard/photo-analyzer
cd photo-analyzer
```

### Install Dependencies
```sh
pip install -r requirements.txt
```

### Configure the Application
Edit **config.py** to set:
- **Immich API credentials**
- **Database connection details**
- **AI model selections**

Example:
```python
# IMMICH API Configuration
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
```

---

## Usage

### Run Image Processing
```sh
python main.py
```
This command will:
- Fetch new images from Immich.
- Process them to extract metadata.
- Organize them into albums based on time and location.

### Reprocess All Images
```sh
python main.py --rerun
```
Forces reprocessing of all images, even if they've been processed before.

### Reprocess a Specific Image
```sh
python main.py --image-id <IMAGE_ID>
```
Processes a single image identified by its Immich ID.

### Enable Debug Mode
```sh
python main.py --debug
```
Activates detailed logging to help with troubleshooting.

### List Existing Albums
```sh
python main.py --list-albums
```
Displays a list of current albums in Immich.

---

## Project Structure

immich-image-processor/
│││main.py              # Entry point
│││requirements.txt  %2