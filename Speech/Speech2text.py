import speech_recognition as sr

def speech_recog():
    r = sr.Recognizer()
    mic = sr.Microphone()
    while True:
        with mic as source: #mic is set as source, data comes in to mic object
            print("Speak............")
            audio = r.listen(source) #store the data into audio

            try: #sometimes voice maynot be detectd
                text = r.recognize_google(audio)#we are using google api
                print("You said:",text)
            except sr.UnknownValueError:
                print("Didn't hear any thing, please repeat")

speech_recog()


