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

    print(gpio.isButtonPresetOneFlag())
    print(gpio.isButtonPresetTwoFlag())
    print(gpio.isButtonPresetThreeFlag())
    print(gpio.isButtonNextFlag())
    print(gpio.isButtonPreviousFlag())
