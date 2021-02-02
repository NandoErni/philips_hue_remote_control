import config
import i2cRepository
import requests
import subprocess
import time

display = i2cRepository.I2cRepository()

display.initDisplay()
display.writeText("Starting...")

r = requests.get(config.SAMPLE_URL, timeout=5)
while not r.status_code == 200:
    try:
        r = requests.get(config.SAMPLE_URL, timeout=5)
    except:
        pass

display.writeText("Success!")
subprocess.call(config.DEPLOYMENT_SCRIPT)
