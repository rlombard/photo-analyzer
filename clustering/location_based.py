from collections import Counter
from utils.logger import logger

def generate_location_based_album(cluster_images):
    """
    Generate a meaningful album name based on locations in a cluster.
    
    Naming rules:
    - If the majority of images (>=50%) are from the same city, use that city (e.g., "Paris - YYYY-MM").
    - If images are from multiple cities within a single country, use the country (e.g., "France Trip - YYYY-MM").
    - If images span multiple countries, label it as an international trip (e.g., "International Trip - YYYY-MM").
    
    The date range is determined by the first image's takenAt field (format "YYYY-MM").
    """
    try:
        # Extract valid location strings from images
        locations = [img["location"] for img in cluster_images if img.get("location")]
        if not locations:
            logger.warning("⚠️ No valid location data found for this cluster.")
            return None

        # For each location, attempt to split into city and country.
        # Expecting format "City, Country" or just "Country".
        cities = []
        countries = []
        for loc in locations:
            parts = [part.strip() for part in loc.split(",")]
            if len(parts) >= 2:
                cities.append(parts[0])
                countries.append(parts[-1])
            else:
                countries.append(parts[0])

        date_range = cluster_images[0]["takenAt"][:7]  # Format: "YYYY-MM"

        album_name = None
        if cities:
            city_counts = Counter(cities)
            most_common_city, city_freq = city_counts.most_common(1)[0]
            # If at least half the images come from the same city, use that city
            if city_freq >= len(cluster_images) / 2:
                album_name = f"{most_common_city} - {date_range}"
            else:
                country_counts = Counter(countries)
                if len(country_counts) == 1:
                    # Multiple cities but within a single country
                    most_common_country = list(country_counts.keys())[0]
                    album_name = f"{most_common_country} Trip - {date_range}"
                else:
                    # Images span multiple countries
                    album_name = f"International Trip - {date_range}"
        else:
            # No city info; rely on countries
            country_counts = Counter(countries)
            if len(country_counts) == 1:
                album_name = f"{list(country_counts.keys())[0]} Trip - {date_range}"
            else:
                album_name = f"International Trip - {date_range}"

        logger.info(f"📍 Generated location-based album: {album_name}")
        return album_name

    except Exception as e:
        logger.error(f"❌ Error generating location-based album: {e}")
        return None
