
import speech_recognition as sr
import pyaudio

r = sr.Recognizer()
with sr.Microphone() as source:

    print('Enter Your Speech:')
    r.adjust_for_ambient_noise(source, duration = 0.1)
    #r.adjust_for_ambient_noise(source)
    #audio = r.listen(source)
    audio = r.listen(source, phrase_time_limit=3)
    
    try:
        unknown_Names = r.recognize_google(audio)
        print('You said: {}'.format(unknown_Names))

    except:
        print('Try again')

