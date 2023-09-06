import pyttsx3
txt_sp = pyttsx3.init() #init class

txt = input("Enter the text toconvert..........\n")
txt_sp.say(txt)
txt_sp.runAndWait() #to run and wait
