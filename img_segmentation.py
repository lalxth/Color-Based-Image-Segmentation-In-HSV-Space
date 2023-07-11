import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("/home/laal/PROJECTS/practice/imagesegmentation/candy.jpg")

hsv_image= cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
lower_limit = np.array([50, 80, 20])
upper_limit = np.array([80, 255, 255])
mask = cv2.inRange(hsv_image,lower_limit, upper_limit)

result = cv2.bitwise_and(image,image,mask=mask)

cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("window",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
cv2.imshow('window',image)
cv2.imshow('window', result)
cv2.imwrite('result.png',result)
cv2.waitKey(0)

