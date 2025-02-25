import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    canny = cv2.Canny(frame, 127, 255, 3)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray", gray)
    # _, thresh = cv2.threshold()
    cv2.imshow("Canny", canny)

    contours, _ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:

        area = cv2.contourArea(contour)
        convexHull = cv2.convexHull(contour)

        #a hand will have a very low convexity
        convexity = area / convexHull
        if 20000 < area < 80000:
            print(area)



            cv2.drawContours(frame, [contour], 0, (255, 0, 0), 2)


    cv2.imshow("frame", frame)

    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break