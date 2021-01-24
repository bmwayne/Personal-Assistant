import wolframalpha
import wikipedia
from tkinter import *
import speech_recognition as sr
import os

while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Say Something...')
        audio = r.listen(source)

        try:
            print('Recognizing...')
            text = r.recognize_google(audio)
            print(text)
            if text == 'stop':
                print('Thank you using my Personal Assistant')
                break
            elif text == 'opendota':
                os.startfile('dota2.bat')
            elif text == 'let\'s go to war':
                os.startfile('cod.bat')
            elif text == 'open Chrome':
                os.startfile('chrome.bat')
            elif text == 'open firefox':
                os.startfile('firefox.bat')
            else:
                window = Tk()
                window.geometry('600x600')

                try:
                    wolfid = 'UY2U9Q-PKAY23Y5TJ'
                    client = wolframalpha.Client(wolfid)
                    res = client.query(text)
                    answer = next(res.results).text
                    print('Viola! Got an answer from WolframAlpha')
                    print(answer)
                    label1 = Label(window, justify = LEFT, compound = CENTER, padx = 10, pady = 10, text = answer, font = 'times 15 bold',bg = 'yellow')
                    label1.place(x=100,y=100)
                    label1.pack()
                    window.after(5000, lambda :window.destroy())
                    window.mainloop()
                except Exception as e:
                    print('WolframAlpha could not find anything. Let\'s try Wikipedia!')
                    wikianswer = wikipedia.summary(text)

                    label1 = Label(window, justify=LEFT, compound=CENTER, padx=10, pady=10, text=wikianswer, font='times 15 bold',bg = 'yellow')
                    label1.place(x=100,y=100)
                    label1.pack()
                    window.after(50000, lambda: window.destroy())
                    window.mainloop()
        except Exception as e:
            answer = 'Sorry I zoned out.. What did you say again?'
            print(answer)