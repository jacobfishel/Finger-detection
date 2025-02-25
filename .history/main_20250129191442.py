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
    adaptive = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 5)
    _, otsu = cv2.threshold(gray, 125, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)


    #open the image to reduce small noise
    eroded = cv2.erode(thresh, (5, 5))
    cv2.imshow("Thresh Adaptive", adaptive)
    cv2.imshow("Otsu", otsu)
    cv2.imshow("Canny", canny)


    contours, _ = cv2.findContours(adaptive, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    foregroundObj = max(contours, key=cv2.contourArea)

    cv2.drawContours(frame, [foregroundObj], -1, (255, 0, 0), 3)

    # for contour in contours:

    #     area = cv2.contourArea(contour)
    #     convexHull = cv2.convexHull(contour)
    #     convexHullArea = cv2.contourArea(convexHull)

    #     #a hand will have a very low convexity
    #     handContour = []    #five finger hand
    #     convexity = area / convexHullArea if convexHullArea != 0 else 1
    #     if 10000 < area < 90000:
    #         print(area)
    #         if 0.2 < convexity < 0.9:
    #             print(convexity)

    #             perimeter = cv2.arcLength(contour, True)
    #             epsilon = 0.02 * perimeter

    #             vertices = cv2.approxPolyDP(contour, epsilon, True)

    #             numFingers = len(vertices)

    #             cv2.putText(frame, f"{numFingers}", (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0))

    #             #use cv2.convexity defects
    #             #cv2.approxPolyDP

                    


    #             #TODO: what is a ratio of area of a full hand to area of a finger down
    #             #full hand: about 64k
    #             # 4 fingers: about 61k
                 


    #             cv2.drawContours(frame, [contour], 0, (255, 0, 0), 2)


    cv2.imshow("frame", frame)

    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break