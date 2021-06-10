import cv2 as cv
import torch
import numpy as np
import torch.nn.functional as F
from torchvision import transforms

model = torch.load('Best_model2.pth')
model.eval()

vc = cv.VideoCapture(0)
window_name = 'Numbers'
cv.namedWindow(window_name)


def pre_pro(img):
    clone_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY).astype(np.float32)
    clone_gray = cv.resize(clone_gray, (28, 28))
    # tensor_img = torch.from_numpy(clone_gray).reshape(784, 1)
    # tensor_img = F.normalize(tensor_img)
    # tensor_img = tensor_img.view((-1, 784))
    return clone_gray


def predict(img_pro):
    with torch.no_grad():
        predictions = model(img_pro)
    #print(predictions)
    return predictions


if vc.isOpened():
    response, frame = vc.read()

else:
    response = False


while response:
    response, frame = vc.read()
    cv.imshow(window_name, frame)

    clone = frame.copy()
    tensor_img = pre_pro(clone)
    cv.imwrite('no.jpg', tensor_img)

    # predict_real = predict(tensor_img)
    # print(predict_real)
    # #print(np.argmax((np.array(predict_real))))

    key = cv.waitKey(1)
    if key == 27:  # exit on ESC
        break

cv.destroyAllWindows()
vc.release()
