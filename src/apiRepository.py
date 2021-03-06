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

    def setOnStateToLight(self, light, state):
        return self.httpPut(self.getLightStateEndpoint(light), {'on': state})

    def toggleGroup(self, group):
        r = self.httpGet(self.getGroupEndpoint(group))
        if r is None or not r.ok:
            return None

        state = not r.json()["action"]["on"]
        return self.setOnStateToGroup(group, state)

    def toggleLight(self, light):
        r = self.httpGet(self.getLightEndpoint(light))
        if r is None or not r.ok:
            return None

        state = not r.json()["state"]["on"]
        return self.setOnStateToLight(light, state)

    def setBrightnessToGroup(self, group, brightness):
        return self.httpPut(self.getGroupActionEndpoint(group),
                            {'bri': self.getCorrectBrightness(brightness), 'on': True})

    def dimGroupDown(self, group):
        print("dimming down!")
        r = self.httpGet(self.getGroupEndpoint(group))
        if r is None or not r.ok:
            return None

        brightness = r.json()["action"]["bri"]

        if brightness == self.MIN_BRIGHTNESS:
            return None

        return self.setBrightnessToGroup(group, brightness - config.DIM_STEP)

    def dimGroupUp(self, group):
        print("dimming up!")
        r = self.httpGet(self.getGroupEndpoint(group))
        if r is None or not r.ok:
            return None

        brightness = r.json()["action"]["bri"]

        if brightness == self.MAX_BRIGHTNESS:
            return None

        return self.setBrightnessToGroup(group, brightness + config.DIM_STEP)

    def setBrightnessToLight(self, light, brightness):
        return self.httpPut(self.getLightStateEndpoint(light),
                            {'bri': self.getCorrectBrightness(brightness), 'on': True})

    def dimLightDown(self, light):
        print("dimming down!")
        r = self.httpGet(self.getLightEndpoint(light))
        if r is None or not r.ok:
            return None

        brightness = r.json()["state"]["bri"]

        if brightness == self.MIN_BRIGHTNESS:
            return None

        return self.setBrightnessToLight(light, brightness - config.DIM_STEP)

    def dimLightUp(self, light):
        print("dimming up!")
        r = self.httpGet(self.getLightEndpoint(light))
        if r is None or not r.ok:
            return None

        brightness = r.json()["state"]["bri"]

        if brightness == self.MAX_BRIGHTNESS:
            return None

        return self.setBrightnessToLight(light, brightness + config.DIM_STEP)

    def isHueAvailable(self):
        r = self.httpGet(self.getApiEndpoint())

        if r is not None and r.ok:
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
        rLights = self.httpGet(self.getLightsEndpoint())
        rGroups = self.httpGet(self.getGroupsEndpoint())
        receivers = []

        if rLights is not None and rLights.ok:
            for i in range(len(rLights.json())):
                receivers.append(config.LIGHT_IDENTIFIER + str(i+1))

        if rGroups is not None and rGroups.ok:
            for i in range(len(rGroups.json())):
                receivers.append(config.GROUP_IDENTIFIER + str(i+1))

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

    @staticmethod
    def getApiEndpoint():
        return config.PHILIPS_HUE_URL + 'api/' + config.USERNAME + '/'

    def getGroupActionEndpoint(self, group):
        return self.getGroupEndpoint(group) + config.GROUP_ACTION_DIR

    def getGroupEndpoint(self, group):
        return self.getApiEndpoint() + config.GROUPS_DIR + str(group) + '/'

    def getGroupsEndpoint(self):
        return self.getApiEndpoint() + config.GROUPS_DIR

    def getLightStateEndpoint(self, light):
        return self.getLightEndpoint(light) + config.LIGHT_STATE_DIR

    def getLightEndpoint(self, light):
        return self.getApiEndpoint() + config.LIGHTS_DIR + str(light) + '/'

    def getLightsEndpoint(self):
        return self.getApiEndpoint() + config.LIGHTS_DIR

    def getCorrectBrightness(self, brightness):
        if brightness < self.MIN_BRIGHTNESS:
            return self.MIN_BRIGHTNESS

        if brightness > self.MAX_BRIGHTNESS:
            return self.MAX_BRIGHTNESS

        return brightness
