import speech_recognition as sr
import pyaudio
import pyttsx3
from playsound import playsound
from time import sleep

r = sr.Recognizer()

def speak_text(command):
    if ("ओपन" in command or "खुल" in command or "खोलो" in command):
        print("Lid Opening")
        playsound("door.wav")
        sleep(3)
        print("Closing Lid")
        playsound("door_close.wav")
    else:
        pass

def read():
    with sr.Microphone() as source2:
        try:
            print("Start Speaking....")
            r.adjust_for_ambient_noise(source2,duration=0.2)
            audio = r.listen(source2)
            my_command = r.recognize_google(audio,language="hi-In")
            my_command = my_command.lower()
            speak_text(my_command)
        except:
            print("I couldn't catch that")
            read()
    #stopper = r.listen_in_background(sr,speak_text)

read()