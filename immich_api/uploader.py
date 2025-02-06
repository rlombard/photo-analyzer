import requests
from config import IMMICH_URL, API_KEY
from utils.logger import logger

def create_album(album_name):
    """
    Create a new album in Immich.
    Logs success or failure.
    """
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    data = {"albumName": album_name}

    try:
        response = requests.post(f"{IMMICH_URL}/api/albums", json=data, headers=headers)

        if response.status_code == 200:
            album_id = response.json()["id"]
            logger.info(f"📂 Album '{album_name}' created successfully (ID: {album_id}).")
            return album_id
        else:
            logger.error(f"❌ Failed to create album '{album_name}'. HTTP {response.status_code}: {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        logger.error(f"❌ Network error while creating album '{album_name}': {e}")
        return None

def add_images_to_album(album_id, image_ids):
    """
    Add images to an existing album in Immich.
    Logs success or failure.
    """
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    data = {"assetIds": image_ids}

    try:
        response = requests.post(f"{IMMICH_URL}/api/albums/{album_id}/add", json=data, headers=headers)

        if response.status_code == 200:
            logger.info(f"📸 Successfully added {len(image_ids)} images to album ID {album_id}.")
            return True
        else:
            logger.error(f"❌ Failed to add images to album {album_id}. HTTP {response.status_code}: {response.text}")
            return False
    except requests.exceptions.RequestException as e:
        logger.error(f"❌ Network error while adding images to album {album_id}: {e}")
        return False

def list_albums():
    """
    Fetch all albums from Immich.
    Logs success or failure.
    """
    headers = {"Authorization": f"Bearer {API_KEY}"}

    try:
        response = requests.get(f"{IMMICH_URL}/api/albums", headers=headers)

        if response.status_code == 200:
            albums = [album["albumName"] for album in response.json()]
            logger.info(f"📂 Retrieved {len(albums)} albums from Immich.")
            return albums
        else:
            logger.error(f"❌ Failed to fetch albums. HTTP {response.status_code}: {response.text}")
            return []
    except requests.exceptions.RequestException as e:
        logger.error(f"❌ Network error while fetching albums: {e}")
        return []
