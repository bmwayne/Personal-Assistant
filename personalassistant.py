import wolframalpha
import wikipedia
from tkinter import *
import speech_recognition as sr

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
            else:
                window = Tk()
                window.geometry('600x600')

                try:
                    wolfid = 'Enter your API here'
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