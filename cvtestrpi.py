import cv2
import numpy as np
from picamera2 import Picamera2
from picamera2.encoders import JpegEncoder
from picamera2.outputs import FileOutput
import time

def main():
    # Initialize the camera
    picam2 = Picamera2()
    config = picam2.create_preview_configuration()
    picam2.configure(config)
    picam2.start_preview()
    picam2.start()

    # Allow the camera to warm up
    time.sleep(2)

    while True:
        # Capture a frame
        array = picam2.capture_array("main")

        # Convert the frame to the HSV color space
        hsv_frame = cv2.cvtColor(array, cv2.COLOR_BGR2HSV)

        # Define the lower and upper bounds for the color (e.g., red)
        lower_red1 = np.array([0, 120, 70], dtype=np.uint8)
        upper_red1 = np.array([10, 255, 255], dtype=np.uint8)
        lower_red2 = np.array([170, 120, 70], dtype=np.uint8)
        upper_red2 = np.array([180, 255, 255], dtype=np.uint8)

        # Create binary masks for the two red ranges
        mask1 = cv2.inRange(hsv_frame, lower_red1, upper_red1)
        mask2 = cv2.inRange(hsv_frame, lower_red2, upper_red2)

        # Combine the two masks
        mask = cv2.bitwise_or(mask1, mask2)

        # Apply a series of dilations and erosions to remove any small blobs left in the mask
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)

        # Find contours in the mask
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Draw bounding boxes around the detected color regions
        for contour in contours:
            # Get the bounding box coordinates
            x, y, w, h = cv2.boundingRect(contour)
            # Draw the bounding box on the frame
            cv2.rectangle(array, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Display the original frame with bounding boxes
        cv2.imshow("Original Frame", array)

        # Break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close all OpenCV windows
    picam2.stop()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()