import speech_recognition as sr
import datetime
import wikipedia
import pyttsx3
import webbrowser
import os
import time
from requests import get
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
import requests
# from PIL import Image, ImageDraw
import pandas as pd
import numpy as np
import matplotlib.pylab as plt

# Initialize the speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Function to speak the given audio


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to wish the user based on the time of the day


def wish():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good morning, sir. How are you?")
    elif 12 <= hour < 18:
        speak("Good afternoon, sir. How are you?")
    elif 19 <= hour < 20:
        speak("Good evening, sir. How are you?")
    else:
        speak("Good Night, sir. How are you?")

# Function to take command from the user


def takecom():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Recognizing.")
        text = r.recognize_google(audio, language='en-in')
        print(text)
    except Exception:
        speak("Error...")
        print("Network connection error")
        return "none"
    return text

# Function to sing a song from the given lyrics


def sing(song_lyrics):
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1)
    for line in song_lyrics:
        engine.say(line)
        time.sleep(1)
    engine.runAndWait()


# Lyrics for the song
song_lyrics = [
    "Are you stupid, sir?",
    "I am a program,",
    "Not a singer, sir."
]

# Function to search the web


def search_web(query):
    try:
        webbrowser.open(f"https://www.google.com/search?q={query}")
        speak("Oke Wait!.")
    except Exception as e:
        speak("An error occurred while trying to search the web.")
        print(f"Error: {str(e)}")

# Function to tell the current time


def tell_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"Current time is {current_time}")

# Function to get images from the web


def get_images(query):
    try:
        search_url = f"https://www.google.com/search?q={query}&tbm=isch"
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(search_url, headers=headers)
        if response.status_code == 200:
            speak("Here are some images related to your query.")
            webbrowser.open(response.url)
        else:
            speak("Sorry, I couldn't find any images for your query.")
    except Exception as e:
        speak("An error occurred while trying to search for images.")
        print(f"Error: {str(e)}")

# Function to create an image


