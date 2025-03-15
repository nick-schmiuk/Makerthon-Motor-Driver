import actionHandler
import motorHandler
import distanceHandler
from picamera2 import Picamera2
import time
from garbageDetector import detectGarbage

motorL = motorHandler.motor(32, 8, 10)
motorR = motorHandler.motor(33, 18, 16)
distance = distanceHandler.Distance()


# Inicializar la cámara
picam2 = Picamera2()
picam2.configure(picam2.create_still_configuration(main={"format": "RGB888", "size": (640, 480)}))

# Iniciar la cámara
picam2.start()
time.sleep(2)

handler = actionHandler.MainHandler(motorL=motorL, motorR=motorR, distance=distance)
handler.driveAndAvoid(picam2)