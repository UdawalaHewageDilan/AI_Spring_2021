import cv2 as cv
import numpy as np

font = cv.FONT_HERSHEY_SIMPLEX
vc = cv.VideoCapture(0)
cv.namedWindow('Balls')
if vc.isOpened():
    response, frame = vc.read()

else:
    response = False

while response:
    cv.imshow('Balls', frame)
    response, frame = vc.read()

    lower_red1 = np.array([0, 180, 150])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 180, 150])
    upper_red2 = np.array([180, 255, 255])

    HSV = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    mask_red0 = cv.inRange(HSV, lower_red1, upper_red1)
    mask_red1 = cv.inRange(HSV, lower_red2, upper_red2)
    mask = mask_red0 + mask_red1

    dist_l = []
    for row in range(mask.shape[0]):
        for column in range(mask.shape[1]):
            if mask[row, column] == 255:
                dist_l.append([row, column])
    if len(dist_l) > 0:
        dist_l = np.array(dist_l)
        try:
            center = dist_l[int(dist_l.shape[0]/2), :]
            radius = abs(np.argmin(dist_l[:, 1]) - np.argmax(dist_l[:, 1]))
            print(center, radius/2)
            cv.circle(frame, center, 25, (0, 255, 0), 5)

            cv.putText(frame, "I'm RED", center+[25, 25], font, 2, (0, 255, 0), 5, cv.LINE_AA)
            # cv.putText(frame, "I'm not red", center + [125, 25], font, 1, (0, 0, 0), 3, cv.LINE_AA)
            # cv.putText(frame, "I'm not red", center + [25, 125], font, 1, (0, 0, 0), 3, cv.LINE_AA)
            # cv.putText(frame, "I'm not red", center + [-175, 25], font, 1, (0, 0, 0), 3, cv.LINE_AA)
            # cv.putText(frame, "I'm not red", center + [25, -175], font, 1, (0, 0, 0), 3, cv.LINE_AA)

        except Exception as e:
            continue
    key = cv.waitKey(20)
    if key == 27:  # exit on ESC
        break

cv.destroyAllWindows()
