import wolframalpha
import wikipedia
import speech_recognition as sr
import pyaudio
from tkinter import *
import tkinter.messagebox

wolfid = 'UY2U9Q-PKAY23Y5TJ'

while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)

