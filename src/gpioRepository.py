import RPi.GPIO as GPIO
import config
import time


class GPIORepository:
    SYSTEM_LATENCY = 0.05
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
        GPIO.setup(config.GPIO_LED_CONNECT, GPIO.OUT)

    def dispose(self):
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
        inputButton = GPIO.input(gpio_button)
        time.sleep(self.SYSTEM_LATENCY)
        if not inputButton:
            if not self.buttonFlags[gpio_button_flag_index]:
                self.buttonFlags[gpio_button_flag_index] = True
                print(outputString)
                return True
            else:
                return False
        self.buttonFlags[gpio_button_flag_index] = False
        return False
