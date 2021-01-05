import RPi.GPIO as GPIO
import config


class GPIORepository:
    buttonToggleOn = buttonBrightnessUp = buttonBrightnessDown = buttonConnection = False

    def initGPIO(self):
        self.dispose()
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(config.GPIO_BUTTON_ON, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(config.GPIO_BUTTON_BRIGHTNESS_UP, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(config.GPIO_BUTTON_BRIGHTNESS_DOWN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(config.GPIO_BUTTON_CONNECTION, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def dispose(self):
        GPIO.cleanup()

    def isButtonBrightnessUpFlag(self):
        if not GPIO.input(config.GPIO_BUTTON_BRIGHTNESS_UP):
            if not self.buttonBrightnessUp:
                self.buttonBrightnessUp = True
                print("Dim Button Up!")
                return True
            else:
                return False
        self.buttonBrightnessUp = False
        return False

    def isButtonBrightnessDownFlag(self):
        if not GPIO.input(config.GPIO_BUTTON_BRIGHTNESS_DOWN):
            if not self.buttonBrightnessDown:
                self.buttonBrightnessDown = True
                print("Dim Button Down!")
                return True
            else:
                return False
        self.buttonBrightnessDown = False
        return False

    def isButtonToggleOnFlag(self):
        if not GPIO.input(config.GPIO_BUTTON_ON):
            if not self.buttonToggleOn:
                self.buttonToggleOn = True
                print("Toggle On/Off!")
                return True
            else:
                return False
        self.buttonToggleOn = False
        return False

    def isButtonConnectionFlag(self):
        if not GPIO.input(config.GPIO_BUTTON_CONNECTION):
            if not self.buttonConnection:
                self.buttonConnection = True
                print("Checking connection...")
                return True
            else:
                return False
        self.buttonConnection = False
        return False
