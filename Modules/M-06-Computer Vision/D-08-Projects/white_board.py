import cv2 as cv
import mediapipe as mp
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

font = cv.FONT_HERSHEY_SIMPLEX
color = (0, 255, 0)

lower_red1 = np.array([0, 150, 50])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 150, 50])
upper_red2 = np.array([180, 255, 255])


vc = cv.VideoCapture(0)
if vc.isOpened():
    response, frame = vc.read()

else:
    response = False

image_hight, image_width, _ = frame.shape

with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:

    while response:
        response, frame = vc.read()

        HSV = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        mask_red0 = cv.inRange(HSV, lower_red1, upper_red1)
        mask_red1 = cv.inRange(HSV, lower_red2, upper_red2)
        mask = mask_red0 + mask_red1

        image = cv.cvtColor(cv.flip(frame, 1), cv.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = hands.process(image)

        image.flags.writeable = True
        image = cv.cvtColor(image, cv.COLOR_RGB2BGR)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:

                index_x = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * image_width
                index_y = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_hight
                thumb_x = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x * image_width
                thumb_y = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y * image_hight

                mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        try:
            if index_x >= 610 and index_y <= 27:
                break
            if index_x <= 50 and index_y <= 27:
                image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
            dist_thumb_index = np.linalg.norm(np.array((index_x, index_y)) - np.array((thumb_x, thumb_y)))
            if dist_thumb_index <= 60:
                image[mask == 0] = dist_thumb_index*2
            print(dist_thumb_index)

        except Exception as e:
            continue
        cv.imshow('MediaPipe Hands', image)

        key = cv.waitKey(1)
        if key == 27:  # exit on ESC
            break

vc.release()
cv.destroyAllWindows()
