import logging
import os

# Ensure logs directory exists
LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Log file path
LOG_FILE = os.path.join(LOG_DIR, "app.log")

# Create logger
logger = logging.getLogger("image_processing")
logger.setLevel(logging.INFO)  # Default level (can be changed dynamically)

# Formatter for logs
formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")

# File Handler (Logs to File)
file_handler = logging.FileHandler(LOG_FILE, mode="a")
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.INFO)

# Console Handler (Logs to Console)
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
console_handler.setLevel(logging.INFO)

# Add handlers to logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Function to set debug mode
def enable_debug():
    """
    Enable debug-level logging for more detailed output.
    """
    logger.setLevel(logging.DEBUG)
    file_handler.setLevel(logging.DEBUG)
    console_handler.setLevel(logging.DEBUG)
    logger.debug("🔍 Debug mode enabled: Logging set to DEBUG level.")
