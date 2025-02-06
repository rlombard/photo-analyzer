import torch
from transformers import BlipProcessor, BlipForConditionalGeneration, ViTForImageClassification, ViTFeatureExtractor
from config import MODEL_BLIP, MODEL_SCENE, MODEL_OBJECTS, MODEL_CACHE_DIR
from utils.logger import logger

def load_blip():
    """Load BLIP model and processor"""
    try:
        processor = BlipProcessor.from_pretrained(MODEL_BLIP, cache_dir=MODEL_CACHE_DIR)
        model = BlipForConditionalGeneration.from_pretrained(MODEL_BLIP, cache_dir=MODEL_CACHE_DIR)
        logger.info(f"✅ BLIP model '{MODEL_BLIP}' loaded from {MODEL_CACHE_DIR}.")
        return processor, model
    except Exception as e:
        logger.error(f"❌ Failed to load BLIP model: {e}")
        raise

def load_scene_model():
    """Load Scene Classification model"""
    try:
        feature_extractor = ViTFeatureExtractor.from_pretrained(MODEL_SCENE, cache_dir=MODEL_CACHE_DIR)
        model = ViTForImageClassification.from_pretrained(MODEL_SCENE, cache_dir=MODEL_CACHE_DIR)
        logger.info(f"✅ Scene model '{MODEL_SCENE}' loaded from {MODEL_CACHE_DIR}.")
        return feature_extractor, model
    except Exception as e:
        logger.error(f"❌ Failed to load scene model: {e}")
        raise

def load_object_model():
    """Load Object Detection model"""
    try:
        feature_extractor = ViTFeatureExtractor.from_pretrained(MODEL_OBJECTS, cache_dir=MODEL_CACHE_DIR)
        model = ViTForImageClassification.from_pretrained(MODEL_OBJECTS, cache_dir=MODEL_CACHE_DIR)
        logger.info(f"✅ Object detection model '{MODEL_OBJECTS}' loaded from {MODEL_CACHE_DIR}.")
        return feature_extractor, model
    except Exception as e:
        logger.error(f"❌ Failed to load object detection model: {e}")
        raise
