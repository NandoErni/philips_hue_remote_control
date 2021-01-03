import requests
import config
import json

MAX_BRIGHTNESS = 254
MIN_BRIGHTNESS = 1

def getGroups():
    return requests.get(config.getApiEndpoint() + config.GROUPS_DIR)


def setLightsToGroup(group, state):
    return requests.put(config.getGroupActionEndpoint(group), json.dumps({'on': state}))


def setBrightnessToGroup(group, brightness):
    if brightness > MAX_BRIGHTNESS:
        brightness = MAX_BRIGHTNESS

    if brightness < MIN_BRIGHTNESS:
        brightness = MIN_BRIGHTNESS

    return requests.put(config.getGroupActionEndpoint(group), json.dumps({'bri': brightness}))

