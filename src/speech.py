import pyttsx3

engine = pyttsx3.init()

txt = input("Type something: ")

voices = engine.getProperty("voices")

engine.setProperty("rate",150)
engine.setProperty("voice", voices[1].id)
engine.say(txt)
engine.runAndWait()
engine.stop()