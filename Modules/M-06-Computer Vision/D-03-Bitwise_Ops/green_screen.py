import numpy as np
import cv2 as cv

img3 = cv.imread('images/matrix3.jpg')

lower_red1 = np.array([0, 150, 50])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 150, 50])
upper_red2 = np.array([180, 255, 255])

vc = cv.VideoCapture(0)
if vc.isOpened():
    response, frame = vc.read()

else:
    response = False
i = 0
while response:
    response, frame = vc.read()
    HSV = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    mask_red0 = cv.inRange(HSV, lower_red1, upper_red1)
    mask_red1 = cv.inRange(HSV, lower_red2, upper_red2)
    mask = mask_red0 + mask_red1

    img3_resized = cv.resize(img3, (frame.shape[1], frame.shape[0]), interpolation=cv.INTER_NEAREST)

    frame[mask == 255] = img3_resized[mask == 255]
    cv.imshow('Balls', frame)

    key = cv.waitKey(1)
    if key == 27:  # exit on ESC
        break

cv.destroyAllWindows()
vc.release()

