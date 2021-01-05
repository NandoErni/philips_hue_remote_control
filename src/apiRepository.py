import requests
from src import config
import json

MAX_BRIGHTNESS = 254
MIN_BRIGHTNESS = 1
DIM_STEP = 10


def getGroups():
    return httpGet(getApiEndpoint() + config.GROUPS_DIR)


def setLightsToGroup(group, state):
    return httpPut(getGroupActionEndpoint(group), {'on': state})


def toggleGroup(group):
    r = httpGet(getGroupActionEndpoint(group))
    return setLightsToGroup(group, r.json()["on"])


def setBrightnessToGroup(group, brightness):
    if brightness > MAX_BRIGHTNESS:
        brightness = MAX_BRIGHTNESS

    if brightness < MIN_BRIGHTNESS:
        brightness = MIN_BRIGHTNESS

    return httpPut(getGroupActionEndpoint(group), {'bri': brightness})


def dimGroup(group):
    r = httpGet(getGroupActionEndpoint(group))
    brightness = r.json()["bri"]
    return httpPut(getGroupActionEndpoint(group), {'bri': brightness-DIM_STEP})


def isHueAvailable():
    r = httpGet(getApiEndpoint())

    if r is not None and r.status_code == 200:
        return True

    return False


def httpPut(url, jsonData):
    try:
        return requests.put(url, json.dumps(jsonData))
    except:
        return None


def httpGet(url):
    try:
        return requests.get(url)
    except:
        return None


def getApiEndpoint():
    return config.PHILIPS_HUE_URL + 'api/' + config.USERNAME + '/'


def getGroupActionEndpoint(group):
    return getApiEndpoint() + config.GROUPS_DIR + str(group) + '/' + config.GROUP_ACTION_DIR


def getLightsEndpoint():
    return getApiEndpoint() + config.LIGHTS_DIR
