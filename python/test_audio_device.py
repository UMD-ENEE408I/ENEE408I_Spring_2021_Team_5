import speech_recognition as sr
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Names: \"{0}\" found for'Microphone(device_index={1})'".format(index, name))
