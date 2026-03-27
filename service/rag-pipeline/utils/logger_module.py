import logging
import sys


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# configuring system workflows
system_handeler = logging.StreamHandler(sys.stdout)
file_handeler = logging.FileHandler('app.log')

# formateer congiguration
formatter = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(name)s - %(message)s')
# add levels to handelers
system_handeler.setLevel(logging.DEBUG)
file_handeler.setLevel(logging.DEBUG)
# setting up how look like the formater should be
system_handeler.setFormatter(formatter)
file_handeler.setFormatter(formatter)

logger.addHandler(system_handeler)
logger.addHandler(file_handeler)

# setting the level up
