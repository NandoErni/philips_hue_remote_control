import RPi.GPIO as GPIO
import config


class GPIORepository:
    buttonOnFlag = buttonBrightnessUp = False

    def initGPIO(self):
        self.dispose()
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(config.GPIO_BUTTON_ON, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(config.GPIO_BUTTON_BRIGHTNESS_UP, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def dispose(self):
        GPIO.cleanup()

    def isButtonOnFlag(self):
        if GPIO.input(config.GPIO_BUTTON_ON) and not self.buttonOnFlag:
            self.buttonOnFlag = True
            return True

        return False

    def isButtonBrightnessUpFlag(self):
        if not GPIO.input(config.GPIO_BUTTON_BRIGHTNESS_UP):
            self.buttonBrightnessUp = True
            print("dim button press!")
            return True

        return False
