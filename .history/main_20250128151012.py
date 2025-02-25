import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    canny = cv2.Canny(frame, 30, 255, 3)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    #open the image to reduce small noise
    eroded = cv2.erode(thresh, (5, 5))
    cv2.imshow("Thresh", thresh)
    cv2.imshow("Canny", canny)


    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:

        area = cv2.contourArea(contour)
        convexHull = cv2.convexHull(contour)
        convexHullArea = cv2.contourArea(convexHull)

        #a hand will have a very low convexity
        convexity = area / convexHullArea if convexHullArea != 0 else 1
        if 20000 < area < 80000:
            print(area)
            if 0.1 < convexity < 0.5:
                print(convexity)



                cv2.drawContours(frame, [contour], 0, (255, 0, 0), 2)


    # cv2.imshow("frame", frame)

    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break