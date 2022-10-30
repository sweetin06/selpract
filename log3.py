import logging
logging.basicConfig(filename="test.log", format='%(asctime)s: %(levelname)s: %(message)s', level=logging.DEBUG)
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)
#when we printed debug and info is not printed in console
logging.debug("debug msg")
logging.info("info msg")
logging.warning("warning msg")
logging.error("error msg")
logging.critical("critical msg")