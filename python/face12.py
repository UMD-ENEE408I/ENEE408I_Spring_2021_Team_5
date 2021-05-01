import cv2
import numpy as np
import face_recognition
import pickle
import os
import time
import serial
print(cv2.__version__)

def known_Greeting():
    ser = serial.Serial('/dev/ttyUSB0')
    timeMark = time.time()
    dtFIL = 0
    scaleFactor = .6

    width = 720
    height = 480
    flip = 0
    font = cv2.FONT_HERSHEY_SIMPLEX

    Encodings = []
    Names = []
    with open('train.pkl', 'rb') as f:
        Names = pickle.load(f)
        Encodings = pickle.load(f)
    

    camSet0 = 'nvarguscamerasrc sensor-id=1 ee-mode=2 ee-strength=0 tnr-mode=2 tnr-strength=1 wbmode=3 ! video/x-raw(memory:NVMM), width=3264, height=2464, framerate=21/1,format=NV12 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(width)+', height='+str(height)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! videobalance contrast=1.5 saturation=1.2 ! appsink drop=True'
    #camSet1 = 'nvarguscamerasrc sensor-id=0 ee-mode=2 ee-strength=0 tnr-mode=2 tnr-strength=1 wbmode=3 ! video/x-raw(memory:NVMM), width=3264, height=2464, framerate=21/1,format=NV12 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(width)+', height='+str(height)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! videobalance contrast=1.5 saturation=1.2 ! appsink drop=True'
	
    cam0 = cv2.VideoCapture(camSet0)
    #cam1 = cv2.VideoCapture(camSet1)

    while True:
        _, frame0 = cam0.read()
        frameSmall0 = cv2.resize(frame0,(0,0), fx=scaleFactor, fy=scaleFactor)#smaller scale will faster the detection but it needs bigger face to reconize it.
        
        facePositions0 = face_recognition.face_locations(frameSmall0)
        allEncodings0 = face_recognition.face_encodings(frameSmall0, facePositions0)

    
        for (top, right, bottom, left), face_encoding0 in zip(facePositions0, allEncodings0):
            name1 = 'Unknown'
            matches = face_recognition.compare_faces(Encodings, face_encoding0)
            if True in matches:
                first_match_index = matches.index(True)
                name1 = Names[first_match_index]
                    
            top = int(top/scaleFactor)
            right = int(right/scaleFactor)
            bottom = int(bottom/scaleFactor)
            left = int(left/scaleFactor)
            cv2.rectangle(frame0,(left, top),(right, bottom), (255,0,0), 2)
            cv2.putText(frame0, name1, (left, top+0), font, .75, (0,0,255), 2 )
        
            #area = cv2.rectangle(frame0,(left, top),(right, bottom), (255,0,0), 2)
            if False in matches:
                objY = (left+right)/2
                errorY = objY - width/2

                ser.write(b'f')
                time.sleep(1)
                if abs(errorY)>100:
                    ser.write(b'f')
                
                    if abs(errorY)>left:
                        ser.write(b'l')
                        time.sleep(0.5)
                        ser.write(b'f')
                        time.sleep(1.5)
                    else:
                        ser.write(b'r')
                        time.sleep(0.5)
                        ser.write(b'f')
                        time.sleep(1.5)
                
                else:
                    ser.write(b's')
                    break
                if False in matches:
                    ser.write(b's')
                    break
            except:
                break
        
        frame3 = np.hstack(frame0)
        dt = time.time()-timeMark
        fps = 1/dt
        timeMark = time.time()
        dtFIL = 0.9*dtFIL + 0.1*fps       # Low-pass filter
        ### To show fps on the background      redcolor  solid box
        cv2.rectangle(frame3,(0,0), (150,40), (0,0,255), -1)
        cv2.putText(frame3, 'fps: '+str(round(fps,1)), (0, 30), font, 1, (0, 255, 255), 2)
    
        cv2.imshow('both_Cam',frame3)
        cv2.moveWindow('both_Cam',200,0)
	
        if cv2.waitKey(1) == ord('q'):
            break
	
    cam0.release()
    cv2.destroyAllWindows()