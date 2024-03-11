from os import listdir, system
import numpy as np
import time
import cv2

VIDEO_PATH = './Videos/'
FILL_CHAR = ' .'    # [0] = low [1] = high

video = cv2.VideoCapture(VIDEO_PATH + listdir(VIDEO_PATH)[0])

while True:
    ret, frame = video.read()
    
    if not ret:
        break

    frame = cv2.resize(frame, fx=0.1, fy=0.1, dsize=(0, 0))
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.Canny(frame, 100, 200)
    frame = np.array(frame)

    x, y = frame.shape
    show = ''
    for i in range(x):
        for j in range(y):
            if frame[i][j] == 255:
                show += FILL_CHAR[1]
            else:
                show += FILL_CHAR[0]
        show += '\n'

    system('cls')   # For Windows, use 'cls'
    print(show)
    time.sleep(1/60)

video.release()
