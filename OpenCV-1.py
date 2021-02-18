import cv2 as cv
print(cv.__version__)

camSet='nvarguscamerasrc sensor-id=0 ! video/x-raw(memory:NVMM), width=3264, height=2464, framerate=21/1,format=NV12 ! nvvidconv flip-method=2 ! video/x-raw, width=800, height=600, format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'

cam=cv.VideoCapture(camSet)
while True:
    _, frame = cam.read()
    cv.imshow('mycam',frame)
   
    if cv.waitKey(1)==ord('q'):
        break
cam.release()
cv.destroyAllWindows()        


