# sudo pip3 install SpeechRecognition
# sudo apt-get install portaudio19-dev python-all-dev python3-all-dev && sudo pip3 install pyaudio

import speech_recognition as sr
import pyaudio
#ecognizer_instance.adjust_for_ambient_noise(source, duration = 1)
#index = pyaudio.PyAudio().get_device_index=24
r = sr.Recognizer()

with sr.Microphone() as source:

    print('Enter Your Speech:')
    r.adjust_for_ambient_noise(source, duration = 1)
    #r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    
    try:
        text = r.recognize_google(audio)
        print('You said: {}'.format(text))
    except:
        print('Try again')
