import requests
import config
import json
import time

MAX_BRIGHTNESS = 254
MIN_BRIGHTNESS = 1
DIM_STEP = 10
SYSTEM_LATENCY = 0.05


def getGroups():
    return httpGet(getApiEndpoint() + config.GROUPS_DIR)


def setLightsToGroup(group, state):
    return httpPut(getGroupActionEndpoint(group), {'on': state})


def toggleGroup(group):
    r = httpGet(getGroupActionEndpoint(group))
    return setLightsToGroup(group, r.json()["on"])


def setBrightnessToGroup(group, brightness):
    return httpPut(getGroupActionEndpoint(group), {'bri': getCorrectBrightness(brightness)})


def dimGroup(group):
    print("dimming!")
    r = httpGet(getGroupEndpoint(group))
    brightness = r.json()["action"]["bri"]
    return setBrightnessToGroup(group, brightness - DIM_STEP)


def isHueAvailable():
    r = httpGet(getApiEndpoint())

    if r is not None and r.status_code == 200:
        return True

    return False


def httpPut(url, jsonData):
    try:
        r = requests.put(url, json.dumps(jsonData))
        time.sleep(SYSTEM_LATENCY)
        return r
    except:
        return None


def httpGet(url):
    try:
        r = requests.get(url)
        time.sleep(SYSTEM_LATENCY)
        return r
    except:
        return None


def getApiEndpoint():
    return config.PHILIPS_HUE_URL + 'api/' + config.USERNAME + '/'


def getGroupActionEndpoint(group):
    return getGroupEndpoint(group) + config.GROUP_ACTION_DIR


def getGroupEndpoint(group):
    return getApiEndpoint() + config.GROUPS_DIR + str(group) + '/'


def getLightsEndpoint():
    return getApiEndpoint() + config.LIGHTS_DIR


def getCorrectBrightness(brightness):
    if brightness < MIN_BRIGHTNESS:
        return MIN_BRIGHTNESS

    if brightness > MAX_BRIGHTNESS:
        return MAX_BRIGHTNESS

    return brightness
