from collections import Counter
from utils.logger import logger

def generate_location_based_album(cluster_images):
    """
    Generate a meaningful album name based on locations in a cluster.

    If all images are from the same city -> "Paris - March 2025"
    If multiple cities but one country -> "France Trip - March 2025"
    If multiple countries -> "Europe Trip - March 2025"
    """
    try:
        locations = [img["location"] for img in cluster_images if img.get("location")]

        if not locations:
            logger.warning("⚠️ No valid location data found for this cluster.")
            return None  # No valid location data

        # Count occurrences of cities and countries
        city_counts = Counter([loc.split(",")[0] for loc in locations if loc])
        country_counts = Counter([loc.split(",")[-1] for loc in locations if loc])

        # Most common city and country
        most_common_city, city_freq = city_counts.most_common(1)[0] if city_counts else (None, 0)
        most_common_country, country_freq = country_counts.most_common(1)[0] if country_counts else (None, 0)

        # Get the date range from the images
        date_range = cluster_images[0]["takenAt"][:7]  # YYYY-MM

        # Determine the best album name
        if len(country_counts) == 1:
            if city_freq > 2:  # More than two images in the same city
                album_name = f"{most_common_city} - {date_range}"
            else:
                album_name = f"{most_common_country} Trip - {date_range}"
        else:
            album_name = f"Europe Trip - {date_range}"  # Multiple countries

        logger.info(f"📍 Generated location-based album: {album_name}")
        return album_name

    except Exception as e:
        logger.error(f"❌ Error generating location-based album: {e}")
        return None
