# to make this work install python3, pip3, requests, RPi.GPIO for python3
import apiRepository
import gpioRepository

gpio = gpioRepository.GPIORepository()

gpio.initGPIO()

currentGroup = 1

while True:
    if gpio.isButtonBrightnessUpFlag():
        apiRepository.dimGroupUp(currentGroup)

    if gpio.isButtonBrightnessDownFlag():
        apiRepository.dimGroupDown(currentGroup)

    if gpio.isButtonToggleOnFlag():
        apiRepository.toggleGroup(currentGroup)

    if gpio.isButtonConnectionFlag():
        apiRepository.isHueAvailable()

    gpio.isButtonPresetOneFlag()
    gpio.isButtonPresetTwoFlag()
    gpio.isButtonPresetThreeFlag()
    gpio.isButtonNextFlag()
    gpio.isButtonPreviousFlag()
