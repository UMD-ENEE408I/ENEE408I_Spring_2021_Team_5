from flask import Flask
from flask_ask import Ask, statement
import time
import serial

app = Flask(__name__)
ask = Ask(app, '/')

ser = serial.Serial('/dev/ttyUSB0')

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

@ask.intent('Stop')
def stop():
    ser.write(b's')
    speech_text = 'Stopping!'
    return statement(speech_text).simple_card('My Robot', speech_text)

@ask.intent('Picture')
def take_a_picture():
    speech_text = 'Enter your name and type enter. Your picture will take in 6 seconds'
    import take_picture
    return statement(speech_text).simple_card('My Robot', speech_text)

if __name__ == '__main__':
    app.run()
