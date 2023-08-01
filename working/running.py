import os
import sys
import Query
from python_assistant.Main import Voice, greetings, command

sys.path.append(0, '/Users/mittal/PycharmProjects/pythonsoftwere/python_assistant')

def run():
    while True:
        query = command.takeCommand().lower()

        if 'wikipedia' in query:
            Query.wiki()

        elif 'open youtube' in query:
            Query.openyoutube()
            if "play on youtube" or "search on youtube" or 'on youtube' in query:
                Query.playyoutube()

        elif 'open google' in query:
            Query.opengoogle()
            if ('search on google' in query) or ('search' in query):
                Query.searchgoogle()

        elif 'open stackoverflow' in query:
            Query.stack()

        elif 'music' in query:
            Query.music()
            if 'next song' in query:
                Query.nextsong()

        elif ('the time' in query) or ('time' in query):
            Query.Time()

        elif 'open vsc' in query:
            Query.vsc()

        elif 'open pycharm' in query:
            Query.pycharm()

        elif ' send email to ' in query:
           Query.email()

        elif 'how are you' in query:
            Query.how_are_u()

        elif ('fine' in query) or ("good" in query):
            Query.fine()

        elif "change my name to" in query:
            Query.changename()

        elif "change name" in query:
            Query.changed()

        elif ("what's your name" in query) or ("What is your name" in query):
            Query.yourname()

        elif ('exit' in query) or ('quit' in query) or ('bye' in query):
            Query.quit()

        elif ("who made you" in query) or ("who created you" in query):
            Query.whomade()

        elif 'joke' in query:
            Query.joke()

        elif "calculate" in query:
            Query.calculate()


        elif "who i am" in query:
            Query.whoim()

        elif "why you came to world" in query:
            Query.whyucum()

        elif "who are you" in query:
            Query.whoru()

        elif 'change background' in query:
            Query.background()

        elif 'news' in query:  # BUG
            Query.news()

        elif ("camera" in query) or ("take a photo" in query):
           Query.camera()  # bug

        elif 'answer' in query:
            Query.answere()

        elif 'weather' in query or 'temperature' in query:
            Query.weather()

        elif 'open cu login' in query:
            Query.cu()

        elif 'open blackboard' in query:
            Query.background()

        elif ('the date' in query) or ('date' in query):
            Query.date()

        elif 'poem' in query:
            Query.poem()

        elif 'resume' in query or 'pause' in query:
            Query.pause()

        elif 'previous' in query:
            Query.privious()

        elif 'next' in query:
            Query.next()

        elif 'convert currency' in query:
            Query.currency()

        elif ('quote' in query) or ('quotes' in query):
            Query.quete()

        elif ('what' in query) or ('who' in query) or ('where' in query):
            Query.what()

        elif ('empty recycle bin' in query) or ('clear recycle bin' in query):
            Query.recyclebin()

        elif ('write a note' in query) or ('make a note' in query):
            Query.makenote()

        elif ('show me the notes' in query) or ('read notes' in query):
            Query.readnote()

        elif 'distance' in query:
            Query.distance()

        elif 'screenshot' in query:
            Query.ss()

        elif 'volume up' in query:
            Query.vup()

        elif 'volume down' in query:
            Query.vdown()

        elif 'mute volume' in query:
            Query.mute()


        elif 'internet speed' in query:
            Query.internet()

        else:
            Query.e()