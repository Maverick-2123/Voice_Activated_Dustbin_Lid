r = sr.Recognizer()


# def speak_text(command):
#     eng = pyttsx3.init()
#     eng.say(command)
#     eng.runAndWait()

# with sr.Microphone() as source2:
#     r.adjust_for_ambient_noise(source2,duration=0.2)
#     audio = r.listen(source2)

#     my_command = r.recognize_google(audio)
#     my_command = my_command.lower()

#     print(my_command)

#     speak_text(my_command)