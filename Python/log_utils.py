import os
import logging

from time import gmtime, strftime
DIRNAME = os.path.join('logs', strftime("%Y-%m-%d_%H.%M.%S", gmtime()))
if not os.path.exists(DIRNAME):
    os.makedirs(DIRNAME)

MAIN_LOGGER_NAME = "root"
main_logger = None

def get_logger(logger_name, is_child_of_root=True):
    # create logger with 'spam_application'
    logger_full_name = MAIN_LOGGER_NAME
    
    if is_child_of_root:
        logger_full_name = logger_full_name + "." + logger_name

    logger = logging.getLogger(logger_full_name)
    logger.setLevel(logging.DEBUG)
    
    if is_child_of_root:
        logger.propagate = True    

    # create file handler which logs even debug messages
    fh = logging.FileHandler(os.path.join(DIRNAME, '%s.log' % (logger_full_name)))
    fh.setLevel(logging.DEBUG)

    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # add the handlers to the logger
    logger.addHandler(fh)
    if is_child_of_root:
        logger.addHandler(ch)

    return logger

def start_root_log():
    global main_logger
    main_logger = get_logger(MAIN_LOGGER_NAME, False)