def create_image():
    # Image size
    width = 400
    height = 400

    # Create image object
    img = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(img)

    # Draw Iron Man head shape
    head_radius = 150
    head_center = (width // 2, height // 2)
    draw.ellipse((head_center[0] - head_radius, head_center[1] - head_radius,
                  head_center[0] + head_radius, head_center[1] + head_radius),
                 fill='red', outline='black')

    # Draw eyes
    eye_radius = 20
    eye_center1 = (head_center[0] - 60, head_center[1] - 50)
    eye_center2 = (head_center[0] + 60, head_center[1] - 50)
    draw.ellipse((eye_center1[0] - eye_radius, eye_center1[1] - eye_radius,
                  eye_center1[0] + eye_radius, eye_center1[1] + eye_radius),
                 fill='white', outline='black')
    draw.ellipse((eye_center2[0] - eye_radius, eye_center2[1] - eye_radius,
                  eye_center2[0] + eye_radius, eye_center2[1] + eye_radius),
                 fill='white', outline='black')

    # Draw mouth
    mouth_start = (head_center[0] - 70, head_center[1] + 30)
    mouth_end = (head_center[0] + 70, head_center[1] + 30)
    draw.line([mouth_start, mouth_end], fill='black', width=10)

    # Save the image
    img.save('iron_man.png')

    # Display the image
    img.show()

# Fungsi untuk membaca data dari file CSV dan melakukan analisis sederhana


def analyze_data(file_path):
    # Read data from a CSV file
    data = pd.read_csv(file_path)
    # Perform simple analysis
    # For example, calculate the average of the 'value' column
    mean_value = data['value'].mean()
    print(f"Average value: {mean_value}")
    speak(f"The average value is {mean_value}")

# Function to open all applications


def terminal():
    os.system('start ""')


# Function to open file explorer
def open_file_explorer():
    os.system('explorer')


def data():
    t = np.linspace(0, 1, 100)
    plt.plot(t, t**2)
    plt.show()


def test():
    reg = linear_model.Ridge(alpha=.5)
    reg.fit([[0, 0], [0, 0], [1, 1]], [0, .1, 1])
    print(reg.coef_)
    print(reg.intercept_)

# Function to close all open applications


# def close_all_applications():
#     os.system("taskkill /f /im chrome.exe")
#     os.system("taskkill /f /im firefox.exe")
#     os.system("taskkill /f /im explorer.exe")
#     os.system("taskkill /f /im excel.exe")
#     # Add more taskkill commands for other applications as needed

# # Function to open all applications


# def open_all_applications():
#     os.system("start chrome")  # Open Chrome browser
#     os.system("start firefox")  # Open Firefox browser
#     os.system("start explorer")  # Open File Explorer
#     os.system("start excel")  # Open Microsoft Excel
#     # Add more start commands for other applications as needed


# Main function
if __name__ == "__main__":
    wish()
    while True:
        query = takecom().lower()

        if "wikipedia" in query:
            speak("Searching details... Please wait.")
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak(results)
            except wikipedia.exceptions.DisambiguationError as e:
                speak("There are multiple entries for this. Can you be more specific?")
                print("Disambiguation error: ", e.options)
            except wikipedia.exceptions.PageError:
                speak("Sorry, I couldn't find any results for your query.")
            except wikipedia.exceptions.WikipediaException as e:
                speak("An unknown error occurred while accessing Wikipedia.")
                print("Wikipedia error: ", str(e))
            except Exception as e:
                speak("An error occurred while fetching information from Wikipedia.")
                print("Error: ", str(e))

        elif "sing" in query:
            speak(sing(song_lyrics))

        elif 'play games' in query:
            webbrowser.open("https://tetris.com/play-tetris")
            speak("Enjoy your game, sir.")

        elif 'my website' in query:
            webbrowser.open("http://localhost/rentalcar/customer/dashboard")
            speak("Okay, wait.")

        elif 'news' in query or 'latest news' in query:
            speak("Searching for the latest news...")
            webbrowser.open("https://news.google.com")
            speak("Here's the latest news.")

        elif 'open notepad' in query:
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)

        elif "my ip" in query:
            ip = get('https://api.ipify.org').text
            speak(f"Your IP address is {ip}")

        elif 'open github' in query:
            webbrowser.open("https://www.github.com")
            speak("Opening GitHub.")

        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com")
            speak("Opening Facebook.")

        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com")
            speak("Opening Instagram.")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com")
            speak("Opening Google.")

        elif 'open yahoo' in query:
            webbrowser.open("https://www.yahoo.com")
            speak("Opening Yahoo.")

        elif 'open gmail' in query:
            webbrowser.open("https://mail.google.com/mail/u/0/")
            speak("Opening Google Mail.")

        elif 'sleeping' in query:
            speak("Goodbye.")
            exit()

        elif "shut down" in query:
            speak("Shutting down.")
            os.system('shutdown -s')

        elif "who are you" in query or "about you" in query or "your details" in query:
            about = "I am Rivi, an AI-based computer program. I can help you with various tasks. Try giving me a simple command!"
            print(about)
            speak(about)

        elif "hello" in query:
            hel = "Hello Sir! How may I help you?"
            print(hel)
            speak(hel)

        elif "thank you" in query or "thanks" in query:
            tq = "You're welcome sir."
            print(tq)
            speak(tq)

        elif "your name" in query:
            na_me = "My name is Rivi. Thanks for asking."
            print(na_me)
            speak(na_me)

        elif "love you" in query:
            print("I appreciate your affection.")
            speak("I appreciate your affection, sir.")

        elif "what time is it" in query or "tell me the time" in query:
            tell_time()

        elif "create image" in query:
            create_image()

        elif "analyze data" in query:
            speak("Analyzing data... Please wait.")
            analyze_data('D:\\pemrograman\\PYTHON\\friend\\nama_file.csv')

        elif "visualize data" in query:
            speak("Analyzing data....Please wait.")
            data()

        elif "test data" in query:
            speak("Analyzing data....Please wait.")
            test()

        elif "open file" in query:
            open_file_explorer()

        # elif "close" in query:
        #     speak("close all aplication....Please wait.")
        #     close_all_applications()

        # elif "open" in query:
        #     speak("open all aplication....Please wait.")
        #     open_all_applications()

        elif "open terminal" in query:
            terminal()

        elif "get weather" in query:
            speak("Searching weather information... Please wait.")
            city = "Jakarta"
            try:
                search_query = f"cuaca di {city}"
                results = webbrowser.open(
                    f"https://www.google.com/search?q={search_query}")
                weather_description = f"The weather in {city} is currently clear with a temperature of {results}"
                speak(weather_description)
                print(weather_description)
            except Exception as e:
                speak("Terjadi kesalahan saat mencoba mengambil informasi cuaca.")
                print(f"Error: {str(e)}")

        elif query == 'none':
            continue

        else:
            search_web(query)
