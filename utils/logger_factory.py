# logger_factory.py
import os
import yaml
import logging
from utils.logger import Logger

_loggers = {}


def create_logger(log_prefix: str = 'app', log_level: str = 'info'):
    # Dictionary to store loggers for different prefixes
    global _loggers
    if not "_loggers" in globals():
        _loggers = {}

    if log_prefix not in _loggers:
        log_level_dict = {
            'CRITICAL': logging.CRITICAL,
            'ERROR': logging.ERROR,
            'WARNING': logging.WARNING,
            'INFO': logging.INFO,
            'DEBUG': logging.DEBUG
        }
        log_level_i = log_level_dict.get(log_level.upper(), logging.INFO)
        _loggers[log_prefix] = Logger(log_name=log_prefix, log_level=log_level_i).get_logger()

    return _loggers[log_prefix]
