import board
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

oled_reset = digitalio.DigitalInOut(board.D4)

WIDTH = 128
HEIGHT = 32

i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C, reset=oled_reset)

oled.fill(0)
oled.show()

image = Image.new("1", (oled.width, oled.height))

draw = ImageDraw.Draw(image)

font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 34)

text = "L1"
(font_width, font_height) = font.getsize(text)

draw.text(
    (oled.width/2 - font_width/2, 0),
    text,
    font=font,
    fill=255,
)

oled.image(image)
oled.show()