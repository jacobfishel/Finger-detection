import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    canny = cv2.Canny(frame, 100, 255, 3)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    adaptive1 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 0)
    adaptive2 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 5)
    adaptive3 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 10)

    cv2.imshow("1", adaptive1)
    cv2.imshow("2", adaptive2)
    cv2.imshow("3", adaptive3)

    adaptive4 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 0)
    adaptive5 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 5)
    adaptive6 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 10)

    cv2.imshow("4", adaptive4)
    cv2.imshow("5", adaptive5)
    cv2.imshow("6", adaptive6)


    #open the image to reduce small noise
    eroded = cv2.erode(thresh, (5, 5))
    cv2.imshow("Thresh", thresh)
    cv2.imshow("Canny", canny)


    contours, _ = cv2.findContours(adaptive1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:

        area = cv2.contourArea(contour)
        convexHull = cv2.convexHull(contour)
        convexHullArea = cv2.contourArea(convexHull)

        #a hand will have a very low convexity
        convexity = area / convexHullArea if convexHullArea != 0 else 1
        if 50000 < area < 90000:
            print(area)
            if 0.4 < convexity < 0.8:
                print(convexity)

                #TODO: what is a ration of area of a full hand to area of a finger down
                #full hand: about 64k
                # 4 fingers: about 61k
                 


                cv2.drawContours(frame, [contour], 0, (255, 0, 0), 2)


    cv2.imshow("frame", frame)

    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break