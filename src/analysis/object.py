import torch
from transformers import ViTForImageClassification, ViTFeatureExtractor
from utils.logger import logger
from config import MODEL_OBJECTS, MODEL_CACHE_DIR

try:
    feature_extractor = ViTFeatureExtractor.from_pretrained(MODEL_OBJECTS, cache_dir=MODEL_CACHE_DIR)
    model = ViTForImageClassification.from_pretrained(MODEL_OBJECTS, cache_dir=MODEL_CACHE_DIR)
    logger.info(f"✅ Object detection model '{MODEL_OBJECTS}' loaded successfully from cache directory {MODEL_CACHE_DIR}.")
except Exception as e:
    logger.error(f"❌ Failed to load object detection model '{MODEL_OBJECTS}' from cache directory {MODEL_CACHE_DIR}: {e}")
    raise

def analyze_object(image):
    """Detect objects in an image using a Vision Transformer model."""
    try:
        inputs = feature_extractor(image, return_tensors="pt")
        with torch.no_grad():
            object_preds = model(**inputs).logits
        detected_object = model.config.id2label[object_preds.argmax().item()]
        logger.info(f"🛠️ Detected object: {detected_object}")
        return detected_object
    except Exception as e:
        logger.error(f"❌ Error detecting objects: {e}")
        return None
