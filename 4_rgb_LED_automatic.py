import RPi.GPIO as GPIO
import time


def color(list):
    try:
        GPIO.setmode(GPIO.BCM)
        anod = 18
        GPIO.setup(anod, GPIO.OUT)
        red = 4
        GPIO.setup(red, GPIO.OUT) 
        green = 27
        GPIO.setup(green, GPIO.OUT)
        blue = 22
        GPIO.setup(blue, GPIO.OUT)
        
        GPIO.output(anod, GPIO.HIGH)
        printed = False
        #list -> rgb
        if(list[0] == 1):
            GPIO.output(red, GPIO.HIGH)
        else:
            GPIO.output(red, GPIO.LOW)
            print("red ") 
            printed = True
        if(list[1] == 1):
            GPIO.output(green, GPIO.HIGH)
        else:
            GPIO.output(green, GPIO.LOW)
            if(printed):
                print("+")
            printed = True
            print("green")
        if(list[2]==1):
            GPIO.output(blue, GPIO.HIGH)
        else:
            GPIO.output(blue, GPIO.LOW)
            if(printed):
                print("+")
            printed = True
            print("blue")
            
        time.sleep(3)
        print("---")
                    
    finally:
        
        GPIO.output(18, GPIO.LOW)
        GPIO.output(4, GPIO.LOW)
        GPIO.output(27, GPIO.LOW)
        GPIO.output(22, GPIO.LOW)
        GPIO.cleanup()

def main():

    i = 0;
    try:
        while True:
            GPIO.setmode(GPIO.BCM) 
            GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
            listContain = [[0, 0, 0],
                        [0, 0, 1],
                        [0, 1, 0],
                        [0, 1, 1],
                        [1, 0, 0],
                        [1, 0, 1],
                        [1, 1, 0],
                        [1, 1, 1]]
            GPIO.setup(16, GPIO.OUT)
            GPIO.output(16, GPIO.HIGH)
            if GPIO.input(21) == GPIO.HIGH:
                time.sleep(0.2)
                print("next color")
                if(i%8==7):
                    i+=1
                color(listContain[i%8])
                i+=1
    finally:
            GPIO.output(16, GPIO.LOW)
            GPIO.cleanup()
main()
