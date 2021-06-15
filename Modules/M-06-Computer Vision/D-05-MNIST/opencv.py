import cv2 as cv
import torch
import numpy as np
import torch.nn.functional as F


model = torch.load('Best_model2.pth')
model.eval()

font = cv.FONT_HERSHEY_SIMPLEX

vc = cv.VideoCapture(0)
window_name = 'Numbers'
cv.namedWindow(window_name)


def pre_pro(img):
    clone_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    clone_gray = ~clone_gray
    mask = clone_gray > 200
    clone_gray[~mask] = 0
    clone_gray_resized = cv.resize(clone_gray, (28, 28)).astype(np.float32)
    cv.imwrite('no.jpg', clone_gray_resized)
    tensor_img = torch.from_numpy(clone_gray_resized).reshape(784, 1)
    tensor_img = F.normalize(tensor_img)
    tensor_img = tensor_img.view((-1, 784))
    return clone_gray, tensor_img


def predict(img_pro):
    with torch.no_grad():
        predictions = model(img_pro)
    return predictions


if vc.isOpened():
    response, frame = vc.read()

else:
    response = False


while response:
    response, frame = vc.read()

    clone = frame.copy()
    mask, tensor_img = pre_pro(clone)
    mask1 = mask != 0
    b, g, r = cv.split(clone)
    b[mask1] = 0
    g[mask1] = 255
    r[mask1] = 0
    frame_new = cv.merge((b, g, r))

    predict_real = predict(tensor_img)
    print(predict_real)
    print(np.argmax((np.array(predict_real))))
    predicted = np.argmax((np.array(predict_real)))
    frame_new = cv.putText(frame_new, str(predicted), (50, 50), font, 1, (255, 0, 0), 2, cv.LINE_AA)
    cv.imshow(window_name, frame_new)

    key = cv.waitKey(1)
    if key == 27:  # exit on ESC
        break

cv.destroyAllWindows()
vc.release()
