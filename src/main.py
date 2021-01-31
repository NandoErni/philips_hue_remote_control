import apiRepository
import gpioRepository

gpio = gpioRepository.GPIORepository()
api = apiRepository.APIRepository()

gpio.initGPIO()
api.isHueAvailable()


def setReceiver(receiver):
    global currentReceiver, isCurrentReceiverLight
    currentReceiver = int(receiver[1])
    isCurrentReceiverLight = receiver[0] == "l"


receivers = api.getCurrentReceivers()
currentReceiver = 0
isCurrentReceiverLight = True

#setReceiver(receivers[0])

while True:
    if gpio.isButtonBrightnessUpFlag():
        api.dimGroupUp(currentReceiver)

    if gpio.isButtonBrightnessDownFlag():
        api.dimGroupDown(currentReceiver)

    if gpio.isButtonToggleOnFlag():
        api.toggleGroup(currentReceiver)

    if gpio.isButtonConnectionFlag():
        api.isHueAvailable()
        api.getCurrentReceivers()

    if gpio.isButtonPresetOneFlag():
        api.applySceneBright(currentReceiver)

    if gpio.isButtonPresetTwoFlag():
        api.applySceneDimmed(currentReceiver)

    if gpio.isButtonPresetThreeFlag():
        api.applySceneNightlight(currentReceiver)

    if gpio.isButtonNextFlag():
        continue

    if gpio.isButtonPreviousFlag():
        continue
