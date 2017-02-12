import RPi.GPIO as gpio
import time

LED_PIN = 18

"""
Set the mode (either BOARD or BCM)
See http://www.raspberrypi-spy.co.uk/2012/06/simple-guide-to-the-rpi-gpio-header-and-pins/
for more information.
For now, we will use BCM (its the same for Pi 2/3)
"""
gpio.setmode(gpio.BCM)

# set LED pin as an OUTPUT pin, so we can write to it
gpio.setup(LED_PIN, gpio.OUT)

# create a new PWM on LED_PIN with frequency 50hz
pwm = gpio.PWM(LED_PIN, 50)
# begin PWM with DutyCycle = 1 (100% on)
pwm.start(1)

try:
    # loop forever
    while True:
        for dc in range(0, 101, 5):
            # increase brightness
            pwm.ChangeDutyCycle(dc)
            time.sleep(0.1)

        for dc in range(100, -1, -5):
            # decrease brightness
            pwm.ChangeDutyCycle(dc)
            time.sleep(0.1)
except KeyboardInterrupt:
    pass


# stop our PWM
pwm.stop()
# clean up any GPIO pins we have been using
gpio.cleanup()
