#!libs/bin/python
# pylint: disable=C0103
"""
high level support for doing this and that.
"""

import logging
from logging.handlers import RotatingFileHandler
import ConfigParser
import sys
from flask import Flask

CONFIG = ConfigParser.ConfigParser()
CONFIG.read("siecle.cfg")

try:
    logger = logging.getLogger()
    stream_handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')
    file_handler = RotatingFileHandler('project.log', 'a', 1000000, 1)

    if CONFIG.get('display', 'log_level') == 'debug':
        logger.setLevel(logging.DEBUG)
        file_handler.setLevel(logging.DEBUG)
        stream_handler.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)
        file_handler.setLevel(logging.INFO)
        stream_handler.setLevel(logging.INFO)

    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
    sys.exit(0)

except KeyboardInterrupt:
    logger.info("Interrupt by user")
    sys.exit(1)
