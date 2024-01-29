import cv2
import os

vidcap = cv2.VideoCapture('badapple.mp4')
success, image = vidcap.read()
count = 0

os.chdir("frames")

while success:
    cv2.imwrite("%d.png" % count, image)
    success, image = vidcap.read()
    print('Read a new frame: ', success)
    count += 1
