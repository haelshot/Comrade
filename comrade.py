import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
# import os
import time
import subprocess
from ecapture import ecapture as ec
from wikipedia.wikipedia import random
import wolframalpha
# import json
import requests
import random

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[1].id')
speechs = ["how can i help you?", "what do you need ?", "what should i do now?", "what are the next instructions"]
speech = random.choice(speechs)
def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = input("Enter your instruction: ")
        # audio=r.listen(source)

        try:
            # statement=r.recognize_google(audio,language='en-in')
            statement = audio
            print(f"user said:{statement}\n")

        except Exception as e:
            speak(speech)
            return "None"
        return statement

print("Loading your AI personal assistant Comrade")
speak("Hi i am comrade your personal assistant")
wishMe()

def open_site(name):
    webbrowser.open_new_tab(f"https://www.{name}.com")
    speak(f"{name} is opening")
def cal(statement1, statement2, operator):
    if operator == "+":
        result = statement1 + statement2
    if operator == "-":
        result = statement1 - statement2
    if operator == "*":
        result = statement1 * statement2
    if operator == "/":
        result = statement1 / statement2
    return result
if __name__=='__main__':
    while True:
        speak(speech)
        statement = takeCommand().lower()
        if statement==0:
            continue
        if "bye" in statement or "ok bye" in statement or "stop" or "exit" in statement:
            speak('shutting down')
            print('shutting down ...')
            print('Good bye')
            break
        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open' in statement:
            new_st = statement[5:]
            statement = ""
            for n in new_st:
                statement += n
                if n == " ":
                    break
            open_site(statement)
            time.sleep(5)
        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)
        elif 'search'  in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)
        elif 'ask' in statement:
            speak('I can answer to computational and geographical questions  and what question do you want to ask now')
            question=takeCommand()
            app_id="Paste your unique ID here "
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)
        elif 'who are you' in statement or 'what can you do' in statement:
                speak('I am comrade version 1 point O your personal assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome, gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 
                  'In different cities, get top headline news from times of india and you can ask me computational or geographical questions too!')
        elif "maths" in statement:
            speak("Okay you want to perform some mathematical operations give me your instructions")
            state_1 = int(input("Enter first number: "))
            opr = input("Enter operator: ")
            state_2 = int(input("Enter second number: "))
            statement = cal(state_1, state_2, opr)
            print(statement)
            speak(f"The result for {state_1} {opr} {state_2} is {statement}")
            time.sleep(3)

        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Hellshot")
            print("I was built by Haelshot")
        elif "weather" in statement:
            api_key="Check wolframalpha for api. dont forget"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("what is the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))
        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])
        else:
            speak("ohmm, sorry i am not programmed to do this i am hoping abdullahi would upgrade be.")
			
time.sleep(8)	