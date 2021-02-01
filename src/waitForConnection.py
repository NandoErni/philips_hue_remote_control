import config
import i2cRepository
import requests
import subprocess

display = i2cRepository.I2cRepository()

display.initDisplay()
display.writeText("Starting...")

r = requests.get(config.SAMPLE_URL)
while not r.status_code == 200:
    try:
        r = requests.get(config.SAMPLE_URL)
    except:
        pass

subprocess.call(config.DEPLOYMENT_SCRIPT)
