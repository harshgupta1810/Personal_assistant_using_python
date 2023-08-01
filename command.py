import sys

import Voice
import speech_recognition as sr



sys.path.append(0, '/Users/mittal/PycharmProjects/pythonsoftwere/python_assistant')

def takeCommand():
    r = sr.Recognizer()
    query=''
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Unable to Recognize your voice.")
        Voice.speak('Unable to Recognize your voice.')
        print('please say it again')
        Voice.speak('please say it again')
        return "None"
    return query