import logging
import time
import datetime

logging.Formatter.converter = time.gmtime  # Use UTC time


def configure_logging(logger_name='simplevideocutter',
                      log_level=logging.WARNING):
    logger = logging.getLogger(logger_name)
    cout = logging.StreamHandler()
    if log_level == logging.DEBUG:
        # Additional logging information when in debug mode.
        fmt = '%(asctime)s - [%(levelname)-7s] %(module)s:%(funcName)s - ' \
              '%(message)s'
    else:
        fmt = '%(asctime)s - [%(levelname)s] %(message)s'
    formatter = logging.Formatter(fmt=fmt, datefmt='%y%m%dZ%H%M%S')
    cout.setFormatter(formatter)
    logger.setLevel(log_level)
    cout.setLevel(log_level)
    logger.addHandler(cout)


def datetime_to_seconds(dt: datetime.datetime) -> int:
    """
    Returns the number of seconds in the given date time.

    Only uses the hour, minute, second values.
    """
    return dt.hour * 60 * 60 + dt.minute * 60 + dt.second
