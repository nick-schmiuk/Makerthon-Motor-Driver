import tkinter
import motorHandler
from time import sleep

window = tkinter.Tk()
motorL = motorHandler.motor(32, 8, 10)
motorR = motorHandler.motor(33, 16, 18)

def forwards():
    motorL.drive(70, 1)
    motorR.drive(70, 1)
    sleep(1)
    motorL.drive(0)
    motorR.drive(0)

def backwards():
    motorL.drive(70, -1)
    motorR.drive(70, -1)
    sleep(1)
    motorL.drive(0)
    motorR.drive(0)

def left():
    motorR.drive(50, 1)
    motorL.drive(50, -1)
    sleep(1)
    motorL.drive(0)
    motorR.drive(0)

def right():
    motorL.drive(50, 1)
    motorR.drive(50, -1)
    sleep(1)
    motorL.drive(0)
    motorR.drive(0)

fwd = tkinter.Button(window, text="↑",command=forwards)
bwd = tkinter.Button(window, text="↓", command=backwards)
lft = tkinter.Button(window, text="←", command=left)
rgt = tkinter.Button(window, text="→", command=right)

fwd.grid(row=1,column=2)
lft.grid(row=2, column=1)
rgt.grid(row=2, column=3)
bwd.grid(row=3, column=2)

window.mainloop()