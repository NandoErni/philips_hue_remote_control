# philips_hue_remote_control
A script to control philips hue lights on a Raspberry Pi Zero W.

This Script is written in Python 3 for the Raspberry Pi Zero W.

## Getting Started
### Prerequisites
In order to make this work install the following packages: 
- python3
- pip3 
- requests
- RPi.GPIO for python3
- Adafruit_CircuitPython_SSD1306
- Pillow

For easy installation use the installation script ```install_prerequesites.sh```

You also have to enable I2C via 
```console
pi@raspberry:~$ sudo raspi-config
```

### Run the program
To run the program execute:
```console
pi@raspberry:~$ python3 src/main.py
```

However, if you want to execute a script first, 
which needs an internet connection, you can run:
```console
pi@raspberry:~$ python3 src/waitForConnection.py
```

This python script will wait until the raspberry pi has access to the internet
and then it will execute a bash script (which is specified in ```src/config.py```).

This is useful if you want to download the latest version of 
this program and execute it after the download. The advantage of this method is, 
that it displays a text while trying to connect to the internet.

### GPIO Configuration
The GPIO configuration can be found and adjusted in the ```src/config.py``` file
To make the buttons work, connect them to the GPIO pin and to ground.
Run the following command to check whether your I2C display is connected correctly:
```console
pi@raspberry:~$ i2cdetect -y 1
```