import torch
from transformers import ViTForImageClassification, ViTFeatureExtractor
from utils.logger import logger
from config import MODEL_SCENE, MODEL_CACHE_DIR

try:
    feature_extractor = ViTFeatureExtractor.from_pretrained(MODEL_SCENE, cache_dir=MODEL_CACHE_DIR)
    model = ViTForImageClassification.from_pretrained(MODEL_SCENE, cache_dir=MODEL_CACHE_DIR)
    logger.info(f"✅ Scene recognition model '{MODEL_SCENE}' loaded successfully from cache directory {MODEL_CACHE_DIR}.")
except Exception as e:
    logger.error(f"❌ Failed to load scene recognition model '{MODEL_SCENE}' from cache directory {MODEL_CACHE_DIR}: {e}")
    raise

def analyze_scene(image):
    """Classify the scene of an image using a Vision Transformer model."""
    try:
        inputs = feature_extractor(image, return_tensors="pt")
        with torch.no_grad():
            scene_preds = model(**inputs).logits
        detected_scene = model.config.id2label[scene_preds.argmax().item()]
        logger.info(f"🌄 Detected scene: {detected_scene}")
        return detected_scene
    except Exception as e:
        logger.error(f"❌ Error classifying scene: {e}")
        return None
