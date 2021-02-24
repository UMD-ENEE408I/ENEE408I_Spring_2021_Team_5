import cv2
print(cv2.__version__)

width=640
height=420
flip=0

camSet0 = 'nvarguscamerasrc sensor-id=1 ! video/x-raw(memory:NVMM), width=3264, height=2464, framerate=21/1,format=NV12 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(width)+', height='+str(height)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
camSet1 = 'nvarguscamerasrc sensor-id=0 ! video/x-raw(memory:NVMM), width=3264, height=2464, framerate=21/1,format=NV12 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(width)+', height='+str(height)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'

cam0 = cv2.VideoCapture(camSet0)
cam1 = cv2.VideoCapture(camSet1)
while True:
    _, frame0 = cam0.read()
    _, frame1 = cam1.read()
    cv2.imshow('myCam0',frame0)
    cv2.moveWindow('myCam0',0,0)

    cv2.imshow('myCam1',frame1)
    cv2.moveWindow('myCam1',1000,0)

    if cv2.waitKey(1)==ord('q'):
        break
cam0.release()
cam1.release()
cv2.destroyAllWindows()

