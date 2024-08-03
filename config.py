import logging

logger = logging.getLogger(__name__)

file_handler = logging.FileHandler("output.log", mode="a", encoding="utf-8")
formatter = logging.Formatter(
    "{asctime}: {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M",
)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)