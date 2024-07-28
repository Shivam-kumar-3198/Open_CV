import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    # Works for images, videos, and live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

capture = cv.VideoCapture('D:/OPEN CV/Open_CV/Videoes/carry.mp4')

if not capture.isOpened():
    print("Error: Could not open video.")
    exit()

while True:
    isTrue, frame = capture.read()

    if not isTrue:
        print("Error: Could not read frame.")
        break

    frame_resized = rescaleFrame(frame, scale=0.2)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
