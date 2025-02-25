import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    canny = cv2.Canny(frame, 127, 255, 3)
    cv2.imshow("Canny", canny)

    contours = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        area = cv2.contourArea(contour, True)

        if 0 < area < 2500:
            cv2.drawContours(frame, [contour], -1, (255, 0, 0), 3)
            # cv2.imshow("frame", frame)
    cv2.imshow("frame", frame)

    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break