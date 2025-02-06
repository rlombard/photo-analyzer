#!/usr/bin/env python3
"""
download_models.py

This script downloads and caches the required models into the ../models directory:
- BLIP for image captioning ("Salesforce/blip-image-captioning-base")
- Scene recognition ("nateraw/vit-base-beans")
- Object detection ("facebook/detr-resnet-50")

Usage:
    python download_models.py
"""

import logging
import sys
import os

# Set the directory where models will be cached.
# Since this script is in the "utils" folder, "../models" is relative to it.
CACHE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "models"))

def download_blip():
    try:
        from transformers import BlipProcessor, BlipForConditionalGeneration
        model_name = "Salesforce/blip-image-captioning-base"
        logging.info(f"Downloading BLIP model: {model_name} into {CACHE_DIR}")
        # Download and cache the model and processor
        _ = BlipProcessor.from_pretrained(model_name, cache_dir=CACHE_DIR)
        _ = BlipForConditionalGeneration.from_pretrained(model_name, cache_dir=CACHE_DIR)
        logging.info("BLIP model downloaded successfully.")
    except Exception as e:
        logging.error(f"Error downloading BLIP model: {e}")
        sys.exit(1)

def download_scene():
    try:
        from transformers import ViTForImageClassification, ViTFeatureExtractor
        model_name = "nateraw/vit-base-beans"
        logging.info(f"Downloading scene recognition model: {model_name} into {CACHE_DIR}")
        # Download and cache the model and feature extractor
        _ = ViTFeatureExtractor.from_pretrained(model_name, cache_dir=CACHE_DIR)
        _ = ViTForImageClassification.from_pretrained(model_name, cache_dir=CACHE_DIR)
        logging.info("Scene recognition model downloaded successfully.")
    except Exception as e:
        logging.error(f"Error downloading scene recognition model: {e}")
        sys.exit(1)

def download_object():
    try:
        from transformers import ViTForImageClassification, ViTFeatureExtractor
        model_name = "facebook/detr-resnet-50"
        logging.info(f"Downloading object detection model: {model_name} into {CACHE_DIR}")
        # Download and cache the model and feature extractor
        _ = ViTFeatureExtractor.from_pretrained(model_name, cache_dir=CACHE_DIR)
        _ = ViTForImageClassification.from_pretrained(model_name, cache_dir=CACHE_DIR)
        logging.info("Object detection model downloaded successfully.")
    except Exception as e:
        logging.error(f"Error downloading object detection model: {e}")
        sys.exit(1)

def main():
    # Ensure the cache directory exists
    if not os.path.exists(CACHE_DIR):
        os.makedirs(CACHE_DIR)
        logging.info(f"Created cache directory at {CACHE_DIR}")

    # Set up logging to output to console
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
    )
    
    logging.info("Starting model downloads...")
    download_blip()
    download_scene()
    download_object()
    logging.info("All models downloaded successfully.")

if __name__ == "__main__":
    main()
