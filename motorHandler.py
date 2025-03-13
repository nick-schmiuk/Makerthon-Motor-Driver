import RPi.GPIO as GPIO
from time import sleep

class motor:
    def __init__(self, pwmPin, forwardPin, backwardPin):
        self.forwardPin = forwardPin
        self.backwardPin = backwardPin
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(pwmPin,GPIO.OUT)         # Throttle
        GPIO.setup(forwardPin, GPIO.OUT)    # Forwards Direction
        GPIO.output(forwardPin, GPIO.LOW)
        GPIO.setup(backwardPin, GPIO.OUT)   # Backwards Direction
        GPIO.output(backwardPin, GPIO.LOW)

        self.pwm = GPIO.PWM(pwmPin, 1000)
        self.pwm.start(0)

    def drive(self, speed, direction=0):
        if speed == 0:
            self.pwm.ChangeDutyCycle(0)
            GPIO.output(self.forwardPin, GPIO.LOW)
            GPIO.output(self.backwardPin, GPIO.LOW)
            return

        if direction == 1:
            GPIO.output(self.forwardPin, GPIO.HIGH)
            GPIO.output(self.backwardPin, GPIO.LOW)
            self.pwm.ChangeDutyCycle(speed)
            return
        elif direction == -1:
            GPIO.output(self.forwardPin, GPIO.LOW)
            GPIO.output(self.backwardPin, GPIO.HIGH)
            self.pwm.ChangeDutyCycle(speed)
            return
        
        

