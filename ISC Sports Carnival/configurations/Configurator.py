import os
from configparser import ConfigParser

from utils.custom_logger.CustomLogger import CustomLogger


class Configurator:
    def __init__(self):
        self.__logger = CustomLogger()

    @staticmethod
    def __get_file_path():
        return "C:\\Users\\mohit.sadhwani\\PycharmProjects\\LearnAndCodeAssignment\\WorkshopProject\\configurations" \
               "\\configurations.ini"

    def load_configurations(self):
        self.__logger.info("Loaded Configuration File")
        config = ConfigParser()
        config.read(self.__get_file_path())
        config_data = config["DEFAULT"]
        return config_data
