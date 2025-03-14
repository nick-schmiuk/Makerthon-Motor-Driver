from time import sleep

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

    def driveAndAvoid(self, forwardspeed):
        while True:
            self.motorL.drive(forwardspeed, -1)
            self.motorR.drive(forwardspeed, -1)
            if self.distance.getAvoidance(0, 1.5) == True: # Left channel
                print("Detected Obstacle on the Left")
                self.motorL.drive(0)
                self.motorR.drive(0)
                self.motorL.drive(100, -1)
                self.motorR.drive(30, 1)
                while self.distance.getAvoidance(0, 1.5) == True:
                    sleep(0.3)
                self.motorL.drive(0)
                self.motorR.drive(0)
                self.motorL.drive(forwardspeed, -1)
                self.motorR.drive(forwardspeed, -1)
            
            if self.distance.getAvoidance(1, 1.5) == True: # Right channel
                print("Detected Obstacle on the Left")
                self.motorL.drive(0)
                self.motorR.drive(0)
                self.motorL.drive(30, 1)
                self.motorR.drive(100, -1)
                while self.distance.getAvoidance(1, 1.5) == True:
                    sleep(0.3)
                self.motorL.drive(0)
                self.motorR.drive(0)
                self.motorL.drive(forwardspeed, -1)
                self.motorR.drive(forwardspeed, -1)
        

    def aimAtDetected(self, coordinates): # 640 x 480
        if coordinates[0][0] >= 340:
            self.motorL.drive(0)
            self.motorR.drive(0)
            self.right()
        elif coordinates[0][0] <= 300:
            self.motorL.drive(0)
            self.motorR.drive(0)
            self.left()
        else:
            self.motorL.drive(0)
            self.motorR.drive(0)

