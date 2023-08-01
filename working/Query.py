import ctypes
import datetime
import os
import random
import webbrowser
import bs4
import poetpy
import pyautogui
import pyjokes
import pywhatkit
import winshell
import wolframalpha
import requests
import email
import sys
import wikipedia
import time
from speedtest import Speedtest
from geopy.geocoders import Nominatim
from geopy import distance
from quote import quote
from urllib.request import urlopen
from python_assistant.Main import Voice, greetings, command
from forex_python.converter import CurrencyRates
from ecapture import ecapture as ec

sys.path.append(0, '/Users/mittal/PycharmProjects/pythonsoftwere/python_assistant')



def wiki() :
    Voice.Voice.Voice.Voice.Voice.Voice.Voice.speak('Searching Wikipedia...')
    query = command.query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    Voice.speak("According to Wikipedia")
    print(results)
    Voice.speak(results)
    time.sleep(3)
    sys.stdout.flush()

def openyoutube() :
    webbrowser.open("youtube.com")
    time.sleep(3)
    sys.stdout.flush()

def playyoutube() :
    try:
        query = command.query.replace("play", "")
        Voice.speak("Playing " + query)
        print("Playing " + query)
        pywhatkit.playonyt(query)
        time.sleep(3)
        sys.stdout.flush()

    except Exception as e:
        Voice.speak('please try again')
        print('please try again')
        time.sleep(3)
        sys.stdout.flush()

def opengoogle() :
    webbrowser.open("google.com")
    time.sleep(3)
    sys.stdout.flush()

def searchgoogle() :
    try:
        Voice.speak("Searching for" + command.query)
        info = pywhatkit.search(command.query, 1)
        Voice.speak(info)
        print(info)
        time.sleep(3)
        sys.stdout.flush()

    except Exception as e:
        Voice.speak('please try again')
        print('please try again')
        time.sleep(3)
        sys.stdout.flush()

def stack() :
    webbrowser.open("stackoverflow.com")
    time.sleep(3)
    sys.stdout.flush()

def music() :
    music_dir = 'E:\\songs\\Favorite Songs'
    songs = os.listdir(music_dir)
    print(songs)
    a = random.randint(0, (len(songs) - 1))
    os.startfile(os.path.join(music_dir, songs[a]))
    print(f'Playing {songs[a]}')
    Voice.speak(f'playing {songs[a]}')
    time.sleep(3)
    sys.stdout.flush()

def nextsong():
    os.startfile(os.path.join(music.music_dir, music.songs[music.a]))
    print(f'Playing next song  {music.songs[music.a]}')
    Voice.speak(f'playing next song  {music.songs[music.a]}')
    time.sleep(3)
    sys.stdout.flush()

def Time() :
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    Voice.speak(f"the time is {strTime}")
    print(f"The time is {strTime}")
    time.sleep(3)
    sys.stdout.flush()

def vsc() :
    codePath = r"C:\Users\mittal\AppData\Local\Programs\Microsoft VS Code\Code.exe"
    Voice.speak('opening Visual sudio code for you')
    print('Opening Visual Sudio Code for you')
    Voice.speak('wait a seconds it may takes time ')
    print('Wait a seconds it may takes time ')
    os.startfile(codePath)
    sys.stdout.flush()

def pycharm() :
    codePath = r"C:\Program Files\JetBrains\PyCharm 2021.1.3\bin\pycharm34.exe"
    Voice.speak('opening pycharm for you')
    print('Opening Pycharm for you')
    Voice.speak('wait a seconds it may takes time ')
    print('Wait a seconds it may takes time ')
    os.startfile(codePath)
    sys.stdout.flush()

def email() :
    try:
        Voice.speak("What should I say?")
        content = command.takeCommand()
        Voice.speak('enter mail id ')
        to = input('enter Mail id : ')
        email.sendEmail(to, content)
        Voice.speak("Email has been sent!")
        print("Email has been sent!")
        time.sleep(3)
        sys.stdout.flush()
    except Exception as e:
        print(e)
        Voice.speak("Sorry, I am not able to send this email")
        time.sleep(3)
        sys.stdout.flush()

def how_are_u() :
    Voice.speak("I am fine, Thank you")
    print("I am fine, Thank you")
    Voice.speak("How are you, Sir")
    print("How are you, Sir")
    time.sleep(3)
    sys.stdout.flush()

def fine() :
    Voice.speak("It's good to know that your fine")
    print("It's good to know that your fine")
    time.sleep(3)
    sys.stdout.flush()

def changename() :
    query = command.query.replace("change my name to", "")
    assname = query
    time.sleep(3)
    sys.stdout.flush()

def changed() :
    Voice.speak("What would you like to call me, Sir ")
    print("What would you like to call me, Sir ")
    assname = command.takeCommand()
    Voice.speak("Thanks for naming me")
    print("Thanks for naming me")
    time.sleep(3)
    sys.stdout.flush()

def yourname() :
    Voice.speak("My friends call me")
    Voice.speak(greetings.assname)
    print("My friends call me", greetings.assname)
    time.sleep(3)
    sys.stdout.flush()

