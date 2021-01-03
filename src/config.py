PHILIPS_HUE_URL = 'http://192.168.1.128/'
USERNAME = 'Sbt85oMJRFH7ZO0v5WEhNxqi2xF7A7jhcnjLvxZ2'
GROUPS_DIR = 'groups/'
GROUP_ACTION_DIR = 'action/'
LIGHTS_DIR = 'lights/'


def getApiEndpoint():
    return PHILIPS_HUE_URL + 'api/' + USERNAME + '/'


def getGroupActionEndpoint(group):
    return getApiEndpoint() + GROUPS_DIR + str(group) + '/' + GROUP_ACTION_DIR


def getLightsEndpoint():
    return getApiEndpoint() + LIGHTS_DIR