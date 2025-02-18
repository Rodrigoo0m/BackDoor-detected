import logging

def setup_logger():
    """Setup logger for the tool."""
    logger = logging.getLogger('BackdoorDetector')
    logger.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger

logger = setup_logger()

def log_detection(message):
    """Log a detection to the console and a file."""
    logger.info(message)
