echo ---------------------------------philips hue remote control---------------------------------
echo Installing all prerequisites!
echo Updating...
sudo apt-get update
sudo apt-get upgrade

echo Installing python3.7...
sudo apt-get install python3.7

echo Installing pip3...
sudo apt-get -y install python3-pip

echo Installing requests...
sudo pip3 install requests

echo Installing RPi.GPIO for python3...
sudo apt install python3-rpi.gpio

echo Installin I2C tools
sudo apt-get install python-smbus i2c-tools git python-pil

echo Installing adafruit I2C...
sudo git clone https://github.com/adafruit/Adafruit_CircuitPython_SSD1306.git ./lib/adafruit/
sudo python3 ./lib/adafruit/setup.py install

echo finished!
echo ---------------------------------philips hue remote control---------------------------------