"""Cutom loger module for my project ```from utils.logger_module import logger```"""

import logging
import sys


# Inicilize getlogger function for root folder name
logger = logging.getLogger(__name__)
# configure logging output formate
formate_schema = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(name)s - %(message)s")

# === stream handeler system === !
stream_handeler = logging.StreamHandler(sys.stdout)
# === file handeler system === !
file_handeler = logging.FileHandler("app.log")
# === setup the formate for file-handeler === !
file_handeler.setFormatter(formate_schema)
# === setup the formate for strem-handeler === !
stream_handeler.setFormatter(formate_schema)
# logger set handeler
logger.addHandler(stream_handeler)
logger.addHandler(file_handeler)
# set the setlevel for logs
logger.setLevel(logging.DEBUG)
