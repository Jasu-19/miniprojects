import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import datetime
import webbrowser
from newsapi import *
import pyautogui
from time import sleep
import psutil
import time as t
import requests
import newsapi
from pytube import YouTube


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()



def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def tellDay():
    day = datetime.datetime.today().weekday() + 1

    Day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}

    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        talk("The day is " + day_of_the_week)

#def Downloader():

    #url = YouTube(str.get().link)
    #video = url.streams.first()
    #video.download()

def sendWhatMsg():
    user_name = {
        'test': '+91 8309535383'
    }
    try:
        talk("To whom you want to send the message?")
        name = take_command()
        talk("What is the message")
        webbrowser.open("https://web.whatsapp.com/send?phone=" +
                user_name[name]+'&text='+take_command())
        sleep(6)
        pyautogui.press('enter')
        talk("Message sent")
    except Exception as e:
        print(e)
        talk("Unable to send the Message")

def weather():
    city = "jaipur"
    res = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=16f0afad2fd9e18b7aee9582e8ce650b&units=metric").json()
    temp1 = res["weather"][0]["description"]
    temp2 = res["main"]["temp"]
    talk(
        f"Temperature is {format(temp2)} degree Celsius \nWeather is {format(temp1)}")

def news():
    newsapi = NewsApiClient(api_key='5840b303fbf949c9985f0e1016fc1155')
    talk("What topic you need the news about")
    topic = take_command()
    data = newsapi.get_top_headlines(
        q=topic, language="en", page_size=5)
    newsData = data["articles"]
    for y in newsData:
        talk(y["description"])

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    elif 'open youtube' in command:
        talk("Opening youtube")
        webbrowser.open("www.youtube.com")
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)

    elif 'who  is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)


    elif 'wikipedia' in command:
        talk('Searching Wikipedia...')
        command = command.replace("wikipedia", "")
        results = wikipedia.summary(command, sentences=2)
        talk("According to Wikipedia")
        print(results)
        talk(results)

    elif "cpu" in command:
        talk(f"Cpu is at {str(psutil.cpu_percent())}")
    elif "open google" in command:
        talk("Opening Google ")
        webbrowser.open("www.google.com")

    #elif " download video from youtube" in command:
        #talk("Downloading")
        #Downloader()

    elif 'date' in command:
        date = command.replace('date is','')
        today = datetime.datetime.today()
        print(today)
        talk(today)
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif ("search" in command):
        talk("what you want to search?")
        webbrowser.open("https://www.google.com/search?q="+take_command())
    elif ('message' in command):
        print("Sending...")
        sendWhatMsg()
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif ('weather' in command):
        weather()
    elif "tell me your name" in command:
        talk("I am beautiful. Your deskstop Assistant")
    elif "which day it is" in command:
        tellDay()
    elif ("news" in command):
        news()
    elif "open whatsapp" in command:
        talk("Opening whatsapp")
        webbrowser.open("https://web.whatsapp.com/")
    elif ("screenshot" in command ):
        pyautogui.screenshot(str(t.time()) + ".png").show()
    elif "bye" in command:
        talk("Bye. Have a good day")
        exit()
    else:
        talk('Please say the command again.')

def hello():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        talk("Good Morning")
    elif hour>=12 and hour<18:
        talk("Good Afternoon")4
    else:
        talk("Good Evening")

    talk("boss, i am your desktop assistant \n Tell me how can i help you")

hello()


while True:
    run_alexa()