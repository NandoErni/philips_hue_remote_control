import requests
import config

def getGroups():
    return requests.get(config.getApiEndpoint() + config.GROUPS_DIR)