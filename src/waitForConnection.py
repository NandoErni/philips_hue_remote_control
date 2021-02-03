import config
import i2cRepository
import requests
import subprocess

display = i2cRepository.I2cRepository()

display.initDisplay()
display.writeText("Starting...")


def waitUntilSuccess():
    while True:
        try:
            r = requests.get(config.SAMPLE_URL, timeout=3)
            if r.status_code == 200:
                return
        except:
            pass


waitUntilSuccess()
display.writeText("Updating")
subprocess.Popen("sudo /bin/sh " + config.DEPLOYMENT_SCRIPT)
