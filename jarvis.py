import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import requests
import json
import random

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    print(f"Rubi: {audio}")

def wishme():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("This is Rubi. How may I help you?")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"You said: {query}\n")
    except Exception as e:
        print("Please say that again...")
        return "None"
    return query

if __name__ == "__main__":
    wishme()
    while 1:
        query = takecommand().lower()

        if 'quit' in query:
            speak("Exiting...")
            break

        elif 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(result)
            speak(result)

        elif 'open youtube' in query:
            speak("Opening Youtube")
            webbrowser.open("www.youtube.com")

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strtime}")

        elif 'open spotify' in query:
            speak("Opening Spotify")
            codepath = "C:/Users/lenovo/AppData/Roaming/Spotify/Spotify.exe"
            os.startfile(codepath)

        elif 'who are you' in query:
            speak("I am a Dekstop assistant named rubi")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'the news' in query:
            speak("The news is as follow")
            url = ('https://newsapi.org/v2/top-headlines?'
                   'sources=google-news-in&'
                   'apiKey=5440b810b0f64bb2964ebd955f0cc95f')
            response = requests.get(url)
            text = response.text
            my_json = json.loads(text)
            for i in range(1, 11):
                try:
                    print(f"{i}){my_json['articles'][i]['title']}")
                    speak(my_json['articles'][i]['title'])
                except IndexError as e:
                    print("No more News!")

        elif 'the weather' in query:
            api_key = "32ace99a0d8ad9cb4ef5c321343062af"
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            city_name = "Ghaziabad"
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            y = x["main"]
            temp = y["temp"]
            temp_celsius = temp-273.15
            temp_celsius = round(temp_celsius, 3)
            speak(f"Sir, the temperature is {temp_celsius} degree celsius")

        elif 'shutdown' in query:
            os.system("shutdown /s /t 5")

        elif 'play rock paper scissors' in query:
            speak("Playing rock paper scissors")
            score_user = 0
            score_computer = 0
            choices = ("rock", "paper", "scissors")
            computer = random.choice(choices)
            while True:
                speak("Your turn:\nWhat do you choose?")
                user = takecommand()
                print("You: ",user)
                if user == "rock" or "paper" or "scissors" or "exit":
                    speak(computer)
                    if user == "exit":
                        break
                    elif user == "paper" and computer == "scissors":
                        print("Me:", computer)
                        speak("I won!")
                        score_computer += 1
                        print("Your score:", score_user, "and computer's score:", score_computer)
                    elif user == "scissors" and computer == "rock":
                        print("Computer:", computer)
                        speak("I won!")
                        score_computer += 1
                        print("Your score:", score_user, "and computer's score:", score_computer)
                    elif computer == "rock" and user == "paper":
                        print("Computer:", computer)
                        speak("You won!")
                        score_user += 1
                        print("Your score:", score_user, "and computer's score:", score_computer)
                    elif computer == "paper" and user == "scissors":
                        print("Computer:", computer)
                        speak("You won!")
                        score_user += 1
                        print("Your score:", score_user, "and computer's score:", score_computer)
                    elif computer == "scissors" and user == "rock":
                        print("Computer:", computer)
                        speak("You won!")
                        score_user += 1
                        print("Your score:", score_user, "and computer's score:", score_computer)
                    elif user == "rock" and computer == "paper":
                        print("Computer:", computer)
                        speak("Computer won!")
                        score_computer += 1
                        print("Your score:", score_user, "and computer's score:", score_computer)
                    elif computer == user:
                        print("Computer:", computer)
                        speak("This is a Tie!")
                        print("Your score:", score_user, "and computer's score:", score_computer)
                    else:
                        speak("Invalid input!")
                        break
                speak("Do you want to play again? Y/N")
                ans = takecommand()
                if ans == 'no':
                    speak("Thanks for playing the game!")
                    break

        else:
            speak("Sorry! I don't have any information related to that")
