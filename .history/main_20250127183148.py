import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    canny = cv2.Canny(frame, 127, 255, 3)
    cv2.imshow("Canny", canny)


    if cv2.waitKey(0) == ord('q'):
        cv2.destroyAllWindows()
        break