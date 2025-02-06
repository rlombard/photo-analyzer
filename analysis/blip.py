import torch
from transformers import BlipProcessor, BlipForConditionalGeneration
from utils.logger import logger
from config import MODEL_BLIP, MODEL_CACHE_DIR

try:
    processor = BlipProcessor.from_pretrained(MODEL_BLIP, cache_dir=MODEL_CACHE_DIR)
    model = BlipForConditionalGeneration.from_pretrained(MODEL_BLIP, cache_dir=MODEL_CACHE_DIR)
    logger.info(f"✅ BLIP model '{MODEL_BLIP}' loaded successfully from cache directory {MODEL_CACHE_DIR}.")
except Exception as e:
    logger.error(f"❌ Failed to load BLIP model '{MODEL_BLIP}' from cache directory {MODEL_CACHE_DIR}: {e}")
    raise

def analyze_caption(image):
    """Generate a caption for an image using BLIP."""
    try:
        inputs = processor(image, return_tensors="pt")
        with torch.no_grad():
            caption = model.generate(**inputs)
        generated_caption = processor.batch_decode(caption, skip_special_tokens=True)[0]
        logger.info(f"📝 Generated caption: {generated_caption}")
        return generated_caption
    except Exception as e:
        logger.error(f"❌ Error generating caption: {e}")
        return None
