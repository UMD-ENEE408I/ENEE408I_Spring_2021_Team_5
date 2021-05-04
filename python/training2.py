import face_recognition
import os
import time
import pickle
import threading
import concurrent.futures

Encodings = []
Names = []
initial = os.getcwd()
image_dir = initial + "/Image"

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

        
