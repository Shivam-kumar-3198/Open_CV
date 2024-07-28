import cv2 as cv
# reading videoes

capture = cv.VideoCapture('D:\OPEN CV\Open_CV\Videoes\carry.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame )

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()   

