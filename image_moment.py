import cv2
import numpy as np

img = cv2.imread('face.png',0)
# cv2.imshow('gah',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
ret, thresh = cv2.threshold(img,127,255,0)
_,contours,_ = cv2.findContours(thresh,1,2)

cnt = contours[66]
M = cv2.moments(cnt)
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
# print(M)
print(cx)
print(cy)
