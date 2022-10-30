import logging

logger = logging.getLogger(_name_)
fileHandler = logging.FileHandler('logfile.log') # log file
# a error message format
logger.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)")
logger.addHandler(fileHandler)
logger.setLevel(logging.CRITICAL)

logger.setLevel(logging.INFO)
#a level of logs
logger.debug("statement of debug")
logger.info("statement of info")
logger.warning("statement of warning")

