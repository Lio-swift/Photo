import cv2 as cv
import numpy as np


class Pro(object):

    def __init__(self, image):
        self.o = cv.imread(image)
        self.k = 2

    def custom_threshold(self):
        # 自动计算阈值并对图像进行二值化
        gray = cv.cvtColor(self.o, cv.COLOR_RGB2GRAY)  # 把输入图像灰度化
        h, w = gray.shape[:2]
        m = np.reshape(gray, [1, w * h])
        mean = m.sum() / (w * h)
        ret, binary = cv.threshold(gray, mean, 255, cv.THRESH_BINARY)
        cv.imwrite("./binary.png", binary)

    def dithering(self):
        # 你懂
        height = self.o.shape[0]
        width = self.o.shape[1]

        # 保证图像长宽都是2的整数倍
        if height % 2 != 0:
            height -= 1
        if width % 2 != 0:
            width -= 1

        if height > width:
            self.o = np.rot90(self.o)
            height, width = width, height

        for h in range(0, height, self.k):
            for w in range(0, width, self.k):
                gray = int(
                    sum(sum([self.o[h][w], self.o[h][w + 1], self.o[h + 1][w], self.o[h + 1][w + 1]])) / (
                                self.k * self.k)
                )
                temp = self.o[h:h + 2, w:w + 2]  # 取样
                self.change(gray, temp)

        ret, img = cv.threshold(self.o, 127, 255, cv.THRESH_BINARY)
        cv.imwrite("dither.png", img)

    def change(self, gray, img):
        # 计算矩阵每个梯级间的步长
        step = int(255 / (self.k * self.k + 1))
        k1 = range(0, step)
        k2 = range(step, 2 * step)
        k3 = range(2 * step, 3 * step)
        k4 = range(3 * step, 4 * step)
        k5 = range(4 * step, 255 + 1)
        if gray in k1:
            img[0][0] = 0
            img[0][1] = 0
            img[1][0] = 0
            img[1][1] = 0
        if gray in k2:
            img[0][0] = 0
            img[0][1] = 0
            img[1][0] = 255
            img[1][1] = 0
        if gray in k3:
            img[0][0] = 0
            img[0][1] = 255
            img[1][0] = 255
            img[1][1] = 0
        if gray in k4:
            img[0][0] = 0
            img[0][1] = 255
            img[1][0] = 255
            img[1][1] = 255
        if gray in k5:
            img[0][0] = 255
            img[0][1] = 255
            img[1][0] = 255
            img[1][1] = 255
