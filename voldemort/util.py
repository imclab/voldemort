#! /usr/bin/env python
#
# Common utility functions
#
# @author: Sreejith K
# Created On 19th Sep 2011


import logging
import logging.handlers


def setup_logging(path, level):
    """Setup application logging.
    """
    log_handler = logging.handlers.RotatingFileHandler(path,
                                                      maxBytes=1024*1024,
                                                      backupCount=2)
    root_logger = logging.getLogger('')
    root_logger.setLevel(level)
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(format)
    log_handler.setFormatter(formatter)
    root_logger.addHandler(log_handler)