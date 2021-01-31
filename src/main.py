import apiRepository
import gpioRepository
import I2cRepository
import time

print("Remote Control is now starting...")
SYSTEM_LATENCY = 0.1
gpio = gpioRepository.GPIORepository()
api = apiRepository.APIRepository()
display = I2cRepository.I2cRepository()

gpio.initGPIO()
api.isHueAvailable()
display.initDisplay()

display.writeText("Hello :)")
time.sleep(3)

def changeReceiver(i):
    global currentReceiverIndex, receivers
    currentReceiverIndex = (currentReceiverIndex + i) % len(receivers)
    print("The current receiver is " + receivers[currentReceiverIndex])


def getCurrentReceiverNumber():
    global currentReceiverIndex, receivers
    return int(receivers[currentReceiverIndex][1])


def isCurrentReceiverLight():
    global receivers
    return receivers[currentReceiverIndex][0] == "l"


def changeToNextGroup():
    global currentReceiverIndex, receivers
    if isCurrentReceiverLight():
        changeReceiver(1)
        changeToNextGroup()


receivers = api.getCurrentReceivers()
currentReceiverIndex = 0

changeToNextGroup()

while True:
    time.sleep(SYSTEM_LATENCY)
    if gpio.isButtonBrightnessUpFlag():
        if isCurrentReceiverLight():
            api.dimLightUp(getCurrentReceiverNumber())
        else:
            api.dimGroupUp(getCurrentReceiverNumber())

    if gpio.isButtonBrightnessDownFlag():
        if isCurrentReceiverLight():
            api.dimLightDown(getCurrentReceiverNumber())
        else:
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
        if isCurrentReceiverLight():
            changeToNextGroup()
        api.applySceneBright(getCurrentReceiverNumber())

    if gpio.isButtonPresetTwoFlag():
        if isCurrentReceiverLight():
            changeToNextGroup()
        api.applySceneDimmed(getCurrentReceiverNumber())

    if gpio.isButtonPresetThreeFlag():
        if isCurrentReceiverLight():
            changeToNextGroup()
        api.applySceneNightlight(getCurrentReceiverNumber())

    if gpio.isButtonNextFlag():
        changeReceiver(1)

    if gpio.isButtonPreviousFlag():
        changeReceiver(-1)
