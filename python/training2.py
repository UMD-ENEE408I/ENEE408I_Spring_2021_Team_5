import face_recognition
import cv2
print(cv2.__version__)
import os
import time
import pickle
import threading
import concurrent.futures
import speech_recognition as sr

width = 720
height = 480
flip = 0

camSet1 = 'nvarguscamerasrc sensor-id=0 ee-mode=2 ee-strength=0 tnr-mode=2 tnr-strength=1 wbmode=3 ! video/x-raw(memory:NVMM), width=3264, height=2464, framerate=21/1,format=NV12 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(width)+', height='+str(height)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! videobalance contrast=1.5 saturation=1.2 ! appsink drop=True'
	
cam1 = cv2.VideoCapture(camSet1)
Encodings = []
Names = []
image_dir = '/home/lian/Desktop/pyPro/images/known'

def trainName():
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
        

def voiceRecog():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Enter Your Name:')
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    
        try:
            unknown_Names = r.recognize_google(audio)
            print('You said: {}'.format(unknown_Names))
        except:
            break
            
voiceEncode = threading.Thread(target=voiceRecog)



while True:
    _, frame1 = cam1.read()

    cv2.imshow('myCam1',frame1)
    cv2.moveWindow('myCam1',900,0)
	
    k = cv2.waitKey(1)
    
    if cv2.waitKey(1) == ord('q'):    # If q is hit, the window will close
        print("Close")
        break

    else: 
        voiceEncode.start()
        image_file = '/home/lian/Desktop/pyPro/images/known/{}.jpg'.format(unknown_Names)
        cv2.imwrite(image_file, frame1)
        break
        
cam1.release()
cv2.destroyAllWindows()   

threads = []
for root, dirs, files in os.walk(image_dir):
    t = threading.Thread(target=trainName)
    t.start()
    threads.append(t)

for thread in theads:
    thread.join()
