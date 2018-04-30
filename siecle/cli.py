"""This class manage the CLI interaction"""
import json
import logging
import sys
import ConfigParser
from .api import ApiDocker
from crontab import CronTab
from .scheduler import Scheduler

LOGGER = logging.getLogger(__name__)
CONFIG = ConfigParser.ConfigParser()

#pylint: disable=invalid-name
class DockerStage(object): # pylint: disable=too-few-public-methods
    """This class manage CLI interactions"""
    @staticmethod
    def ps(): # pylint: disable=invalid-name
        """List active containers (debug purpose)"""
        api = ApiDocker()
        api.list_containers()

    @staticmethod
    def crontab():
        """
        Parse CronTab
        """
        schd = Scheduler()
        schd.parse_crontab('crontab')


class Cli(object):# pylint: disable=too-few-public-methods
    """CLI class"""
    def __init__(self):
        """CLI constructor"""
        self.docker = DockerStage()
