from database.connection import connect_db
from utils.logger import logger

def get_existing_metadata(image_id):
    """
    Retrieve existing metadata for a given image ID.
    Logs success or warning if no record is found.
    """
    try:
        conn = connect_db()
        if not conn:
            logger.error("❌ Database connection failed. Cannot fetch metadata.")
            return None

        cur = conn.cursor()
        cur.execute("SELECT * FROM image_metadata WHERE image_id = %s", (image_id,))
        result = cur.fetchone()
        cur.close()
        conn.close()

        if result:
            logger.info(f"📄 Retrieved metadata for image {image_id}.")
        else:
            logger.warning(f"⚠️ No metadata found for image {image_id}.")

        return result
    except Exception as e:
        logger.error(f"❌ Error fetching metadata for image {image_id}: {e}")
        return None

def save_metadata(image_id, metadata):
    """
    Insert or update metadata for an image in the database.
    Logs when a new entry is created or an existing entry is updated.
    """
    try:
        conn = connect_db()
        if not conn:
            logger.error("❌ Database connection failed. Cannot save metadata.")
            return False

        cur = conn.cursor()
        cur.execute("""
            INSERT INTO image_metadata (image_id, taken_at, latitude, longitude, caption, scene, object, faces, albums, location, processed_at)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, NOW())
            ON CONFLICT (image_id) DO UPDATE 
            SET caption = EXCLUDED.caption, 
                scene = EXCLUDED.scene, 
                object = EXCLUDED.object, 
                faces = EXCLUDED.faces, 
                albums = EXCLUDED.albums, 
                location = EXCLUDED.location,
                processed_at = NOW();
        """, (
            image_id, metadata["taken_at"], metadata["latitude"], metadata["longitude"],
            metadata["caption"], metadata["scene"], metadata["object"], metadata["faces"], metadata["albums"], metadata["location"]
        ))

        conn.commit()
        cur.close()
        conn.close()

        logger.info(f"✅ Metadata saved for image {image_id}. (Inserted or Updated)")
        return True
    except Exception as e:
        logger.error(f"❌ Error saving metadata for image {image_id}: {e}")
        return False
