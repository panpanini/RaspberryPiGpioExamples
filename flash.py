import RPi.GPIO as gpio
import time

LED_PIN = 18
LED_STATE = True

"""
Set the mode (either BOARD or BCM)
See http://www.raspberrypi-spy.co.uk/2012/06/simple-guide-to-the-rpi-gpio-header-and-pins/
for more information.
For now, we will use BCM (its the same for Pi 2/3)
"""
gpio.setmode(gpio.BCM)

# set LED pin as an OUTPUT pin, so we can write to it
gpio.setup(LED_PIN, gpio.OUT)

try:
    # loop forever
    while True:
        # set the LED state. You can use either
        # gpio.HIGH/gpio.LOW, True/False, 1/0
        gpio.output(LED_PIN, LED_STATE)
        # toggle the LED state
        LED_STATE = not LED_STATE
        # wait for 1 second
        time.sleep(1)
except KeyboardInterrupt:
    pass


# clean up any GPIO pins we have been using
gpio.cleanup()
