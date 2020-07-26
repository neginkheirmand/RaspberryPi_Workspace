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
    list=[1,1,1]
    for i in range(2):
        list[0]=i
        for j in range (2):
            list[1]=j
            for k in range(2):
                list[2]=k
                color(list)

main()
