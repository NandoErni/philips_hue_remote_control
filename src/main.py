import apiRepository
import gpioRepository

gpio = gpioRepository.GPIORepository()
api = apiRepository.APIRepository()

gpio.initGPIO()
api.isHueAvailable()


def changeReceiver(i):
    global currentReceiverIndex, receivers
    currentReceiverIndex = (currentReceiverIndex + i) % len(receivers)
    print("The current receiver is " + receivers[currentReceiverIndex])


def getCurrentReceiverNumber():
    global currentReceiverIndex, receivers
    return int(receivers[currentReceiverIndex])


def isCurrentReceiverLight():
    global receivers
    return receivers[currentReceiverIndex][0] == "l"


receivers = api.getCurrentReceivers()
currentReceiverIndex = 0

while True:
    if gpio.isButtonBrightnessUpFlag():
        api.dimGroupUp(getCurrentReceiverNumber())

    if gpio.isButtonBrightnessDownFlag():
        api.dimGroupDown(getCurrentReceiverNumber())

    if gpio.isButtonToggleOnFlag():
        if isCurrentReceiverLight():
            api.toggleLight(getCurrentReceiverNumber())
        else:
            api.toggleGroup(getCurrentReceiverNumber())

    if gpio.isButtonConnectionFlag():
        api.isHueAvailable()
        api.getCurrentReceivers()

    if gpio.isButtonPresetOneFlag():
        api.applySceneBright(getCurrentReceiverNumber())

    if gpio.isButtonPresetTwoFlag():
        api.applySceneDimmed(getCurrentReceiverNumber())

    if gpio.isButtonPresetThreeFlag():
        api.applySceneNightlight(getCurrentReceiverNumber())

    if gpio.isButtonNextFlag():
        changeReceiver(1)

    if gpio.isButtonPreviousFlag():
        changeReceiver(-1)
