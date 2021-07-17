import configparser
import os

config = configparser.ConfigParser()
config.read(os.path.join(os.path.join(os.path.dirname(__file__), "..", "Configurations/", "config.ini")))


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common_info', 'baseURL')
        return url

    @staticmethod
    def getUseremail():
        username = config.get('common_info', 'user_email')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common_info', 'password')
        return password
