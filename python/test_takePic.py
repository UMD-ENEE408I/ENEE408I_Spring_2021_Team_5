
import cv2
print(cv2.__version__)

import speech_recognition as sr
import pyaudio
import threading
import time

class FrameGrabber(threading.Thread):
    def __init__(self, cam):
        threading.Thread.__init__(self)
        self._cam = cam
        self._frame = None
        self._stop_thread = False

    def run(self):
        while not self._stop_thread:
            _, self._frame = self._cam.read()
        self._cam.release()

    # If your program runs faster than the framerate of the
    # camera this will return duplicate frames
    def get_latest_frame(self):
        return self._frame

    def signal_stop(self):
        self._stop_thread = True

width = 720
height = 480
flip = 0
    
try:

    camSet1 = 'nvarguscamerasrc sensor-id=0 ee-mode=2 ee-strength=0 tnr-mode=2 tnr-strength=1 wbmode=3 ! video/x-raw(memory:NVMM), width=3264, height=2464, framerate=21/1,format=NV12 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(width)+', height='+str(height)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! videobalance contrast=1.5 saturation=1.2 ! appsink drop=True'	
    cam1 = cv2.VideoCapture(camSet1)
    frame_grabber = FrameGrabber(cam1)
    
    frame_grabber.start()
    '''
    while frame_grabber.get_latest_frame() is None:
        time.sleep(0.1)
    '''
    #print(frame_grabber.get_latest_frame())
except Exception as e:
    print(e)
    frame_grabber.signal_stop()
    frame_grabber.join()



def selfie():

    while True:
        frame1 = frame_grabber.get_latest_frame()
        print(frame1)
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
                audio = r.listen(source)
                #audio = r.listen(source, phrase_time_limit=3)
    
                try:
                    unknown_Names = r.recognize_google(audio)
                    print('You said: {}'.format(unknown_Names))
                    #time.sleep(3)
                    image_file = '/home/lian/Desktop/pyPro/images/known/{}.jpg'.format(unknown_Names)
                    cv2.imwrite(image_file, frame1)
                except:
                    print("Try again")      
            break
    print('line 50')
    cam1.release()
    cv2.destroyAllWindows() 

      
