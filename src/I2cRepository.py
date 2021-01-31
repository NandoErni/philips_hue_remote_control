import config
import board
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306


class I2cRepository:
    oled = image = draw = font = None

    def initDisplay(self):
        oled_reset = digitalio.DigitalInOut(board.D4)
        i2c = board.I2C()
        self.oled = adafruit_ssd1306.SSD1306_I2C(config.DISPLAY_WIDTH, config.DISPLAY_HEIGHT, i2c, addr=0x3C,
                                                 reset=oled_reset)

        self.oled.fill(0)
        self.oled.show()

        self.image = Image.new("1", (self.oled.width, self.oled.height))
        self.draw = ImageDraw.Draw(self.image)

        self.font = ImageFont.truetype(config.STANDARD_FONT, config.STANDARD_FONT_SIZE)

    def clear(self):
        self.draw.rectangle((0, 0, 300, 150), fill=0)

    def writeText(self, text):
        (font_width, font_height) = self.font.getsize(text)

        self.draw.text(
            (self.oled.width / 2 - font_width / 2, 0),
            text,
            font=self.font,
            fill=255,
        )

        self.clear()
        self.oled.image(self.image.rotate(180))
        self.oled.show()
