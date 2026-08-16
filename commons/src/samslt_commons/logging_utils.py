import logging

def get_logger(name="samslt"):
    logging.basicConfig(level=logging.INFO)
    return logging.getLogger(name)
