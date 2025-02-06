import psycopg2
from config import DB_CONFIG
from utils.logger import logger

def connect_db():
    """
    Establish a connection to the PostgreSQL database.
    If the connection succeeds, ensure required tables exist.
    """
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        logger.info("✅ Successfully connected to the PostgreSQL database.")
        ensure_tables_exist(conn)
        return conn
    except Exception as e:
        logger.error(f"❌ Failed to connect to PostgreSQL: {e}")
        return None  # Return None instead of crashing

def ensure_tables_exist(conn):
    """
    Ensure the required tables exist in the database.
    If missing, create them.
    """
    try:
        cur = conn.cursor()
        
        # SQL to check if the table exists
        cur.execute("""
            SELECT EXISTS (
                SELECT FROM information_schema.tables 
                WHERE table_name = 'image_metadata'
            );
        """)
        table_exists = cur.fetchone()[0]

        if not table_exists:
            logger.warning("⚠️ Table 'image_metadata' does not exist. Creating it now...")
            cur.execute("""
                CREATE TABLE image_metadata (
                    id SERIAL PRIMARY KEY,
                    image_id TEXT UNIQUE NOT NULL,
                    taken_at TIMESTAMP,
                    latitude FLOAT,
                    longitude FLOAT,
                    caption TEXT,
                    scene TEXT,
                    object TEXT,
                    faces TEXT[],
                    albums TEXT[],
                    location TEXT,
                    processed_at TIMESTAMP DEFAULT NOW()
                );
            """)
            conn.commit()
            logger.info("✅ Table 'image_metadata' successfully created.")
        else:
            logger.info("✅ Table 'image_metadata' already exists.")

        cur.close()
    except Exception as e:
        logger.error(f"❌ Error ensuring database tables exist: {e}")
