import argparse
from immich_api.client import get_all_assets, download_image, update_image_metadata
from utils.logger import logger, enable_debug
from analysis.object import analyze_object
from analysis.scene import analyze_scene
from analysis.blip import analyze_caption
#from database.queries import store_metadata, get_analyzed_images

def process_assets(image_id=None, rerun=False):
    """Retrieve assets, analyze them, store metadata in DB, and perform clustering."""
    assets = get_all_assets()
    if not assets:
        logger.info("No assets found.")
        return

    #analyzed_images = get_analyzed_images() if not rerun else []

    # if image_id:
    #     assets = [asset for asset in assets if asset["id"] == image_id]
    # else:
    #     # Exclude already analyzed images unless rerun is specified
    #     assets = [asset for asset in assets if asset["id"] not in analyzed_images]
    
    for asset in assets:
        image_id = asset["id"]
        save_path = f"/tmp/{image_id}.jpg"

        # Download image for analysis and clustering
        if download_image(image_id, save_path):
            logger.info(f"Downloaded image {image_id} to {save_path}")

            # Perform analysis
            object_metadata = analyze_object(save_path)
            scene_metadata = analyze_scene(save_path)
            caption_metadata = analyze_caption(save_path)

            # Merge metadata and update image metadata
            new_metadata = {"tags": ["processed", "analyzed"], **object_metadata, **scene_metadata, **caption_metadata}
            #update_image_metadata(image_id, new_metadata)

            # Store metadata in the database
            #store_metadata(image_id, new_metadata)

    # Perform clustering after processing
    #cluster_by_location(assets)
    #cluster_by_time(assets)

def main():
    parser = argparse.ArgumentParser(
        description="\U0001F4F8 Process and organize images from Immich into meaningful albums based on location and time.",
        epilog="Example usage:\n  python main.py --rerun\n  python main.py --image-id <IMAGE_ID>\n  python main.py --list-albums",
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    parser.add_argument("--rerun", action="store_true", help="\U0001F504 Reprocess all images, even if they were previously analyzed.")
    parser.add_argument("--image-id", type=str, help="\U0001F4F7 Reprocess a specific image by providing its IMAGE_ID.")
    parser.add_argument("--debug", action="store_true", help="\U0001F41B Enable debug mode to display more detailed output.")
    
    args = parser.parse_args()

    if args.debug:
        enable_debug()

    process_assets(image_id=args.image_id, rerun=args.rerun)

if __name__ == "__main__":
    main()