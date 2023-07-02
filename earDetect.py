# 'haarcascade_mcs_rightear.xml' is for Left ear and vice versa.

import cv2 as cv
import os

img = cv.imread('Left Ear.jpg')
print(img.shape)
classifier = cv.CascadeClassifier('haarcascade_mcs_rightear.xml')
boxes = classifier.detectMultiScale(img)

for box in boxes:
    x,y,width,height = box
    x2,y2, = x+width,y+height
    cv.rectangle(img,(x,y),(x2,y2),(0,255,0), 5)
    print(x,y,width,height)

cv.imshow('Ear Detected',img)
cv.waitKey(0)
cv.destroyAllWindows()

temp = cv.imread('Left Ear.jpg')
temp = temp[x:x+height,y:y+width]
cv.imshow('Left Ear',temp)
cv.waitKey(0)
cv.destroyAllWindows()

img1 = temp
img2 = temp

img1 = cv.cvtColor(img1,cv.COLOR_BGR2GRAY)
img2 = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)

sift = cv.SIFT_create()
bf = cv.BFMatcher(cv.NORM_L2,crossCheck=True)

keypoints1, descriptors1 = sift.detectAndCompute(img1,None)
keypoints2, descriptors2 = sift.detectAndCompute(img2,None)

matches = bf.match(descriptors1,descriptors2)

matches = sorted(matches,key=lambda x: x.distance)

img3 = cv.drawMatches(img1,keypoints1,img2,keypoints2,matches,img2)
new_size = (450, 340)
img3 = cv.resize(img3, new_size)

cv.imshow('SIFT',img3)
cv.waitKey(0)