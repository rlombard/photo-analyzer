from utils.logger import logger

def validate_image_data(image):
    """
    Validate image data to ensure it has the necessary fields.
    Logs warnings if data is missing.
    """
    required_fields = ["id", "takenAt", "latitude", "longitude"]

    for field in required_fields:
        if field not in image or image[field] is None:
            logger.warning(f"⚠️ Missing '{field}' in image data (ID: {image.get('id', 'Unknown')}).")
            return False

    return True

def format_album_name(name):
    """
    Format an album name to remove special characters and limit length.
    Logs adjustments made.
    """
    try:
        formatted_name = "".join(c if c.isalnum() or c in " -_" else "_" for c in name)
        formatted_name = formatted_name[:100]  # Limit album name length
        if formatted_name != name:
            logger.info(f"📝 Adjusted album name '{name}' → '{formatted_name}' to meet formatting rules.")
        return formatted_name
    except Exception as e:
        logger.error(f"❌ Error formatting album name '{name}': {e}")
        return "Unnamed_Album"
