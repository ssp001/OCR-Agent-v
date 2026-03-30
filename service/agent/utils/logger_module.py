import logging
import sys

logger = logging.getLogger(__name__)


formate = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(name)s - %(message)s')

system_handeler = logging.StreamHandler(sys.stdout)
file_handeler = logging.FileHandler("app.log")

system_handeler.setFormatter(formate)
file_handeler.setFormatter(formate)

logger.addHandler(system_handeler)
logger.addHandler(file_handeler)

logger.setLevel(logging.DEBUG)
