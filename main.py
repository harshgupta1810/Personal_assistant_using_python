import smtplib
import bs4
import pyttsx3
from pywikihow import search_wikihow
import pyautogui
import poetpy
from forex_python.converter import CurrencyRates
import winshell as winshell
from geopy.geocoders import Nominatim
from geopy import distance
import datetime
import pywhatkit
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import subprocess
import wolframalpha
import tkinter
import json
import operator
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
from tkinter import _tkinter
from tkinter import *
from PIL import ImageTk, Image
from twilio.rest import Client
from clint.textui import progress
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
import sys
from speedtest import Speedtest
from ecapture import ecapture as ec

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    speak('Hey')
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good morning!!!')

    elif hour >= 12 and hour < 18:
        speak('good afternoon!!!')

    else:
        speak('good evening!!')
    assname = ("neesan 1 point o")
    speak('you are using Neesaan, how may i help you')


def username():
    speak("What should i call you sir")
    uname = takeCommand()
    speak("Welcome Mister")
    speak(uname)

    query = shutil.get_terminal_size().command

    print("#####################".center(query))
    print("Welcome", uname.center(query))
    print("#####################".center(query))

    speak("How can i Help you, Sir")


def takeCommand():
    r = sr.Recognizer()
    query = ''
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
        speak('Unable to Recognize your voice.')
        print('please say it again')
        speak('please say it again')
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('desperateenuf52@gmail.com', '1810@harsh')
    server.sendmail('desperateenuf52@gmail.com', to, content)
    server.close()


