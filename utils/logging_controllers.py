import sys
import warnings
import contextlib

import stackprinter
from loguru import logger

showwarning_ = warnings.showwarning


def showwarning(message, *args, **kwargs):
    logger.warning(message)
    showwarning_(message, *args, **kwargs)


warnings.showwarning = showwarning
stackprinter.set_excepthook(style='darkbg2')


# fmt = "{time:MM:DD:HH:mm:ss} | {level:8}| {exception} {file} {module} {name} {function} {line} : {message}"


def fmt(record):
    format_ = "{time} {message}\n"

    if record["exception"] is not None:
        record["extra"]["stack"] = stackprinter.format(record["exception"])
        format_ += "{extra[stack]}\n"

    return fmt


logger.add(sys.stderr, format=fmt)


class Formatter:

    def __init__(self):
        self.padding = 0
        self.fmt = "<b><y><lvl>{time:MM:DD:HH:mm:ss}</lvl></y></b> | " \
                   "<b><lvl><l>{level:<8}</l></lvl></b> | " \
                   "<i><w>{file}</w></i> :<r>{name}</r>: {function}: <c>{line}</c>{extra[padding]} | " \
                   "<lvl>{message}</lvl>\n{exception}"

    def format(self, record):
        length = len("{file}{name}:{function}:{line}".format(**record))
        self.padding = max(self.padding, length)
        record["extra"]["padding"] = " " * (self.padding - length)
        return self.fmt


formatter = Formatter()

logger.remove()
logger.add(sys.stderr, format=formatter.format)
logger.remove()
logger.add("./logs/{time:MM}_{time:DD}.log", format=formatter.format, level="DEBUG", rotation="5 MB")
logger.remove()
logger.add(sys.stdout, format=formatter.format, level="DEBUG")
logger.level("INFO", color="<green><bold>", icon="✅")
logger.level("WARNING", color="<m><bold>")
logger.level("SUCCESS", color="<y><bold>")
logger.level("CRITICAL", color="<bold><bg m>")


# class StreamToLogger:
#
#     def __init__(self, level="INFO"):
#         self._level = level
#
#     def write(self, buffer):
#         for line in buffer.rstrip().splitlines():
#             logger.opt(depth=1).log(self._level, line.rstrip())
#
#     def flush(self):
#         pass
#
#
# logger.remove()
# logger.add(sys.__stdout__)
#
# stream = StreamToLogger()
# with contextlib.redirect_stdout(stream):
#     print("Standard output is sent to added handlers.")

# logger.debug("Logger running...DEBUG")
# logger.info("Logger running...INFO")
# logger.success("Logger running...SUCCESS")
# logger.warning("Logger running...WARNING")
# logger.error("Logger running...ERROR")
# logger.critical("Logger running...CRITICAL")
