import os
import pyttsx3
import datetime
import wikipedia

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

print("JARVIS AI Assistant Started")

while True:
    command = input("You : ").lower()

    if "hello" in command:
        speak("Hello Sir")

    elif "time" in command:
        time = datetime.datetime.now().strftime("%H:%M")
        speak("The time is " + time)

    elif "who is" in command:
        name = command.replace("who is","")
        info = wikipedia.summary(name,1)
        print(info)
        speak(info)

    elif "exit" in command:
        speak("Goodbye")
        break

    else:
        speak("I don't understand")
