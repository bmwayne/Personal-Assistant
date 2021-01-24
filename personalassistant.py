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
            else:
                window = tkinter.Tk()
                window.geometry('600x600')
                try:
                    wolfid = 'UY2U9Q-PKAY23Y5TJ'
                    client = wolframalpha.Client(wolfid)
                    result = client.query(text)
                    answer = next(result.results).text

                    label = Label(window, justify = LEFT, compound = CENTER, padx = 10, text = answer, font = 'times 15 bold' )
                    label.pack()
                    tkinter.mainloop()
                except:
                    print('WolframAlpha could not find anything. Let\'s try Wikipedia!')
                    answer = wikipedia.summary(text)

                    label = Label(window, justify=LEFT, compound=CENTER, padx=10, text=answer, font='times 15 bold')
                    label.pack()
                    tkinter.mainloop()