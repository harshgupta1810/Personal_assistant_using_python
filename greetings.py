import shutil
import sys
import Voice
import datetime
import command
from Voice import speak


sys.path.append(0, '/Users/mittal/PycharmProjects/pythonsoftwere/python_assistant')

def wishMe():
    speak('Hey')
    hour = int(datetime.datetime.now().hour)
    if hour >= 0  and  hour < 12 :
        speak('Good morning!!!')

    elif hour >= 12  and  hour < 18 :
        speak('good afternoon!!!')

    else:
        speak('good evening!!')
    assname = ("neesan 1 point o")
    speak('you are using Neesaan, how may i help you')

def username():
    speak("What should i call you sir")
    uname = command.takeCommand()
    speak("Welcome Mister")
    speak(uname)

    query = shutil.get_terminal_size().command

    print("#####################".center(query))
    print("Welcome", uname.center(query))
    print("#####################".center(query))

    speak("How can i Help you, Sir")