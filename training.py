
import face_recognition
import cv2
print(cv2.__version__)
import os
import pickle

Encodings = []
Names = []
image_dir = '/home/lian/Desktop/pyPro/images/known'
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
        
