import numpy as np
import cv2 as cv
import time 
import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)

socket.connect("tcp://localhost:5556")
socket.set(zmq.SUBSCRIBE, b'')

while True:
    rx = socket.recv(0, False, False)
    buf = memoryview(rx)
    
    x = np.frombuffer(buf, dtype='uint8')
    A = x.reshape(480,640)
    print(A.shape)
    print(A.dtype)
    print(type(A))
    print(A.ndim)
    if A.shape == (480, 640):
        print("good size")
        cv.imshow('frame', A)
    
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    
cv.destroyAllWindows()