def quit() :
    Voice.speak("Thanks for giving me your time")
    print("Thanks for giving me your time")

    sys.stdout.flush()
    exit()

def whomade() :
    Voice.speak("I have been created by Harsh.")
    print("I have been created by Harsh.")
    time.sleep(3)
    sys.stdout.flush()

def joke() :
    Voice.speak(pyjokes.get_joke())
    print(pyjokes.get_joke())
    time.sleep(3)
    sys.stdout.flush()

def calculate() :
    app_id = "4XV73X-JKG5Q9YHY7"
    client = wolframalpha.Client(app_id)
    indx = command.query.lower().split().index('calculate')
    query = command.query.split()[indx + 1:]
    res = client.query(' '.join(query))
    answer = next(res.results).text
    print("The answer is " + answer)
    Voice.speak("The answer is " + answer)
    time.sleep(3)
    sys.stdout.flush()

def whoim() :
    Voice.speak("If you talk then definitely your human.")
    print("If you talk then definitely your human.")
    time.sleep(3)
    sys.stdout.flush()

def whyucum() :
    Voice.speak("Thanks to Harsh. further It's a secret")
    print("Thanks to Harsh. further It's a secret")
    time.sleep(3)
    sys.stdout.flush()

def whoru() :
    Voice.speak("I am your virtual assistant created by Harsh")
    print("I am your virtual assistant created by Harsh")
    time.sleep(3)
    sys.stdout.flush()

def background() :
    ctypes.windll.user32.SystemParametersInfoW(20, 0, "Location of wallpaper", 0)
    Voice.speak("Background changed successfully")
    print("Background changed successfully")
    sys.stdout.flush()

def news() :
    url = "https://news.google.com/news/rss"
    client = urlopen(url)
    xml_page = client.read()
    client.close()
    page = bs4.BeautifulSoup(xml_page, 'lxml')
    news_list = page.findAll("item")
    Voice.speak("Today's top headlines are--")
    try:
        for news in news_list:
            print(news.title.text)
            print(news.pubDate.text)
            Voice.speak(f"{news.title.text}")
            Voice.speak(f"{news.pubDate.text}")
            print()

    except Exception as e:
        pass
    time.sleep(3)

def camera() :
    ec.capture(0, "USB camera", "img.jpg")

def answere() :
    Voice.speak('I can answer to computational and geographical questions  and what question do you want to ask now')
    question = command.takeCommand()
    app_id = " 4XV73X-JKG5Q9YHY7 "
    client = wolframalpha.Client(app_id)  # bug
    res = client.query(question)
    answer = next(res.results).text
    Voice.speak(answer)
    print(answer)

def weather() :
    try:
        Voice.speak("Tell me the city name.")
        city = command.takeCommand()
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
        Voice.speak(f"Gathering the weather information of {city}...")
        print(f"Gathering the weather information of {city}...")
        print(all_data1)
        Voice.speak(all_data1)
        print(all_data2)
        Voice.speak(all_data2)
        time.sleep(3)
        sys.stdout.flush()

    except Exception as e:
        pass

def cu() :
    webbrowser.open("uims.cuchd.in/uims/")  # BUG

def blackboard() :
    webbrowser.open("cuchd.blackboard.com")
    time.sleep(3)
    sys.stdout.flush()

def date() :
    strDate = datetime.datetime.today().strftime('%Y-%m-%d')
    print(strDate)
    Voice.speak(f"The date is {strDate}")
    time.sleep(3)
    sys.stdout.flush()

def poem() :
    Voice.speak('Poem of which author you want to listen?')
    auth = command.takeCommand()
    poem = poetpy.get_poetry('author', auth, 'title,linecount')
    poems = poetpy.get_poetry('author', auth, 'lines')
    poem_len = len(poem)
    poem_no = random.randint(1, poem_len)
    print("Title- ", poem[poem_no]['title'])
    Voice.speak(f"Title- {poem[poem_no]['title']}")  # BUG
    print("No. of lines-", poem[poem_no]['linecount'])
    Voice.speak(f"No. of lines- {poem[poem_no]['linecount']}")
    poem_str = '\n'
    print("Poem-\n", poem_str.join(poems[poem_no]['4']))
    Voice.speak(f"Poem-\n {poem_str.join(poems[poem_no]['4'])}")
    time.sleep(3)
    sys.stdout.flush()

def pause() :
    pyautogui.press("playpause")

def privious():
    pyautogui.press("prevtrack")

def next() :
    pyautogui.press("nexttrack")

