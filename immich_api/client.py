import requests
from config import IMMICH_URL, API_KEY
from utils.logger import logger

def get_images():
    """
    Fetch images from Immich API.
    Logs success or failure.
    """
    headers = {"Authorization": f"Bearer {API_KEY}"}
    try:
        response = requests.get(f"{IMMICH_URL}/api/assets", headers=headers)

        if response.status_code == 200:
            images = response.json()["assets"]
            logger.info(f"📸 Successfully fetched {len(images)} images from Immich.")
            return images
        else:
            logger.error(f"❌ Failed to fetch images. HTTP {response.status_code}: {response.text}")
            return []
    except requests.exceptions.RequestException as e:
        logger.error(f"❌ Network error while fetching images: {e}")
        return []
