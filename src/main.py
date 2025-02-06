import argparse
from immich_api.client import get_images
from immich_api.uploader import create_album, add_images_to_album, list_albums
from analysis.blip import analyze_caption
from analysis.scene import analyze_scene
from analysis.object import analyze_object
from clustering.time_based import cluster_images
from clustering.location_based import generate_location_based_album
from utils.geocode import get_location_name
from database.queries import save_metadata, get_existing_metadata
from utils.logger import logger, enable_debug 

def process_images(rerun=False, specific_image_id=None):
    """
    Process images from Immich, extract metadata, and group them into albums.
    """
    logger.info("📸 Starting image processing...")

    images = get_images()

    if specific_image_id:
        images = [img for img in images if img["id"] == specific_image_id]
        if not images:
            logger.warning(f"❌ Image ID {specific_image_id} not found.")
            return

    if not images:
        logger.info("✅ No new images to process.")
        return

    for img in images:
        image_id = img["id"]

        if not rerun and get_existing_metadata(image_id):
            logger.info(f"✅ Skipping image {image_id}, already processed.")
            continue  

        logger.info(f"🔍 Processing image {image_id}...")

        # Reverse geocode location
        latitude, longitude = img.get("latitude"), img.get("longitude")
        city, country = get_location_name(latitude, longitude) if latitude and longitude else (None, None)
        location_name = f"{city}, {country}" if city else country

        # Analyze metadata
        metadata = {
            "taken_at": img["takenAt"],
            "latitude": latitude,
            "longitude": longitude,
            "location": location_name,
            "caption": analyze_caption(img),
            "scene": analyze_scene(img),
            "object": analyze_object(img),
            "albums": []  
        }

        save_metadata(image_id, metadata)
        logger.info(f"✅ Metadata saved for image {image_id}.")

    # Cluster images and create albums
    clusters = cluster_images(images)
    for cluster_id, cluster_images in clusters.items():
        album_name = generate_location_based_album(cluster_images)
        if album_name:
            logger.info(f"📂 Creating album: {album_name}")
            album_id = create_album(album_name)
            if album_id:
                image_ids = [img["id"] for img in cluster_images]
                add_images_to_album(album_id, image_ids)
                logger.info(f"✅ Album '{album_name}' created and images added.")

    logger.info("✅ Image processing completed.")

def main():
    parser = argparse.ArgumentParser(
        description="📸 Process and organize images from Immich into meaningful albums based on location and time.",
        epilog="Example usage:\n  python main.py --rerun\n  python main.py --image-id <IMAGE_ID>\n  python main.py --list-albums",
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    parser.add_argument(
        "--rerun",
        action="store_true",
        help="🔄 Reprocess all images, even if they were previously analyzed."
    )
    
    parser.add_argument(
        "--image-id",
        type=str,
        help="📷 Reprocess a specific image by providing its IMAGE_ID."
    )
    
    parser.add_argument(
        "--debug",
        action="store_true",
        help="🐛 Enable debug mode to display more detailed output."
    )
    
    parser.add_argument(
        "--list-albums",
        action="store_true",
        help="📂 List existing albums in Immich."
    )

    args = parser.parse_args()

    if args.debug:
        enable_debug()

    if args.list_albums:
        logger.info("📂 Available Albums:")
        for album in list_albums():
            logger.info(f"  - {album}")
        return

    process_images(rerun=args.rerun, specific_image_id=args.image_id)

if __name__ == "__main__":
    main()
