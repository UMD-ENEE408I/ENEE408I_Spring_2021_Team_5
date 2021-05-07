# Modification of Face Recognition

import cv2
import numpy as np
import face_recognition
import pickle
import os
import time
import serial
import threading

print(cv2.__version__)
#reset_Timer = 8

def known_Greeting():
    ser = serial.Serial('/dev/ttyUSB0')
    timeMark = time.time()
    dtFIL = 0
    scaleFactor = .5
    
    reset_Timer = 8

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
    camSet1 = 'nvarguscamerasrc sensor-id=0 ee-mode=2 ee-strength=0 tnr-mode=2 tnr-strength=1 wbmode=3 ! video/x-raw(memory:NVMM), width=3264, height=2464, framerate=21/1,format=NV12 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(width)+', height='+str(height)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! videobalance contrast=1.5 saturation=1.2 ! appsink drop=True'
	
    cam0 = cv2.VideoCapture(camSet0)
    cam1 = cv2.VideoCapture(camSet1)

    def countdown():
    	global reset_Timer
    	while reset_Timer > 0:
        	print('T-minus', reset_Timer)
        	time.sleep(1)
        	reset_Timer -= 1
    countdown()
        
    count = threading.Thread(target=countdown)
    count.start()
    print('111111111111111111111')

    while reset_Timer>0:
    
        _, frame0 = cam0.read()
        _, frame1 = cam1.read()
        frameSmall0 = cv2.resize(frame0,(0,0), fx=scaleFactor, fy=scaleFactor)#smaller scale will faster the detection but it needs bigger face to reconize it.
        #frameSmall1 = cv2.resize(frame1,(0,0), fx=scaleFactor, fy=scaleFactor)

        facePositions0 = face_recognition.face_locations(frameSmall0)
        #facePositions1 = face_recognition.face_locations(frameSmall1)
    
        allEncodings0 = face_recognition.face_encodings(frameSmall0, facePositions0)
        #allEncodings1 = face_recognition.face_encodings(frameSmall1, facePositions1)
    
        for (top, right, bottom, left), face_encoding0 in zip(facePositions0, allEncodings0):
            name1 = 'Unknown'
            reset_Timer = 8
            print('222222222222222222')
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
        

            objY = abs(left+right)/2
            errorY = objY - width/2

            print(left)
            print(right)
            print(errorY)
            
                     
            if errorY<-50:
                ser.write(b'l')
                print('llllllllllllllllll')
                break

            elif errorY>50:
                ser.write(b'r')
                print('rrrrrrrrrrrrrrrrrrrr')
                break
                
            else:
                ser.write(b'f')
                print('middleeeeeeeeeeeeeeeee')
                break
        
        frame3 = np.hstack((frame0, frame1))
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
    
    both_Cam.release()
    cv2.destroyAllWindows()
