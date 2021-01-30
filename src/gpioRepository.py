import RPi.GPIO as GPIO
import config


class GPIORepository:
    buttonFlags = [False, False, False, False, False, False, False, False, False]
    buttonToggleOn = buttonBrightnessUp = buttonBrightnessDown = buttonConnection = False

    def initGPIO(self):
        self.dispose()
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(config.GPIO_BUTTON_ON, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(config.GPIO_BUTTON_BRIGHTNESS_UP, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(config.GPIO_BUTTON_BRIGHTNESS_DOWN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(config.GPIO_BUTTON_CONNECTION, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(config.GPIO_BUTTON_PRESET_ONE, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(config.GPIO_BUTTON_PRESET_TWO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(config.GPIO_BUTTON_PRESET_THREE, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(config.GPIO_BUTTON_NEXT, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(config.GPIO_BUTTON_PREVIOUS, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def dispose(self):
        GPIO.cleanup()

    def isButtonBrightnessUpFlag(self):
        if not GPIO.input(config.GPIO_BUTTON_BRIGHTNESS_UP):
            if not self.buttonBrightnessUp:
                self.buttonBrightnessUp = True
                print("Dim Up Button!")
                return True
            else:
                return False
        self.buttonBrightnessUp = False
        return False

    def isButtonBrightnessDownFlag(self):
        if not GPIO.input(config.GPIO_BUTTON_BRIGHTNESS_DOWN):
            if not self.buttonBrightnessDown:
                self.buttonBrightnessDown = True
                print("Dim Down Button!")
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

    def testConnect(self):
        return self.isButtonFlag(config.GPIO_BUTTON_CONNECTION, self.buttonConnection)

    def isButtonFlag(self, gpio_button, gpio_button_flag_index):
        if not GPIO.input(gpio_button):
            if not self.buttonFlags[0]:
                self.buttonFlags[0] = True
                print("Checking connection...")
                return True
            else:
                return False
        self.buttonFlags[0] = False
        return False
