import logging
import os

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.propagate = True  # important

    if not logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )

        os.makedirs("logs", exist_ok=True)
        file_handler = logging.FileHandler("logs/test_execution.log")
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    return logger
