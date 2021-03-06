import face_recognition
import os
import pickle
import concurrent.futures
import cv2
print(cv2.__version__)

import speech_recognition as sr
import pyaudio
import threading
import time
#os.system("git pull")
def selfie():

    Encodings = []
    Names = []
    initial = os.getcwd()
    image_dir = initial + "/Image"
    width = 720
    height = 480
    flip = 0
    #print('line14')
    camSet1 = 'nvarguscamerasrc sensor-id=0 ee-mode=2 ee-strength=0 tnr-mode=2 tnr-strength=1 wbmode=3 ! video/x-raw(memory:NVMM), width=3264, height=2464, framerate=21/1,format=NV12 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(width)+', height='+str(height)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! videobalance contrast=1.5 saturation=1.2 ! appsink drop=True'	
    cam1 = cv2.VideoCapture(camSet1)

    while True:
        #print('line19')
        _, frame1 = cam1.read()
        cv2.imshow('myCam1',frame1)
        cv2.moveWindow('myCam1',900,0)
	
        k = cv2.waitKey(1)
    
        if cv2.waitKey(1) == ord('q'):    # If q is hit, the window will close
            print("Close")
            break

        else: 
            r = sr.Recognizer()
            with sr.Microphone() as source:

                print('Enter Your Speech:')
                r.adjust_for_ambient_noise(source, duration = 0.2)
                #r.adjust_for_ambient_noise(source)
                #audio = r.listen(source)
                audio = r.listen(source, phrase_time_limit=3)
    
                try:
                    unknown_Names = r.recognize_google(audio)
                    print('You said: {}'.format(unknown_Names))
                    #time.sleep(3)
                    image_file = image_dir + '/{}.jpg'.format(unknown_Names)
                    cv2.imwrite(image_file, frame1)
                except:
                    print("Try again")      
            break
    cam1.release()
    cv2.destroyAllWindows() 

    for root, dirs, files in os.walk(image_dir):
        for file in files:
            fullPath = os.path.join(root,file)
            print(fullPath)
            name = os.path.splitext(file)[0]
            print(name)
            person = face_recognition.load_image_file(fullPath)
            encoding = face_recognition.face_encodings(person)[0]
            Encodings.append(encoding)
            Names.append(name)
        print(Names)
        with open('train.pkl', 'wb') as f:
            pickle.dump(Names, f)
            pickle.dump(Encodings, f)

    os.system("git status")
    os.system("git add Image")
    os.system("git status")
    os.system("git commit -m image")
    os.system("git push")
    os.system("git status")
    os.system("git add train.pkl")
    os.system("git status")
    os.system("git commit -m train")
    os.system("git push")
