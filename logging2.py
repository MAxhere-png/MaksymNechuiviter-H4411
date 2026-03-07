import logging 

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

handler = logging.FileHandler("debug.log")
handler.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

info_handler = logging.FileHandler("info.log")
info_handler.setLevel(logging.INFO)
info_handler.setFormatter(formatter)

logger.addHandler(info_handler)
logger.info("info")

