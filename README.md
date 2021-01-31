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

### Run the script
```console
pi@raspberry:~$ python3 ./main.py
```

### GPIO Configuration
The GPIO configuration can be found in the ```config.py``` file