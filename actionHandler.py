from time import sleep

from garbageDetector import detectGarbage

class MainHandler:
    def __init__(self, motorL, motorR, distance):
        self.motorL = motorL
        self.motorR = motorR
        self.distance = distance

    def right(self):
        self.motorR.drive(100, 1)
        #self.motorL.drive(50, -1)

    def left(self):
        self.motorL.drive(100, 1)
        #self.motorR.drive(50, -1)

    def driveAndAvoid(self, forwardspeed,picam2):
        while True:

            value = detectGarbage(picam2)
            if value != 0:
                self.collectGarbage(value,picam2,forwardspeed)
    
            self.motorL.drive(forwardspeed, -1)
            self.motorR.drive(forwardspeed, -1)
            if self.distance.getAvoidance(0, 0.7) == True: # Left channel
                print("Detected Obstacle on the Left")
                self.motorL.drive(0)
                self.motorR.drive(0)
                self.motorL.drive(100, -1)
                self.motorR.drive(30, 1)
                while self.distance.getAvoidance(0, 0.7) == True:
                    sleep(0.3)
                self.motorL.drive(0)
                self.motorR.drive(0)
                self.motorL.drive(forwardspeed, -1)
                self.motorR.drive(forwardspeed, -1)
            
            if self.distance.getAvoidance(1, 0.7) == True: # Right channel
                print("Detected Obstacle on the Left")
                self.motorL.drive(0)
                self.motorR.drive(0)
                self.motorL.drive(30, 1)
                self.motorR.drive(100, -1)
                while self.distance.getAvoidance(1, 0.7) == True:
                    sleep(0.3)
                self.motorL.drive(0)
                self.motorR.drive(0)
                self.motorL.drive(forwardspeed, -1)
                self.motorR.drive(forwardspeed, -1)
        

    def aimAtDetected(self, coordinates,forwardspeed): # 640 x 480
        if coordinates[0][0] >= 340:
            self.motorL.drive(100, -1)
            self.motorR.drive(30, 1)
        elif coordinates[0][0] <= 300:
            self.motorL.drive(30, 1)
            self.motorR.drive(100, -1)
        else:
            self.motorL.drive(forwardspeed, -1)
            self.motorR.drive(forwardspeed, -1)


    def collectGarbage(self,value,picam2,forwardspeed):

        #self.motorL.drive(0)
        #self.motorR.drive(0)

        while True:
            if value == 1:
                print("DETECT - GOING RIGHT")
                #self.motorL.drive(0)
                #self.motorR.drive(0)
                self.motorL.drive(70, -1)
                self.motorR.drive(20, 1)
                value = detectGarbage(picam2)
                continue
            if value == -1:
                print("DETECT - GOING LEFT")
                #self.motorL.drive(0)
                #self.motorR.drive(0)
                self.motorL.drive(20, 1)
                self.motorR.drive(70, -1)
                value = detectGarbage(picam2)
                continue
            if value == 0:
                print("DETECT - GOING STRAIGHT")
                self.motorL.drive(forwardspeed, -1)
                self.motorR.drive(forwardspeed, -1)
                return

