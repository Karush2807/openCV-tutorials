import cv2
import random

img=cv2.imread('openCV-tutorials//assets//valorant-logo-FAB2CA0E55-seeklogo.com.png', -1)
print(img.shape) #height*width*channels
print(img[0][2])

#ek imag ka portion crop krke, doosri jagah paste krdia
tag=img[120:150, 130:180]
img[30:60, 70:120]=tag

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows
