import cv2 as cv
import numpy as np

path = "numberscv2.jpg"

img = cv.imread(path)
copy = img.copy()
copy = cv.resize(copy, (512, 512))
copy = cv.rotate(copy, cv.ROTATE_90_COUNTERCLOCKWISE)

rotated = cv.rotate(img, cv.ROTATE_90_COUNTERCLOCKWISE)

gray = cv.cvtColor(rotated, cv.COLOR_BGR2GRAY)

gray = cv.resize(gray, (512, 512))

inv = ~gray
mask = inv > 160
inv[~mask] = 0
kernel = np.ones((5, 5), np.uint8)

# blurred = cv.GaussianBlur(inv, (5, 5), 0)
# edged = cv.Canny(blurred, 100, 200, 255)
closing = cv.morphologyEx(inv, cv.MORPH_CLOSE, kernel)
dilation = cv.dilate(closing, kernel, iterations=2)

contours, h = cv.findContours(dilation, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

color = (0, 255, 0)
print(len(contours))

sorted_contours = sorted(contours, key=cv.contourArea, reverse=True)

cv.drawContours(copy, sorted_contours[:7], -1, color, 2)

num_cont = sorted_contours[:7]

blank = np.zeros((512, 512))
digits = []
for cont in num_cont:
    [x, y, w, h] = cv.boundingRect(cont)
    cv.rectangle(copy, (x, y), (x + w, y + h), (0, 0, 255), 2)
    #imgdig = dilation[x]
    #digits.append()

cv.imshow('numbers', copy)
cv.waitKey()
cv.destroyAllWindows()
