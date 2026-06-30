from loguru import logger
import sys

logger.remove()

logger.add(
    sys.stdout,
    colorize=True,
    level="INFO"
)