import apiRepository
import gpioRepository

gpio = gpioRepository.GPIORepository()

gpio.initGPIO()

currentGroup = 1

apiRepository.isHueAvailable()

while True:
    if gpio.isButtonBrightnessUpFlag():
        apiRepository.dimGroupUp(currentGroup)

    if gpio.isButtonBrightnessDownFlag():
        apiRepository.dimGroupDown(currentGroup)

    if gpio.isButtonToggleOnFlag():
        apiRepository.toggleGroup(currentGroup)

    if gpio.isButtonConnectionFlag():
        apiRepository.isHueAvailable()

    if gpio.isButtonPresetOneFlag():
        apiRepository.applySceneBright(currentGroup)

    if gpio.isButtonPresetTwoFlag():
        apiRepository.applySceneDimmed(currentGroup)

    if gpio.isButtonPresetThreeFlag():
        apiRepository.applySceneNightlight(currentGroup)

    if gpio.isButtonNextFlag():
        continue

    if gpio.isButtonPreviousFlag():
        continue
