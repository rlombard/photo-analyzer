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
- **Reverse Geocoding**:  
  Converts GPS coordinates to city/country names for improved album naming.
- **PostgreSQL Integration**:  
  Stores all processed metadata in a relational database.
- **Robust Logging**:  
  Logs events to both the console and a file with adjustable debug levels.
- **Error Handling**:  
  Ensures the process continues gracefully even if errors occur.

---

## 📦 Installation

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/rlombard/photo-analyzer.git
cd photo-analyzer
```

### **2️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **3️⃣ Configure the Application**
Edit the **config.py** file to set:
- **Immich API credentials**
- **Database connection details**
- **AI model selections**

Example configuration:
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

# Model Cache Directory
MODEL_CACHE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "models"))

# Clustering Parameters
TIME_CLUSTERING_EPS = 86400  # 1 day in seconds
TIME_CLUSTERING_MIN_SAMPLES = 3  # Minimum images per cluster
```

---

## 🎯 Usage

### **1️⃣ Run Image Processing**
```sh
python main.py
```
This command will:
- Fetch new images from Immich.
- Process them to extract metadata.
- Organize them into albums based on time and location.

### **2️⃣ Reprocess All Images**
```sh
python main.py --rerun
```
Forces reprocessing of all images, even if they've been processed before.

### **3️⃣ Reprocess a Specific Image**
```sh
python main.py --image-id <IMAGE_ID>
```
Processes a single image identified by its Immich ID.

### **4️⃣ Enable Debug Mode**
```sh
python main.py --debug
```
Activates detailed logging to help with troubleshooting.

### **5️⃣ List Existing Albums**
```sh
python main.py --list-albums
```
Displays a list of current albums in Immich.

---

## 📂 Project Structure

```
photo-analyzer/
│── main.py                # Entry point
│── requirements.txt       # Dependencies
│── README.md              # Project Documentation
│── config.py              # Configuration (API, DB, Models)
│
├── database/
│   ├── connection.py      # Database connection & table creation
│   ├── queries.py         # Database queries for metadata
│
├── immich_api/
│   ├── client.py          # Fetches images from Immich
│   ├── uploader.py        # Creates albums and adds images
│
├── analysis/
│   ├── blip.py            # Image captioning
│   ├── scene.py           # Scene classification
│   ├── object.py          # Object detection
│
├── clustering/
│   ├── time_based.py      # Clusters images by time
│   ├── location_based.py  # Clusters images by location
│
├── utils/
│   ├── download_models.py # Model downloader
│   ├── geocode.py         # Reverse geocoding
│   ├── helpers.py         # Helper functions
│   ├── logger.py          # Logging configuration (console & file)
│   ├── model_loader.py    # Centralized model loading
│
└── logs/
    ├── app.log            # Log file for debugging
```

---

## 🚀 Updates & Enhancements

- **Database connection pooling** implemented for efficiency.
- **AI model loading refactored** to `utils/model_loader.py`.
- **Clustering parameters** now configurable via `config.py`.
- **Utility functions centralized** in `utils/helpers.py`.

---

## 🛠️ Troubleshooting

### **Database Connection Issues**
- Ensure PostgreSQL is running and configured:
  ```sh
  psql -h localhost -U your_db_user -d immich_db
  ```
- The connection pool manages connections automatically.

### **Immich API Issues**
- Ensure Immich is accessible at the configured `IMMICH_URL`.
- Test API connectivity:
  ```sh
  curl -H "Authorization: Bearer your_immich_api_key" http://192.168.0.217:2283/api/albums
  ```

---

## 📜 License
This software is released under the **Unlicense**.

This means:
- The code is **fully open-source** and can be used by anyone for any purpose.
- There are **no restrictions** on how you can modify, distribute, or commercialize the software.
- The software is provided **as-is**, without any warranty or liability.

For more details, see: [https://unlicense.org](https://unlicense.org)

---

## 🤝 Contributing
Contributions, issues, and feature requests are welcome!

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/fooBar`).
3. Commit your changes (`git commit -am 'Add some fooBar'`).
4. Push to the branch (`git push origin feature/fooBar`).
5. Create a new Pull Request.

---

## ⭐ Acknowledgments
- **Hugging Face Transformers** for AI models.
- **Immich** for image management.
- **PostgreSQL** for structured data storage.
- **OpenStreetMap** for reverse geocoding.

🔥 **Automate your image processing with AI-powered metadata and smart albums!** 🚀

