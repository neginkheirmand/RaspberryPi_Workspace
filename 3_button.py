import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM) 
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
try:
    GPIO.setup(16, GPIO.OUT)
    GPIO.output(16, GPIO.HIGH)
    while True: 
        if GPIO.input(21) == GPIO.HIGH:
            print("Button was pushed!")
            time.sleep(0.2)
finally:
        GPIO.output(21, GPIO.LOW)
        GPIO.output(16, GPIO.LOW)
        GPIO.cleanup()
