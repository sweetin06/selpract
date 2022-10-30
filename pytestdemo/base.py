import logging
from _pytest import logging


class Baseclass:
    def getLogger(self):
        logger = logging.FileHandler()
        fileHandler = logging.FileHandler('logfile.log')
        formatter=logging.Formatter("%(asctime)s :%(levelname)s : %(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)
        logger.setLevel(logging.CRITICAL)
        return  logger
