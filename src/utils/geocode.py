import requests
from config import GEOCODING_URL
from utils.logger import logger

def get_location_name(latitude, longitude):
    """
    Reverse geocode GPS coordinates to get a city and country name.
    Logs success, warnings, or failures.
    """
    if latitude is None or longitude is None:
        logger.warning("⚠️ Missing latitude or longitude. Cannot perform reverse geocoding.")
        return None

    params = {"lat": latitude, "lon": longitude, "format": "json"}

    try:
        response = requests.get(GEOCODING_URL, params=params, timeout=5)

        if response.status_code == 200:
            data = response.json()
            city = data.get("address", {}).get("city") or data.get("address", {}).get("town") or data.get("address", {}).get("village")
            country = data.get("address", {}).get("country")

            if city and country:
                location_name = f"{city}, {country}"
            elif country:
                location_name = country
            else:
                logger.warning(f"⚠️ No meaningful location found for coordinates ({latitude}, {longitude}).")
                return None

            logger.info(f"📍 Reverse geocoded location: {location_name}")
            return location_name
        else:
            logger.error(f"❌ Failed to reverse geocode coordinates ({latitude}, {longitude}). HTTP {response.status_code}: {response.text}")
            return None
    except requests.exceptions.Timeout:
        logger.error(f"❌ Geocoding request timed out for coordinates ({latitude}, {longitude}).")
        return None
    except requests.exceptions.RequestException as e:
        logger.error(f"❌ Network error while reverse geocoding ({latitude}, {longitude}): {e}")
        return None
