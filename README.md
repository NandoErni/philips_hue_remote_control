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

Download this repository with this command:
```console
pi@raspberry:~$ sudo git clone https://github.com/NandoErni/philips_hue_remote_control.git
```

After you have downloaded the repository, 
you will need to adjust some values in the ```src/config.py```.
Especially the following:
- PHILIPS_HUE_URL   => The IP-Address for the philips hue station
- USERNAME          => The username for using the philips hue api (The long number). Follow the instructions on this site: https://developers.meethue.com/develop/get-started-2/
- SCENE_BRIGHT      => The id of the scene for the first preset button
- SCENE_DIMMED      => The id of the scene for the second preset button
- SCENE_NIGHTLIGHT  => The id of the scene for the third preset button
- STANDARD_FONT     => The path to the font used by the display
- DISPLAY_HEIGHT    => The height of your display
- DEPLOYMENT_SCRIPT => The deployment script (This is only needed, when you're using the ```src/waitForConnection.py``` script)

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
Also note that when you download the repository, 
you have to adjust all the values in the ```src/config.py``` 
again (probably via deployment script).

### GPIO Configuration
The GPIO configuration can be found and adjusted in the ```src/config.py``` file
To make the buttons work, connect them to the GPIO pin and to ground.
Run the following command to check whether your I2C display is connected correctly:
```console
pi@raspberry:~$ i2cdetect -y 1
```