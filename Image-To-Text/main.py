from os import listdir
import numpy as np
import cv2

IMAGE_PATH = './Images/'
RESULT_PATH = './Results/'

FILL_CHAR = ' .'    # [0] = low [1] = high

ImgNameList = listdir(IMAGE_PATH)
# print(ImgNameList)

for ImgName in ImgNameList:
    img = cv2.imread(IMAGE_PATH + ImgName)
    img = cv2.resize(img, fx=0.6, fy=0.2, dsize=(0, 0)) # resize here
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.Canny(img, 100, 200)

    img = np.array(img)
    x, y = img.shape

    result = open(RESULT_PATH + ImgName.split('.')[0] + '.txt', 'w')
    for i in range(x):
        for j in range(y):
            if img[i][j] == 255:
                result.write(FILL_CHAR[1])
            else:
                result.write(FILL_CHAR[0])
        result.write('\n')
    result.close()