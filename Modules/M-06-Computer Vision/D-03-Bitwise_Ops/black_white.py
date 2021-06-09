import cv2 as cv


class BlackWhiteColour:

    def __init__(self, image_path, colour=1):
        self.image_path = image_path
        self.colour = colour
        self.image = cv.imread(image_path, self.colour)
        if self.colour == 1:
            self.B, self.G, self.R = cv.split(self.image)
            self.black_white()
            self.coloured()

    def black_white(self):
        return cv.bitwise_and(self.B, self.G, self.R)

    def coloured(self):
        return cv.merge((self.B, self.G, self.R))

