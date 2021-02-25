
# sudo apt-get install v4l-utils
# gst-launch-1.0 audiotestsrc ! alsasink
# gst-inspect-1.0 audiotestsrc
# gst-launch-1.0 audiotestsrc wave=1 freq=300 ! audio/x-raw,format=U8 ! alsasink

# gst-launch-1.0 videotestsrc ! ximagesink
# gst-launch-1.0 videotestsrc pattern=0 ! video/x-raw,format=BGR ! autovideoconvert ! ximagesink

# gst-launch-1.0 nvarguscamerasrc ! autovideoconvert ! ximagesink

import cv2
import numpy as np
import time
print(cv2.__version__)
timeMark = time.time()
dtFIL = 0
	
width = 720
height = 480
flip = 0
font = cv2.FONT_HERSHEY_SIMPLEX
     
camSet0 = 'nvarguscamerasrc sensor-id=1 ee-mode=2 ee-strength=0 tnr-mode=2 tnr-strength=1 wbmode=3 ! video/x-raw(memory:NVMM), width=3264, height=2464, framerate=21/1,format=NV12 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(width)+', height='+str(height)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! videobalance contrast=1.5 saturation=1.2 ! appsink drop=True'
camSet1 = 'nvarguscamerasrc sensor-id=0 ee-mode=2 ee-strength=0 tnr-mode=2 tnr-strength=1 wbmode=3 ! video/x-raw(memory:NVMM), width=3264, height=2464, framerate=21/1,format=NV12 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(width)+', height='+str(height)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! videobalance contrast=1.5 saturation=1.2 ! appsink drop=True'
	
cam0 = cv2.VideoCapture(camSet0)
cam1 = cv2.VideoCapture(camSet1)
while True:
    _, frame0 = cam0.read()
    _, frame1 = cam1.read()
    frame3 = np.hstack((frame0, frame1))
    
    dt = time.time()-timeMark
    timeMark = time.time()
    
    dtFIL = 0.9*dtFIL + 0.1*dt       # Low-pass filter
    fps = 1/dtFIL
    
    ### To show fps on the background      redcolor  solid box
    cv2.rectangle(frame3,(0,0), (150,40), (0,0,255), -1)
    cv2.putText(frame3, 'fps: '+str(round(fps,1)), (0, 30), font, 1, (0, 255, 255), 2)
    #print('fps: ',fps)
    
    cv2.imshow('both_Cam',frame3)
    cv2.moveWindow('both_Cam',200,0)
	
    if cv2.waitKey(1) == ord('q'):
        break
both_Cam.release()
cv2.destroyAllWindows()