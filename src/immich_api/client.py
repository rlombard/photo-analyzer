from config import IMMICH_URL, API_KEY
from utils.logger import logger
from wrappers.api import ImmichApi

# Initialize the Immich API client
immich_api = ImmichApi(IMMICH_URL, API_KEY)

def get_all_assets():
    """
    Fetch all assets using ImmichApi, including metadata.
    """
    try:
        assets = immich_api.get_all_assets()
        for asset in assets:
            asset['metadata'] = immich_api.get_asset_metadata(asset['id'])
        return assets if assets else []
    except Exception as e:
        logger.error(f"Error fetching all assets: {e}")
        return []

def download_image(image_id, save_path):
    """
    Download an image from Immich and save it to a specified path.
    """
    try:
        image_data = immich_api.download_asset(image_id)
        with open(save_path, 'wb') as file:
            file.write(image_data)
        return save_path
    except Exception as e:
        logger.error(f"Error downloading image {image_id}: {e}")
        return None

def update_image_metadata(image_id, metadata):
    """
    Update an image's metadata (tags) in Immich.
    """
    try:
        response = immich_api.update_asset_metadata(image_id, metadata)
        return response
    except Exception as e:
        logger.error(f"Error updating metadata for image {image_id}: {e}")
        return None
