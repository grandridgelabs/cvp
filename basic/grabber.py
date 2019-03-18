import numpy as np
import cv2 as cv
import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5556")

cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    print(gray.shape)
    print(type(gray))
    print(gray.dtype)
    print(gray.ndim)
    socket.send(gray, 0, False, False)

    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
    

