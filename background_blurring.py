import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(gray, 90, 255, cv2.THRESH_BINARY)

    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    blurred = cv2.GaussianBlur(frame, (21, 21), 0)

    #convert mask to 3 channels
    mask_3d = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    foreground = cv2.bitwise_and(frame, mask_3d)
    background = cv2.bitwise_and(blurred, cv2.bitwise_not(mask_3d))

    final = cv2.add(foreground, background)

    cv2.imshow("kl", final)

    if cv2.waitKey(1) == ord('q'):
        break


cv2.destroyAllWindows()