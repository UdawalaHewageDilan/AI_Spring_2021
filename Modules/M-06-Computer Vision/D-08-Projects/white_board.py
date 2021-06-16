import cv2 as cv
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands


vc = cv.VideoCapture(0)
if vc.isOpened():
    response, frame = vc.read()

else:
    response = False

with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:

    while response:
        response, frame = vc.read()

        image = cv.cvtColor(cv.flip(frame, 1), cv.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = hands.process(image)

        image.flags.writeable = True
        image = cv.cvtColor(image, cv.COLOR_RGB2BGR)
        if results.multi_hand_landmarks:
            #print(results.multi_hand_landmarks[0])
            for hand_landmarks in results.multi_hand_landmarks:
                print(hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP])
                mp_drawing.draw_landmarks(image, [hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP]])
        cv.imshow('MediaPipe Hands', image)

        key = cv.waitKey(1)
        if key == 27:  # exit on ESC
            break

vc.release()
cv.destroyAllWindows()
