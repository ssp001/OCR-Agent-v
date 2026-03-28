import logging
import sys


logger = logging.getLogger(__name__)

# formateer congiguration
formatter = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(name)s - %(message)s')
# configuring system workflows
system_handeler = logging.StreamHandler(sys.stdout)
file_handeler = logging.FileHandler('app.log')
# setting up how look like the formater should be
system_handeler.setFormatter(formatter)
file_handeler.setFormatter(formatter)
# add add all handeler to the loggers
logger.addHandler(system_handeler)
logger.addHandler(file_handeler)

# setting the level up
logger.setLevel(logging.DEBUG)
