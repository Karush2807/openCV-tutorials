# leanrt to read images, data
# concepts leant:
# 1. loading an image
# 2. displaying an image
# 3. resizing an image
# 4. rotating an image

import cv2

img=cv2.imread('openCV-tutorials//assets//valorant-logo-FAB2CA0E55-seeklogo.com.png', -1) # greyscale/normal color/ without transparency
# img=cv2.resize(img, (40, 40))
img=cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imwrite('new_img.png', img)
cv2.imshow('Image', img)
cv2.waitKey(0) #will wait for us, to press any key
cv2.destroyAllWindows()


#-1, cv2.IMREAD_COLOR: color image
# 0, cv2.IMREAD_GRAYSCALE: grayscale mode
# 1, cv2.IMREAD_UNCHANGED: loads image as such including alpha values