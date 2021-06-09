import numpy as np
import cv2 as cv

# img = cv.imread('images/blue-red-flowers.png')
img1 = cv.imread('images/matrix.jpg')
img2 = cv.imread('images/matrix2.jpg')
img3 = cv.imread('images/matrix3.jpg')
#img4 = cv.imread('images/matrix.jpg')


#
lower_red1 = np.array([0, 150, 50])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 150, 50])
upper_red2 = np.array([180, 255, 255])
#
# HSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# mask_red0 = cv.inRange(HSV, lower_red1, upper_red1)
# mask_red1 = cv.inRange(HSV, lower_red2, upper_red2)
# mask = mask_red0 + mask_red1
#
# img[mask == 255] = img2_resized[mask == 255]
#
#
# cv.imshow('test', img)
# cv.waitKey()
# cv.destroyAllWindows()

vc = cv.VideoCapture(0)
#cv.namedWindow('Balls')
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
    img1_resized = cv.resize(img1, (frame.shape[1], frame.shape[0]), interpolation=cv.INTER_NEAREST)
    img2_resized = cv.resize(img2, (frame.shape[1], frame.shape[0]), interpolation=cv.INTER_NEAREST)
    img3_resized = cv.resize(img3, (frame.shape[1], frame.shape[0]), interpolation=cv.INTER_NEAREST)
    if i % 3 == 0:
        frame[mask == 255] = img3_resized[mask == 255]
    # elif i % 3 == 1:
    #     frame[mask == 255] = img2_resized[mask == 255]
    # elif i % 3 == 2:
    #     frame[mask == 255] = img1_resized[mask == 255]
    cv.imshow('Balls', frame)

    #cv.imshow('mask', mask)

    key = cv.waitKey(1)
    if key == 27:  # exit on ESC
        break

cv.destroyAllWindows()
