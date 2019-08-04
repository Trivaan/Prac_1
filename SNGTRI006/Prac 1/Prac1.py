"""
Python Practical Template
Keegan Crankshaw
Readjust this Docstring as follows:
Names: Trivaan Singh
Student Number: SNGTRI006
Prac: 1
Date: 28/07/2019
"""


# import Relevant Librares
import RPi.GPIO as GPIO
import time
import itertools

GPIO.setmode(GPIO.BCM) #refer to GPIO pins with BCM numbering/configuration

LED_config = [18,23,24]  # setting GPIO pins on pi for LEDS
SW1 = 17                 # setting GPIO pins on pi for switch 1
SW2 = 27                 # setting GPIO pins on pi for switch 2
count = 0                 # setting variable to track binary number 
i=list(itertools.product([0,1], repeat=3))   # creating binary map of numbers from 0 to 7

GPIO.setup(18, GPIO.OUT)               # setting mode for LEDs as output
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(SW1, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # setting mode for switches to inputs and setting it as pull up, therefore TRUE means the push button is up therefore switch is off.
GPIO.setup(SW2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.output(18, GPIO.HIGH)             # setting the LEDs to off when programme is ran
GPIO.output(23, GPIO.HIGH)
GPIO.output(24, GPIO.HIGH)


def main():
    print(i)             # printing output to see if it is outputing on LEDs correctly
    while True:
        time.sleep(1)    # waits for the current thread for 1 seconds
        GPIO.add_event_detect(SW2, GPIO.FALLING, callback=my_callback_one, bouncetime = 250)  # add rising edge detection on a channel, ignoring further edges for 250ms for switch bounce handling
        GPIO.add_event_detect(SW1, GPIO.FALLING, callback=my_callback_two, bouncetime = 250)


def my_callback_one(channel): # switching function for increasing number
    global count
    if count == 7:       # if statement allows the loop from 7 back to 0
        count=0
    else:
        count += 1       # increment count by 1 each time
    GPIO.output(LED_config, i[count])     # displays binary number on LEDs

def my_callback_two(channel):
    global count
    if count == 0:       # if statement allows the loop from 0 back to 7
        count=7
    else:
        count -= 1       # decrement count by 1 each time
    GPIO.output(LED_config, i[count])



# Only run the functions if
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("Exiting gracefully")   # turns off LEDs if a keyboard interupt occurs
        GPIO.output(18, GPIO.HIGH)
        GPIO.output(23, GPIO.HIGH)
        GPIO.output(24, GPIO.HIGH)
        # Turn off your GPIOs here
        GPIO.cleanup()
    except Exception as e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)