
# sudo apt-get install v4l-utils
# gst-launch-1.0 audiotestsrc ! alsasink
# gst-inspect-1.0 audiotestsrc
# gst-launch-1.0 audiotestsrc wave=1 freq=300 ! audio/x-raw,format=U8 ! alsasink

# gst-launch-1.0 videotestsrc ! ximagesink
# gst-launch-1.0 videotestsrc pattern=0 ! video/x-raw,format=BGR ! autovideoconvert ! ximagesink

# gst-launch-1.0 nvarguscamerasrc ! autovideoconvert ! ximagesink

import cv2
print(cv2.__version__)
	
width = 720
height = 480
flip = 0
     
camSet0 = 'nvarguscamerasrc sensor-id=1 ee-mode=2 ee-strength=0 tnr-mode=2 tnr-strength=1 wbmode=3 ! video/x-raw(memory:NVMM), width=3264, height=2464, framerate=21/1,format=NV12 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(width)+', height='+str(height)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! videobalance contrast=1.5 saturation=1.2 ! appsink drop=True'
camSet1 = 'nvarguscamerasrc sensor-id=0 ee-mode=2 ee-strength=0 tnr-mode=2 tnr-strength=1 wbmode=3 ! video/x-raw(memory:NVMM), width=3264, height=2464, framerate=21/1,format=NV12 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(width)+', height='+str(height)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! videobalance contrast=1.5 saturation=1.2 ! appsink drop=True'
	

cam0 = cv2.VideoCapture(camSet0)
cam1 = cv2.VideoCapture(camSet1)
while True:
    _, frame0 = cam0.read()
    _, frame1 = cam1.read()
    cv2.imshow('myCam0',frame0)
    cv2.moveWindow('myCam0',0,0)
	

    cv2.imshow('myCam1',frame1)
    cv2.moveWindow('myCam1',900,0)
	

    if cv2.waitKey(1) == ord('q'):
        break
cam0.release()
cam1.release()
cv2.destroyAllWindows()
