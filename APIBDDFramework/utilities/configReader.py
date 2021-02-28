import configparser

def getConfig():
    config = configparser.ConfigParser()
    config.read('Config/config.ini')
    return config