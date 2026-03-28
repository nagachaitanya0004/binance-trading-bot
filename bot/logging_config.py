from loguru import logger
import os

def setup_logger():
    os.makedirs("logs", exist_ok=True)
    logger.add("logs/bot.log", rotation="1 MB", level="INFO")
    return logger