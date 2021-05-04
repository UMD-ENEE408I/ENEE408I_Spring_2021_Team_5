from flask import Flask, request
from flask_ask import Ask, statement, question
import time
import serial
import threading
import take_picture4
import face11
import face12
app = Flask(__name__)
ask = Ask(app, '/')

ser = serial.Serial('/dev/ttyUSB0')

def take_Pic():
    time.sleep(3)
    take_picture4.selfie()
    #print(take_Pic)
    
def knownGreeting():
    face11.known_Greeting()
    
def unknownGreeting():
    face12.unknown_Greeting()

@ask.launch
def test_skill():
    msg = 'Hi Lian, Bibbadi bibbadi boo'
    return statement(msg)

@ask.intent('Wander')
def wander():
    ser.write(b'w')
    speech_text = 'Wandering'
    return statement(speech_text).simple_card('My Robot', speech_text)

@ask.intent('Forward')
def go_forward():
    ser.write(b'f')
    speech_text = 'Going forward'
    return statement(speech_text).simple_card('My Robot', speech_text)

@ask.intent('Backward')
def go_forward():
    ser.write(b'b')
    speech_text = 'Going backward'
    return statement(speech_text).simple_card('My Robot', speech_text)

@ask.intent('Halt')
def stop():
    ser.write(b's')
    speech_text = 'Stopping!'
    return statement(speech_text).simple_card('My Robot', speech_text)
   
@ask.intent('Picture')
def take_a_picture():
    speech_text = 'Please say your name'
    snap_pic = threading.Thread(target=take_Pic)
    
    snap_pic.start()
    
    return statement(speech_text).simple_card('My Robot', speech_text)
    
@ask.intent('Greeting')
def greet_Known():
    kgreet = threading.Thread(target=knownGreeting)
    kgreet.start()
    speech_text = 'Hello {}, it is my pleasure to meet you'.format(name1)
    return statement(speech_text).simple_card('My Robot', speech_text)
    
@ask.intent('Finding')
def greet_unKnown():
    ugreet = threading.Thread(target=unknownGreeting)
    ugreet.start()
    speech_text = 'Hello! Can I take a picture of you?'
    return question(speech_text).simple_card('My Robot', speech_text)
    
@ask.intent('YesIntent')
def yes_Intent():
    speech_text = 'Please say your name and please get closer to the camera for clear picture'
    snap_pic = threading.Thread(target=take_Pic)
    snap_pic.start()
    return statement(speech_text).simple_card('My Robot', speech_text)
    
@ask.intent('NoIntent')
def no_Intent():
    speech_text = 'Thank you for your answer. It is my pleasure to talk with you. See you around'
    
    return statement(speech_text).simple_card('My Robot', speech_text)
    

if __name__ == '__main__':
    app.run(port=8005, debug=True)
