import tkinter
import motorHandler
from time import sleep
import distanceHandler

window = tkinter.Tk()
motorL = motorHandler.motor(32, 8, 10)
motorR = motorHandler.motor(33, 18, 16)
distance = distanceHandler.Distance()


def forwards():
    motorL.drive(70, -1)
    motorR.drive(70, -1)
    sleep(1)
    motorL.drive(0)
    motorR.drive(0)

def backwards():
    motorL.drive(70, 1)
    motorR.drive(70, 1)
    sleep(1)
    motorL.drive(0)
    motorR.drive(0)

def left():
    motorR.drive(70, 1)
    motorL.drive(70, -1)
    sleep(1)
    motorL.drive(0)
    motorR.drive(0)

def right():
    motorL.drive(70, 1)
    motorR.drive(70, -1)
    sleep(1)
    motorL.drive(0)
    motorR.drive(0)

def halt():
    motorL.drive(0)
    motorR.drive(0)

def driveAndAvoid():
    while True:
        motorL.drive(70, -1)
        motorR.drive(70, -1)
        if distance.getAvoidance(0, 0.5) == True: # Left channel
            halt()
            motorL.drive(70, -1)
            motorR.drive(70, 1)
            while distance.getAvoidance(0, 0.5) == True:
                sleep(0.1)
            halt()
            motorL.drive(70, -1)
            motorR.drive(70, -1)
        
        if distance.getAvoidance(1, 0.5) == True: # Left channel
            halt()
            motorL.drive(70, 1)
            motorR.drive(70, -1)
            while distance.getAvoidance(1, 0.5) == True:
                sleep(0.1)
            halt()
            motorL.drive(70, -1)
            motorR.drive(70, -1)
       


    
fwd = tkinter.Button(window, text="↑",command=forwards)
bwd = tkinter.Button(window, text="↓", command=backwards)
lft = tkinter.Button(window, text="←", command=left)
rgt = tkinter.Button(window, text="→", command=right)

startAvoidancedrive = tkinter.Button(window, text="Avoidancetest", command=driveAndAvoid)

fwd.grid(row=1,column=2)
lft.grid(row=2, column=1)
rgt.grid(row=2, column=3)
bwd.grid(row=3, column=2)
startAvoidancedrive.grid(row=4, column=1)

window.mainloop()