# to make this work install python3, pip3, requests, RPi.GPIO for python3
import apiRepository
import RPi.GPIO as GPIO
import time

button = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

state = False
flagging = False
while True:
    buttonPress = GPIO.input(button)

    if buttonPress and not flagging:
        state = not state
        apiRepository.setLightsToGroup(1,state)

    flagging = buttonPress

print(apiRepository.isHueAvailable())
print('done!')