import face_recognition
import os
import time
import pickle
import threading
import concurrent.futures

Encodings = []
Names = []
image_dir = '/home/lian/Desktop/pyPro/images/known'


def trainName():
    def record_images(file):
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
        
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(record_images, files)


threads = []
for root, dirs, files in os.walk(image_dir):
    t = threading.Thread(target=trainName)
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()
