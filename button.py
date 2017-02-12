import RPi.GPIO as gpio
import time
import signal, sys

LED_PIN = 18
BUTTON_PIN = 12

"""
Set the mode (either BOARD or BCM)
See http://www.raspberrypi-spy.co.uk/2012/06/simple-guide-to-the-rpi-gpio-header-and-pins/
for more information.
For now, we will use BCM (its the same for Pi 2/3)
"""
gpio.setmode(gpio.BCM)

# set button pin as an INPUT pin, so we can read from it
gpio.setup(BUTTON_PIN, gpio.IN)
# set LED pin as an OUTPUT pin, so we can write to it
gpio.setup(LED_PIN, gpio.OUT)

try:
    # loop forever
    while True:
        # set the LED state to the state of the button
        gpio.output(LED_PIN, gpio.input(BUTTON_PIN))
except KeyboardInterrupt:
    pass

# clean up any GPIO pins we have been using
gpio.cleanup()
