import apiRepository
import gpioRepository
import i2cRepository
import time
import config

print("Remote Control is now starting...")
SYSTEM_LATENCY = 0.1
anyButtonPressed = False

gpio = gpioRepository.GPIORepository()
api = apiRepository.APIRepository()
display = i2cRepository.I2cRepository()

gpio.initGPIO()
display.initDisplay()

display.writeText("Connecting...")

while not api.isHueAvailable():
    display.writeText("Hue is not")
    time.sleep(1)
    display.writeText("available")
    time.sleep(1)
    display.writeText("retrying...")

display.writeText("Hello :)")
time.sleep(2)


def changeReceiver(i):
    global currentReceiverIndex, receivers
    currentReceiverIndex = (currentReceiverIndex + i) % len(receivers)
    print("The current receiver is " + receivers[currentReceiverIndex])
    showCurrentReceiver()


def getCurrentReceiverNumber():
    global currentReceiverIndex, receivers
    return int(receivers[currentReceiverIndex][1])


def isCurrentReceiverLight():
    global receivers
    if len(receivers) <= 0:
        return False

    return receivers[currentReceiverIndex][0] == config.LIGHT_IDENTIFIER


def changeToNextGroup():
    global currentReceiverIndex, receivers
    if isCurrentReceiverLight():
        changeReceiver(1)
        changeToNextGroup()


def showCurrentReceiver():
    display.writeText(receivers[currentReceiverIndex]
                      .replace(config.GROUP_IDENTIFIER, "Group ")
                      .replace(config.LIGHT_IDENTIFIER, "Light "))


receivers = api.getCurrentReceivers()
currentReceiverIndex = 0

changeToNextGroup()
showCurrentReceiver()
while True:
    anyButtonPressed = False
    time.sleep(SYSTEM_LATENCY)

    display.processScreenSaver(SYSTEM_LATENCY)

    if gpio.isButtonBrightnessUpFlag():
        anyButtonPressed = True
        if isCurrentReceiverLight():
            api.dimLightUp(getCurrentReceiverNumber())
        else:
            api.dimGroupUp(getCurrentReceiverNumber())

    if gpio.isButtonBrightnessDownFlag():
        anyButtonPressed = True
        if isCurrentReceiverLight():
            api.dimLightDown(getCurrentReceiverNumber())
        else:
            api.dimGroupDown(getCurrentReceiverNumber())

    if gpio.isButtonToggleOnFlag():
        anyButtonPressed = True
        if isCurrentReceiverLight():
            api.toggleLight(getCurrentReceiverNumber())
        else:
            api.toggleGroup(getCurrentReceiverNumber())

    if gpio.isButtonConnectionFlag():
        anyButtonPressed = True
        display.writeText("Checking...")
        if api.isHueAvailable():
            display.writeText("Success!")
        else:
            display.writeText("Fail!")
        receivers = api.getCurrentReceivers()
        time.sleep(1.5)
        showCurrentReceiver()

    if gpio.isButtonPresetOneFlag():
        anyButtonPressed = True
        if isCurrentReceiverLight():
            changeToNextGroup()
        api.applySceneBright(getCurrentReceiverNumber())

    if gpio.isButtonPresetTwoFlag():
        anyButtonPressed = True
        if isCurrentReceiverLight():
            changeToNextGroup()
        api.applySceneDimmed(getCurrentReceiverNumber())

    if gpio.isButtonPresetThreeFlag():
        anyButtonPressed = True
        if isCurrentReceiverLight():
            changeToNextGroup()
        api.applySceneNightlight(getCurrentReceiverNumber())

    if gpio.isButtonNextFlag():
        anyButtonPressed = True
        changeReceiver(1)

    if gpio.isButtonPreviousFlag():
        anyButtonPressed = True
        changeReceiver(-1)

    if anyButtonPressed:
        display.resetScreenSaver()
        showCurrentReceiver()
