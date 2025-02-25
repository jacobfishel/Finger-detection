import cv2
import numpy as np

#capture the webcam feed
cap = cv2.VideoCapture(0)

#while the cam is on, read each frame
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #canny edge detection
    canny = cv2.Canny(gray, 127, 255)
    # cv2.imshow("Canny", canny)



    #Threshold the image
    # _, thresh = cv2.threshold(gray, 90, 255, cv2.THRESH_BINARY)

    #calculate how many contour lines
    contours, _ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        cv2.drawContours(frame, [contour], -1, (0, 255, 255), 3)

    # convex = cv2.convexHull()

    cv2.imshow("Webcam", frame)
    cv2.imshow("Binary", canny)

    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break