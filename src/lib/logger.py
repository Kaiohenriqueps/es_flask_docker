"""logger.py"""
import logging
from datetime import datetime
from pytz import timezone, utc
import msgpack
from io import BytesIO


def custom_time(*args):
    utc_dt = utc.localize(datetime.utcnow())
    my_tz = timezone("America/Sao_Paulo")
    converted = utc_dt.astimezone(my_tz)
    return converted.timetuple()


def set_formatter():
    custom_format = {
        "host": "%(hostname)s",
        "where": "%(module)s.%(funcName)s",
        "type": "%(levelname)s",
        "stack_trace": "%(exc_text)s",
        "timestamp": "%(asctime)s"
    }
    formatter = handler.FluentRecordFormatter(custom_format)
    formatter.converter = custom_time
    return formatter


def overflow_handler(pendings):
    unpacker = msgpack.Unpacker(BytesIO(pendings))
    for unpacked in unpacker:
        print(unpacked)


def set_logger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.level = logging.INFO

    fluent_handler = handler.FluentHandler(
        _name_,
        host='a01c3cc0bb49b11eaac330ac2983d850-2059753173.us-east-2.elb.amazonaws.com',
        port=9880,
        buffer_overflow_handler=overflow_handler
    )

    formatter = set_formatter()
    fluent_handler.setFormatter(formatter)

    logger.addHandler(fluent_handler)
    return logger