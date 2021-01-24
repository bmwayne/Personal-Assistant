import wolframalpha
import wikipedia
import tkinter
import speech_recognition as sr

while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)