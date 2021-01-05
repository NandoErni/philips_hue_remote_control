# to make this work install python3, pip3, requests, RPi.GPIO for python3
import apiRepository
import gpioRepository

gpio = gpioRepository.GPIORepository()

gpio.initGPIO()

while True:
    if gpio.isButtonBrightnessUpFlag():
        apiRepository.dimGroup(1)
