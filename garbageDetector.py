import numpy as np
import cv2
from picamera2 import Picamera2
import numpy as np

tolerance = 75

def detectGarbage(picam2):

    lower_limit = (1, 50, 50)
    upper_limit = (40, 255, 255)
    #cv2.flip(picam2, 1)
    frame = picam2.capture_array()
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    frame = cv2.flip(frame, 0)

    cv2.imshow('C',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        return 0

    # Proceso de enmascarado de la imagen
    blur = cv2.bilateralFilter(frame, 25, 75, 75)
    hsv_frameblur = cv2.cvtColor(blur, cv2.COLOR_RGB2HSV)

    # Generamos la máscara de color azul de la imagen
    color_mask = cv2.inRange(hsv_frameblur, lower_limit, upper_limit)

    # Aplicamos la máscara a la imagen suavizada
    masking_result = cv2.bitwise_and(blur, blur, mask=color_mask)

    # Combinamos la imagen original con la imagen filtrada para resaltar las zonas azules
    frame_blended_with_mask = cv2.addWeighted(frame, 0.6, masking_result, 0.4, 0.0)

    # Overlay espacial del video de fondo
    inverted_color_mask = cv2.bitwise_not(color_mask)
    foreground_layer = cv2.bitwise_and(frame, frame, mask=inverted_color_mask)

    # Detección de triángulos
    canny = cv2.Canny(masking_result, 100, 200)
    contours, _ = cv2.findContours(color_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    garbagePoints = []

    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        area = cv2.contourArea(contour)

        # Only checks blobs with more than 400 pixels of area surface
        if area >= 400:
            cv2.rectangle(frame_blended_with_mask, (x, y), (x + w, y + h), (255, 0, 0), 2)
            # Calculate centroid
            M = cv2.moments(contour)
            if M["m00"] != 0:
                cx = int(M["m10"] / M["m00"])  
                cy = int(M["m01"] / M["m00"])
            garbagePoints.append([cx, cy])

    if len(garbagePoints):
        centerPoint = [frame.shape[1] / 2,frame.shape[0]/2]
        diff = garbagePoints[0][0] - centerPoint[0]
        if diff > tolerance:
            return -1
        elif diff < -tolerance:
            return 1
        else:
            return 0
    return 0
