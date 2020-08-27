#!/usr/bin/env python

import RPi.GPIO as GPIO
import time


def rotate_feed_arm():
    try:

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        servo_signal_pin = 18
        # Here we are configuring our PIN to OUPUT to send current through it
        GPIO.setup(servo_signal_pin, GPIO.OUT)

        run_time = .25

        PWM_FREQUENCY = 80

        FULL_SPEED_FORWARD_DC = 20
        FULL_SPEED_BACKWARD_DC = 10
        pwm = GPIO.PWM(servo_signal_pin, PWM_FREQUENCY)

        # Start the SERVO moving forward
        pwm.start(FULL_SPEED_FORWARD_DC)
        time.sleep(run_time)

        pwm.ChangeDutyCycle(FULL_SPEED_BACKWARD_DC)
        time.sleep(run_time)

        pwm.start(FULL_SPEED_FORWARD_DC)
        time.sleep(run_time)

        pwm.ChangeDutyCycle(FULL_SPEED_BACKWARD_DC)
        time.sleep(run_time)

        # CleanUp
        pwm.stop()
        time.sleep(0.5)
        GPIO.cleanup()

        result = True
    except:
        result = False

    # Return result
    print('Completed') if result else print("Error")


rotate_feed_arm()





