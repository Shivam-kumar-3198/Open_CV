import cv2 as cv

img = cv.imread('photos/stud.jpg')

cv.imshow('Student', img)

cv.waitKey(3000)