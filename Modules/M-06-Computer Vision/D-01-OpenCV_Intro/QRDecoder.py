import cv2 as cv
import numpy as np

cv.namedWindow("QRcode_Reader")
capture = cv.VideoCapture(0)
qr_detector = cv.QRCodeDetector()
code_resp_l = []

if capture.isOpened():
    response, frame = capture.read()

else:
    response = False

while response:
    cv.imshow('QRcode_Reader', frame)
    response, frame = capture.read()

    retval, points = qr_detector.detect(frame)
    if retval:
        points_mat = points.reshape((4, 2)).astype(np.uint8)

        try:
            qr_resp, code = qr_detector.decode(frame, points)
            print(code)
            if qr_resp:
                code_resp_l.append(qr_resp)
                cv.line(frame, (points_mat[1, 0], points_mat[1, 1]), (points_mat[0, 0], points_mat[0, 1]), (0, 255, 0),
                        5)
                cv.line(frame, (points_mat[2, 0], points_mat[2, 1]), (points_mat[1, 0], points_mat[1, 1]), (0, 0, 0),
                        5)
                cv.line(frame, (points_mat[2, 0], points_mat[2, 1]), (points_mat[3, 0], points_mat[3, 1]), (0, 255, 0),
                        5)
                cv.line(frame, (points_mat[3, 0], points_mat[3, 1]), (points_mat[0, 0], points_mat[0, 1]), (0, 0, 255),
                        5)
                if len(code_resp_l) > 20:
                    cv.destroyWindow("QRcode_Reader")
                    cv.imshow('QRcode_shower', code)
                    key1 = cv.waitKey(20)
                    # if key1 == 27:  # exit on ESC
                    #     break
                    # code_resp_l = []
        except Exception as e:
            print('not a valid qr-code')
            continue

    key = cv.waitKey(20)
    if key == 27:  # exit on ESC
        break

cv.destroyAllWindows()



