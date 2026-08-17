import logging

logging.basicConfig(
    format='%(asctime)s | %(levelname)-8s | %(name)-8s | %(message)s' ,
    level=logging.DEBUG,
    filename='logs.txt'
)

def get_logger(name):
    return logging.getLogger(name)