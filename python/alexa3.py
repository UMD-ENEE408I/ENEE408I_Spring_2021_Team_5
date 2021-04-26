from flask import Flask, request
from flask_ask import Ask, statement
import time
import serial
import threading
import take_picture4
app = Flask(__name__)
ask = Ask(app, '/')

ser = serial.Serial('/dev/ttyUSB0')

def take_Pic():
    time.sleep(1)
    take_picture4.selfie()
    #print(take_Pic)

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
    return statement(speech_text)#.simple_card('My Robot', speech_text)

@ask.intent('Backward')
def go_forward():
    ser.write(b'b')
    speech_text = 'Going backward'
    return statement(speech_text).simple_card('My Robot', speech_text)

@ask.intent('Stop')
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
    

if __name__ == '__main__':
    app.run(port=8005, debug=True)
