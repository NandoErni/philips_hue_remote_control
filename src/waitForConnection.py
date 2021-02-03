import i2cRepository

display = i2cRepository.I2cRepository()

display.initDisplay()
display.writeText("Starting...")
