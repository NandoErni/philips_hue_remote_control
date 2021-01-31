import requests
import config
import json
import time


class APIRepository:
    MAX_BRIGHTNESS = 254
    MIN_BRIGHTNESS = 1
    SYSTEM_LATENCY = 0.05

    def setOnStateToGroup(self, group, state):
        return self.httpPut(self.getGroupActionEndpoint(group), {'on': state})

    def toggleGroup(self, group):
        r = self.httpGet(self.getGroupEndpoint(group))
        state = not r.json()["action"]["on"]
        return self.setOnStateToGroup(group, state)

    def setBrightnessToGroup(self, group, brightness):
        return self.httpPut(self.getGroupActionEndpoint(group),
                            {'bri': self.getCorrectBrightness(brightness), 'on': True})

    def dimGroupDown(self, group):
        print("dimming down!")
        r = self.httpGet(self.getGroupEndpoint(group))
        brightness = r.json()["action"]["bri"]

        if brightness == self.MIN_BRIGHTNESS:
            return None

        return self.setBrightnessToGroup(group, brightness - config.DIM_STEP)

    def dimGroupUp(self, group):
        print("dimming up!")
        r = self.httpGet(self.getGroupEndpoint(group))
        brightness = r.json()["action"]["bri"]

        if brightness == self.MAX_BRIGHTNESS:
            return None

        return self.setBrightnessToGroup(group, brightness + config.DIM_STEP)

    def isHueAvailable(self):
        r = self.httpGet(self.getApiEndpoint())

        if r is not None and r.status_code == 200:
            print("Hue is available!")
            return True

        print("Hue is not available!")
        return False

    def applySceneBright(self, group):
        return self.httpPut(self.getGroupActionEndpoint(group), {'scene': config.SCENE_BRIGHT})

    def applySceneDimmed(self, group):
        return self.httpPut(self.getGroupActionEndpoint(group), {'scene': config.SCENE_DIMMED})

    def applySceneNightlight(self, group):
        return self.httpPut(self.getGroupActionEndpoint(group), {'scene': config.SCENE_NIGHTLIGHT})

    def getCurrentReceivers(self):
        responseLights = self.httpGet(self.getLightsEndpoint())
        responseGroups = self.httpGet(self.getGroups())
        receivers = []

        for i in range(len(responseLights.json())):
            receivers.append("l" + str(i))

        for i in range(len(responseGroups.json())):
            receivers.append("g" + str(i))

        print("All receivers:")
        for rec in receivers:
            print(rec)

        return receivers

    def httpPut(self, url, jsonData):
        try:
            r = requests.put(url, json.dumps(jsonData))
            time.sleep(self.SYSTEM_LATENCY)
            return r
        except:
            return None

    def httpGet(self, url):
        try:
            r = requests.get(url)
            time.sleep(self.SYSTEM_LATENCY)
            return r
        except:
            return None

    def getApiEndpoint(self):
        return config.PHILIPS_HUE_URL + 'api/' + config.USERNAME + '/'

    def getGroupActionEndpoint(self, group):
        return self.getGroupEndpoint(group) + config.GROUP_ACTION_DIR

    def getGroupEndpoint(self, group):
        return self.getApiEndpoint() + config.GROUPS_DIR + str(group) + '/'

    def getLightsEndpoint(self):
        return self.getApiEndpoint() + config.LIGHTS_DIR

    def getGroups(self):
        return self.httpGet(self.getApiEndpoint() + config.GROUPS_DIR)

    def getCorrectBrightness(self, brightness):
        if brightness < self.MIN_BRIGHTNESS:
            return self.MIN_BRIGHTNESS

        if brightness > self.MAX_BRIGHTNESS:
            return self.MAX_BRIGHTNESS

        return brightness
