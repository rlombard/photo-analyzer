import psycopg2
from psycopg2 import pool
from config import DB_CONFIG
from utils.logger import logger

# Initialize connection pool
db_pool = None

def init_db_pool():
    global db_pool
    if db_pool is None:
        try:
            db_pool = psycopg2.pool.SimpleConnectionPool(
                minconn=1,
                maxconn=10,  # Adjust max connections as needed
                **DB_CONFIG
            )
            logger.info("✅ Database connection pool initialized.")
        except Exception as e:
            logger.error(f"❌ Failed to initialize database connection pool: {e}")
            raise

def get_connection():
    """ Get a connection from the pool """
    try:
        if db_pool is None:
            init_db_pool()
        return db_pool.getconn()
    except Exception as e:
        logger.error(f"❌ Error getting database connection: {e}")
        return None

def release_connection(conn):
    """ Release a connection back to the pool """
    if conn:
        db_pool.putconn(conn)

def close_pool():
    """ Close all connections in the pool """
    if db_pool:
        db_pool.closeall()
        logger.info("✅ Database connection pool closed.")