if __name__ == '__main__':
    clear = lambda: os.system('cls')
    clear()
    wishMe()
    username()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            time.sleep(3)
            sys.stdout.flush()

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            time.sleep(3)
            sys.stdout.flush()
            if "play on youtube" or "search on youtube" or 'on youtube' in query:
                try:
                    query = query.replace("play", "")
                    speak("Playing " + query)
                    print("Playing " + query)
                    pywhatkit.playonyt(query)
                    time.sleep(3)
                    sys.stdout.flush()

                except Exception as e:
                    speak('please try again')
                    print('please try again')
                    time.sleep(3)
                    sys.stdout.flush()

        elif 'open google' in query:
            webbrowser.open("google.com")
            time.sleep(3)
            sys.stdout.flush()
            if ('search on google' in query) or ('search' in query):
                try:
                    speak("Searching for" + query)
                    info = pywhatkit.search(query, 1)
                    speak(info)
                    print(info)
                    time.sleep(3)
                    sys.stdout.flush()

                except Exception as e:
                    speak('please try again')
                    print('please try again')
                    time.sleep(3)
                    sys.stdout.flush()

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            time.sleep(3)
            sys.stdout.flush()

        elif 'music' in query:
            music_dir = 'E:\\songs\\Favorite Songs'
            songs = os.listdir(music_dir)
            print(songs)
            a = random.randint(0, (len(songs) - 1))
            os.startfile(os.path.join(music_dir, songs[a]))
            print(f'Playing {songs[a]}')
            speak(f'playing {songs[a]}')
            time.sleep(3)
            sys.stdout.flush()
            if 'next song' in query:
                os.startfile(os.path.join(music_dir, songs[a]))
                print(f'Playing next song  {songs[a]}')
                speak(f'playing next song  {songs[a]}')
                time.sleep(3)
                sys.stdout.flush()

        elif ('the time' in query) or ('time' in query):
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
            print(f"The time is {strTime}")
            time.sleep(3)
            sys.stdout.flush()

        elif 'open vsc' in query:
            codePath = r"C:\Users\mittal\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            speak('opening Visual sudio code for you')
            print('Opening Visual Sudio Code for you')
            speak('wait a seconds it may takes time ')
            print('Wait a seconds it may takes time ')
            os.startfile(codePath)
            sys.stdout.flush()

        elif 'open pycharm' in query:
            codePath = r"C:\Program Files\JetBrains\PyCharm 2021.1.3\bin\pycharm34.exe"
            speak('opening pycharm for you')
            print('Opening Pycharm for you')
            speak('wait a seconds it may takes time ')
            print('Wait a seconds it may takes time ')
            os.startfile(codePath)
            sys.stdout.flush()

        elif ' send email to ' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak('enter mail id ')
                to = input('enter Mail id : ')
                sendEmail(to, content)
                speak("Email has been sent!")
                print("Email has been sent!")
                time.sleep(3)
                sys.stdout.flush()
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to send this email")
                time.sleep(3)
                sys.stdout.flush()

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            print("I am fine, Thank you")
            speak("How are you, Sir")
            print("How are you, Sir")
            time.sleep(3)
            sys.stdout.flush()

        elif ('fine' in query) or ("good" in query):
            speak("It's good to know that your fine")
            print("It's good to know that your fine")
            time.sleep(3)
            sys.stdout.flush()

        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            assname = query
            time.sleep(3)
            sys.stdout.flush()

        elif "change name" in query:
            speak("What would you like to call me, Sir ")
            print("What would you like to call me, Sir ")
            assname = takeCommand()
            speak("Thanks for naming me")
            print("Thanks for naming me")
            time.sleep(3)
            sys.stdout.flush()

        elif ("what's your name" in query) or ("What is your name" in query):
            speak("My friends call me")
            speak(assname)
            print("My friends call me", assname)
            time.sleep(3)
            sys.stdout.flush()

        elif ('exit' in query) or ('quit' in query) or ('bye' in query):
            speak("Thanks for giving me your time")
            print("Thanks for giving me your time")

            sys.stdout.flush()
            exit()

        elif ("who made you" in query) or ("who created you" in query):
            speak("I have been created by Harsh.")
            print("I have been created by Harsh.")
            time.sleep(3)
            sys.stdout.flush()

        elif 'joke' in query:
            speak(pyjokes.get_joke())
            print(pyjokes.get_joke())
            time.sleep(3)
            sys.stdout.flush()

        elif "calculate" in query:

            app_id = "4XV73X-JKG5Q9YHY7"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)
            time.sleep(3)
            sys.stdout.flush()


        elif "who i am" in query:
            speak("If you talk then definitely your human.")
            print("If you talk then definitely your human.")
            time.sleep(3)
            sys.stdout.flush()

        elif "why you came to world" in query:
            speak("Thanks to Harsh. further It's a secret")
            print("Thanks to Harsh. further It's a secret")
            time.sleep(3)
            sys.stdout.flush()

        elif "who are you" in query:
            speak("I am your virtual assistant created by Harsh")
            print("I am your virtual assistant created by Harsh")
            time.sleep(3)
            sys.stdout.flush()


        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, "Location of wallpaper", 0)
            speak("Background changed successfully")
            print("Background changed successfully")
            sys.stdout.flush()

        elif 'news' in query:  # BUG
            url = "https://news.google.com/news/rss"
            client = urlopen(url)
            xml_page = client.read()
            client.close()
            page = bs4.BeautifulSoup(lxml_page, 'lxml')
            news_list = page.findAll("item")
            speak("Today's top headlines are--")
            try:
                for news in news_list:
                    print(news.title.text)
                    print(news.pubDate.text)
                    speak(f"{news.title.text}")
                    speak(f"{news.pubDate.text}")
                    print()

            except Exception as e:
                pass
            time.sleep(3)

        elif ("camera" in query) or ("take a photo" in query):
            ec.capture(0, "USB camera", "img.jpg")  # bug

        elif 'answere' in query:
            speak('I can answer to computational and geographical questions  and what question do you want to ask now')
            question = takeCommand()
            app_id = " 4XV73X-JKG5Q9YHY7 "
            client = wolframalpha.Client(app_id)
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        elif 'weather' in query or 'temperature' in query:
            try:
                speak("Tell me the city name.")
                city = takeCommand()
                api = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=a5ceab259e0887e731c34493831cdf8d"
                w_data = requests.get(api).json()
                weather = w_data['weather'][0]['main']
                temp = int(w_data['main']['temp'] - 273.15)
                temp_min = int(w_data['main']['temp_min'] - 273.15)
                temp_max = int(w_data['main']['temp_max'] - 273.15)
                pressure = w_data['main']['pressure']
                humidity = w_data['main']['humidity']
                visibility = w_data['visibility']
                wind = w_data['wind']['speed']
                sunrise = time.strftime("%H:%M:%S", time.gmtime(w_data['sys']['sunrise'] + 19800))
                sunset = time.strftime("%H:%M:%S", time.gmtime(w_data['sys']['sunset'] + 19800))

                all_data1 = f"Condition: {weather} \nTemperature: {str(temp)}°C\n"
                all_data2 = f"Minimum Temperature: {str(temp_min)}°C \nMaximum Temperature: {str(temp_max)}°C \n" \
                            f"Pressure: {str(pressure)} millibar \nHumidity: {str(humidity)}% \n\n" \
                            f"Visibility: {str(visibility)} metres \nWind: {str(wind)} km/hr \nSunrise: {sunrise}  " \
                            f"\nSunset: {sunset}"
                speak(f"Gathering the weather information of {city}...")
                print(f"Gathering the weather information of {city}...")
                print(all_data1)
                speak(all_data1)
                print(all_data2)
                speak(all_data2)
                time.sleep(3)
                sys.stdout.flush()

            except Exception as e:
                pass

        elif 'open cu login' in query:
            webbrowser.open("uims.cuchd.in/uims/")  # BUG

        elif 'open blackboard' in query:
            webbrowser.open("cuchd.blackboard.com")
            time.sleep(3)
            sys.stdout.flush()

        elif ('the date' in query) or ('date' in query):
            strDate = datetime.datetime.today().strftime('%Y-%m-%d')
            print(strDate)
            speak(f"The date is {strDate}")
            time.sleep(3)
            sys.stdout.flush()

        elif 'poem' in query:
            speak('Poem of which author you want to listen?')
            auth = takeCommand()
            poem = poetpy.get_poetry('author', auth, 'title,linecount')
            poems = poetpy.get_poetry('author', auth, 'lines')
            poem_len = len(poem)
            poem_no = random.randint(1, poem_len)
            print("Title- ", poem[poem_no]['title'])
            speak(f"Title- {poem[poem_no]['title']}")  # BUG
            print("No. of lines-", poem[poem_no]['linecount'])
            speak(f"No. of lines- {poem[poem_no]['linecount']}")
            poem_str = '\n'
            print("Poem-\n", poem_str.join(poems[poem_no]['4']))
            speak(f"Poem-\n {poem_str.join(poems[poem_no]['4'])}")
            time.sleep(3)
            sys.stdout.flush()

        elif 'resume' in query or 'pause' in query:
            pyautogui.press("playpause")

        elif 'previous' in query:
            pyautogui.press("prevtrack")

        elif 'next' in query:
            pyautogui.press("nexttrack")

        elif 'convert currency' in query:
            try:
                curr_list = {
                    'dollar': 'USD', 'taka': 'BDT', 'dinar': 'BHD',
                    'rupee': 'INR', 'afghani': 'AFN', 'real': 'BRL',
                    'yen': 'JPY', 'peso': 'ARS', 'pound': 'EGP', 'rial': 'OMR',
                    'lek': 'ALL', 'kwanza': 'AOA', 'manat': 'AZN', 'franc': 'CHF'
                }

                cur = CurrencyRates()
                # print(cur.get_rate('USD', 'INR'))
                speak('From which currency u want to convert?')
                from_cur = takeCommand()
                src_cur = curr_list[from_cur.lower()]
                speak('To which currency u want to convert?')
                to_cur = takeCommand()
                dest_cur = curr_list[to_cur.lower()]
                speak('Tell me the value of currency u want to convert.')
                val_cur = float(takeCommand())
                print(cur.convert(src_cur, dest_cur, val_cur))

            except Exception as e:
                print("Couldn't get what you have said, Can you say it again??")
                speak("Couldn't get what you have said, Can you say it again??")

        elif ('quote' in query) or ('quotes' in query):
            speak("Tell me the author or person name.")
            q_author = takeCommand()
            quotes = quote(q_author)
            quote_no = random.randint(1, len(quotes))
            print("Author: ", quotes[quote_no]['author'])
            print("-->", quotes[quote_no]['quote'])
            speak(f"Author: {quotes[quote_no]['author']}")
            speak(f"He said {quotes[quote_no]['quote']}")
            time.sleep(3)
            sys.stdout.flush()

        elif ('what' in query) or ('who' in query) or ('where' in query):
            client = wolframalpha.Client("4XV73X-JKG5Q9YHY7")
            res = client.query(query)
            try:
                print(next(res.results).text)
                speak(next(res.results).text)

            except StopIteration:
                print("No results found!!")
            time.sleep(3)
            sys.stdout.flush()

        elif ('empty recycle bin' in query) or ('clear recycle bin' in query):
            try:
                winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
                print("Recycle Bin is cleaned successfully.")
                speak("Recycle Bin is cleaned successfully.")

            except Exception as e:
                print("Recycle bin is already Empty.")
                speak("Recycle bin is already Empty.")
            time.sleep(3)
            sys.stdout.flush()

        elif ('write a note' in query) or ('make a note' in query):
            speak("What should I write, sir??")
            note = takeCommand()
            file = open('Notes.txt', 'a')
            speak("Should I include the date and time??")
            n_conf = takeCommand()
            if 'yes' in n_conf:
                str_time = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(str_time)
                file.write(" --> ")
                file.write(note)
                speak("Point noted successfully.")
            else:
                file.write("\n")
                file.write(note)
                speak("Point noted successfully.")
            time.sleep(3)
            sys.stdout.flush()

        elif ('show me the notes' in query) or ('read notes' in query):
            speak("Reading Notes")
            file = open("Notes.txt", "r")
            data_note = file.readlines()
            print(data_note)
            speak(data_note)
            time.sleep(3)
            sys.stdout.flush()

        elif 'distance' in query:
            geocoder = Nominatim(user_agent="gupta")
            speak("Tell me the first city name??")
            location1 = takeCommand()
            speak("Tell me the second city name??")
            location2 = takeCommand()
            coordinates1 = geocoder.geocode(location1)
            coordinates2 = geocoder.geocode(location2)
            lat1, long1 = coordinates1.latitude, coordinates1.longitude
            lat2, long2 = coordinates2.latitude, coordinates2.longitude
            place1 = (lat1, long1)
            place2 = (lat2, long2)
            distance_places = distance.distance(place1, place2)
            print(f"The distance between {location1} and {location2} is {distance_places}.")
            speak(f"The distance between {location1} and {location2} is {distance_places}")
            time.sleep(3)
            sys.stdout.flush()

        elif 'screenshot' in query:
            sc = pyautogui.screenshot()
            sc.save('pa_ss.png')
            print("Screenshot taken successfully.")
            speak("Screenshot taken successfully.")
            time.sleep(3)
            sys.stdout.flush()

        elif 'volume up' in query:
            pyautogui.press("volumeup")
            time.sleep(3)
            sys.stdout.flush()

        elif 'volume down' in query:
            pyautogui.press("volumedown")
            time.sleep(3)
            sys.stdout.flush()

        elif 'mute volume' in query:
            pyautogui.press("volumemute")
            time.sleep(3)
            sys.stdout.flush()


        elif 'internet speed' in query:
            st = Speedtest()
            print("Wait!! I am checking your Internet Speed...")
            speak("Wait!! I am checking your Internet Speed...")
            dw_speed = st.download()
            up_speed = st.upload()
            dw_speed = dw_speed / 1000000
            up_speed = up_speed / 1000000
            print('Your download speed is', round(dw_speed, 3), 'Mbps')
            print('Your upload speed is', round(up_speed, 3), 'Mbps')
            speak(f'Your download speed is {round(dw_speed, 3)} Mbps')
            speak(f'Your upload speed is {round(up_speed, 3)} Mbps')
            time.sleep(3)
            sys.stdout.flush()



        else:
            try:
                query = query.replace("search", "")  # BUG
                query = query.replace("play", "")
                webbrowser.open(query)
                time.sleep(3)
                sys.stdout.flush()
            except Exception as e:
                speak('data insuficent')
                print('data insuficent')