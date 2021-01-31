import RPi.GPIO as GPIO
import config
import time


class GPIORepository:
    buttonFlags = [False, False, False, False, False, False, False, False, False]
    buttonToggleOn = buttonBrightnessUp = buttonBrightnessDown = buttonConnection = False

    def initGPIO(self):
        self.dispose()
        GPIO.setmode(GPIO.BCM)
        self.setupBtn(config.GPIO_BUTTON_ON)
        self.setupBtn(config.GPIO_BUTTON_BRIGHTNESS_UP)
        self.setupBtn(config.GPIO_BUTTON_BRIGHTNESS_DOWN)
        self.setupBtn(config.GPIO_BUTTON_CONNECTION)
        self.setupBtn(config.GPIO_BUTTON_PRESET_ONE)
        self.setupBtn(config.GPIO_BUTTON_PRESET_TWO)
        self.setupBtn(config.GPIO_BUTTON_PRESET_THREE)
        self.setupBtn(config.GPIO_BUTTON_NEXT)
        self.setupBtn(config.GPIO_BUTTON_PREVIOUS)
        GPIO.setup(config.GPIO_LED_CONNECT, GPIO.OUT)

    @staticmethod
    def setupBtn(button):
        GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    @staticmethod
    def dispose():
        GPIO.cleanup()

    def isButtonBrightnessUpFlag(self):
        return self.isButtonFlag(config.GPIO_BUTTON_BRIGHTNESS_UP, 0, "Dim Up Button!")

    def isButtonBrightnessDownFlag(self):
        return self.isButtonFlag(config.GPIO_BUTTON_BRIGHTNESS_DOWN, 1, "Dim Down Button!")

    def isButtonToggleOnFlag(self):
        return self.isButtonFlag(config.GPIO_BUTTON_ON, 2, "Toggle On/Off!")

    def isButtonConnectionFlag(self):
        return self.isButtonFlag(config.GPIO_BUTTON_CONNECTION, 3, "Checking connection...")

    def isButtonPresetOneFlag(self):
        return self.isButtonFlag(config.GPIO_BUTTON_PRESET_ONE, 4, "Preset One!")

    def isButtonPresetTwoFlag(self):
        return self.isButtonFlag(config.GPIO_BUTTON_PRESET_TWO, 5, "Preset Two!")

    def isButtonPresetThreeFlag(self):
        return self.isButtonFlag(config.GPIO_BUTTON_PRESET_THREE, 6, "Preset Three!")

    def isButtonNextFlag(self):
        return self.isButtonFlag(config.GPIO_BUTTON_NEXT, 7, "Next Value...")

    def isButtonPreviousFlag(self):
        return self.isButtonFlag(config.GPIO_BUTTON_PREVIOUS, 8, "Previous Value...")

    def isButtonFlag(self, gpio_button, gpio_button_flag_index, outputString):
        if not GPIO.input(gpio_button):
            if not self.buttonFlags[gpio_button_flag_index]:
                self.buttonFlags[gpio_button_flag_index] = True
                print(outputString)
                time.sleep(0.001)
                return True
            else:
                return False

        self.buttonFlags[gpio_button_flag_index] = False
        return False
