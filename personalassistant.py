import wolframalpha
import wikipedia
import tkinter
import speech_recognition as sr

while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            if text == 'stop':
                print('Thank you using my Personal Assistant')