def currency() :
    try:
        curr_list = {
            'dollar': 'USD', 'taka': 'BDT', 'dinar': 'BHD',
            'rupee': 'INR', 'afghani': 'AFN', 'real': 'BRL',
            'yen': 'JPY', 'peso': 'ARS', 'pound': 'EGP', 'rial': 'OMR',
            'lek': 'ALL', 'kwanza': 'AOA', 'manat': 'AZN', 'franc': 'CHF'
        }

        cur = CurrencyRates()
        # print(cur.get_rate('USD', 'INR'))
        Voice.speak('From which currency u want to convert?')
        from_cur = command.takeCommand()
        src_cur = curr_list[from_cur.lower()]
        Voice.speak('To which currency u want to convert?')
        to_cur = command.takeCommand()
        dest_cur = curr_list[to_cur.lower()]
        Voice.speak('Tell me the value of currency u want to convert.')
        val_cur = float(command.takeCommand())
        print(cur.convert(src_cur, dest_cur, val_cur))

    except Exception as e:
        print("Couldn't get what you have said, Can you say it again??")
        Voice.speak("Couldn't get what you have said, Can you say it again??")

def quete() :
    Voice.speak("Tell me the author or person name.")
    q_author = command.takeCommand()
    quotes = quote(q_author)
    quote_no = random.randint(1, len(quotes))
    print("Author: ", quotes[quote_no]['author'])
    print("-->", quotes[quote_no]['quote'])
    Voice.speak(f"Author: {quotes[quote_no]['author']}")
    Voice.speak(f"He said {quotes[quote_no]['quote']}")
    time.sleep(3)
    sys.stdout.flush()

def what() :
    client = wolframalpha.Client("4XV73X-JKG5Q9YHY7")
    res = client.query(command.query)
    try:
        print(next(res.results).text)
        Voice.speak(next(res.results).text)

    except StopIteration:
        print("No results found!!")
    time.sleep(3)
    sys.stdout.flush()

def recyclebin() :
    try:
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
        print("Recycle Bin is cleaned successfully.")
        Voice.speak("Recycle Bin is cleaned successfully.")

    except Exception as e:
        print("Recycle bin is already Empty.")
        Voice.speak("Recycle bin is already Empty.")
    time.sleep(3)
    sys.stdout.flush()

def makenote() :
    Voice.speak("What should I write, sir??")
    note = command.takeCommand()
    file = open('Notes.txt', 'a')
    Voice.speak("Should I include the date and time??")
    n_conf = command.takeCommand()
    if 'yes' in n_conf:
        str_time = datetime.datetime.now().strftime("%H:%M:%S")
        file.write(str_time)
        file.write(" --> ")
        file.write(note)
        Voice.speak("Point noted successfully.")
    else:
        file.write("\n")
        file.write(note)
        Voice.speak("Point noted successfully.")
    time.sleep(3)
    sys.stdout.flush()

def readnote() :
    Voice.speak("Reading Notes")
    file = open("Notes.txt", "r")
    data_note = file.readlines()
    print(data_note)
    Voice.speak(data_note)
    time.sleep(3)
    sys.stdout.flush()

def distance() :
    geocoder = Nominatim(user_agent="gupta")
    Voice.speak("Tell me the first city name??")
    location1 = command.takeCommand()
    Voice.speak("Tell me the second city name??")
    location2 = command.takeCommand()
    coordinates1 = geocoder.geocode(location1)
    coordinates2 = geocoder.geocode(location2)
    lat1, long1 = coordinates1.latitude, coordinates1.longitude
    lat2, long2 = coordinates2.latitude, coordinates2.longitude
    place1 = (lat1, long1)
    place2 = (lat2, long2)
    distance_places = distance.distance(place1, place2)
    print(f"The distance between {location1} and {location2} is {distance_places}.")
    Voice.speak(f"The distance between {location1} and {location2} is {distance_places}")
    time.sleep(3)
    sys.stdout.flush()

def ss() :
    sc = pyautogui.screenshot()
    sc.save('pa_ss.png')
    print("Screenshot taken successfully.")
    Voice.speak("Screenshot taken successfully.")
    time.sleep(3)
    sys.stdout.flush()

def vup() :
    pyautogui.press("volumeup")
    time.sleep(3)
    sys.stdout.flush()

def vdown() :
    pyautogui.press("volumedown")
    time.sleep(3)
    sys.stdout.flush()

def mute() :
    pyautogui.press("volumemute")
    time.sleep(3)
    sys.stdout.flush()

def internet() :
    st = Speedtest()
    print("Wait!! I am checking your Internet Speed...")
    Voice.speak("Wait!! I am checking your Internet Speed...")
    dw_speed = st.download()
    up_speed = st.upload()
    dw_speed = dw_speed / 1000000
    up_speed = up_speed / 1000000
    print('Your download speed is', round(dw_speed, 3), 'Mbps')
    print('Your upload speed is', round(up_speed, 3), 'Mbps')
    Voice.speak(f'Your download speed is {round(dw_speed, 3)} Mbps')
    Voice.speak(f'Your upload speed is {round(up_speed, 3)} Mbps')
    time.sleep(3)
    sys.stdout.flush()

def e() :
    try:
        query = command.query.replace("search", "")  # BUG
        query = query.replace("play", "")
        webbrowser.open(query)
        time.sleep(3)
        sys.stdout.flush()
    except Exception as e:
        Voice.speak('data insuficent')
        print('data insuficent')