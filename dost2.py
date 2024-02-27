
import pyttsx3
import speech_recognition as sr
from datetime import datetime
from random import choice
import cv2
import tkinter as tk
from PIL import Image, ImageTk
import os
import subprocess as sp
import requests
import wikipedia
import pyautogui
# import pywhatkit as kit
import urllib.parse
import webbrowser
# from functions.os_ops import open_calculator,open_notepad

import subprocess





#   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
#   .\myenv\Scripts\Activate

# Initialize text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 120)
engine.setProperty('voice', voices[1].id)  # Set voice to female voice


# Set up speech recognizer
recognizer = sr.Recognizer()
microphone = sr.Microphone()

# Opening text for responses
opening_text = [
    "Cool, I'm on it sir.",
    "Okay sir, I'm working on it.",
    "Just a second sir.",
]

# Function to greet the user
def greet_user():
    current_hour = datetime.now().hour
    if 6 <= current_hour < 12:
        speak("Good morning, sir!")
    elif 12 <= current_hour < 16:
        speak("Good afternoon, sir!")
    elif 16 <= current_hour < 21:
        speak("Good evening, sir!")
    else:
        speak("Hello, sir!")
    speak("I am Jarwis,your virtual assistant. How may I assist you today?")

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen for user input
def take_user_input():
    with microphone as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language="en")
        print("User said:", query)
        if "open camera" in query.lower() or "camera" in query.lower() or "open the camera" in query.lower():
            open_camera()
            return None
        if "capture photo" in query.lower() or "photo" in query.lower() or "click photo" in query.lower() or "picture " in query.lower():
            capture_photo()
            return None
        if "youtube" in query.lower():
            search_query = extract_search_query(query)
            print("Search query:", search_query)
            search_youtube(search_query)
            return "exit"
        if "open command prompt" in query.lower() or "command prompt" in query.lower() or "command line interface" in query.lower():
            open_cmd()
        if "time" in query:
            # current_hour = datetime.now().hour
            strTime = datetime.now().strftime("%H:%M:%S")
            speak("Sir, the time is " + strTime)
            return None
        if "cursor" in query.lower() or "eye" in query.lower() or "eyes" in query.lower():
            speak("Ok, sure sir, I am working on it and please keep your eyes infront the camere.")
            eye_cursor_process = sp.Popen(['C:\\Users\\sigde\\OneDrive\\Desktop\\extra python\\myenv\\Scripts\\python.exe', 'C:\\Users\\sigde\\OneDrive\\Desktop\\extra python\\eyecursor.py'])
            eye_cursor_process.wait()
            return None
        if "minimize" in query.lower() or "minimise" in query.lower():
            speak("Ok sir, I am minimizing it.")
            pyautogui.hotkey('win','down','down')
            return None
        if "maximize" in query.lower() or "maximise" in query.lower():
            speak("Ok sir, I am maximizing it.")
            pyautogui.hotkey('win','up','up')
            return None
        if "cloze the window" in query.lower() or "close the window" in query.lower() or "close" in query.lower():
            speak("Ok sir, I am closing it.")
            pyautogui.hotkey('ctrl','w')
            return None
    
        if "chandrama" in query.lower() or "ishika" in query.lower() or "chandarama" in query.lower():
            speak("Oh, yeah sir, she is your wife. You have married the beautiful girl sir.")
            return None
        if "bijan" in query.lower() or "vision" in query.lower() or "bejan" in query.lower():
            speak("Oh, yeah I know him sir. He is your student . He feel bored while studying but he loves to play football. You should train him well")
            return None
        if "sahil" in query.lower() or "sahel" in query.lower() or "sawhil" in query.lower():
            speak("Oh, yeah I know him sir. He is your student . He is in A level now. You should train him well")
            return None
        if "roshan" in query.lower() or "roshaan" in query.lower() or "roshen" in query.lower():
            speak("Oh, yeah I got it. The few days ago you checked his bag when you lost your phone. He is really a silly guy sir.")
            return None
        if "assam" in query.lower() or "friend" in query.lower() or "dost" in query.lower():
            speak("Oh, yeah I got it. He used to offer you bhola sir.")
            return None
        if "sansar" in query.lower() or "sanchar" in query.lower() or "sanshar" in query.lower():
            speak("Oh, yeah I got it. You saved his contact number as hancy hero sir.")
            return None
        if "ishan" in query.lower() or "friend" in query.lower() or "dost" in query.lower():
            speak("Oh, yeah I got it. He always seem to come with you while going to college.")
            return None
        if "how are you" in query.lower() or "are you fine" in query.lower() or "what's up" in query.lower():
            speak("I am fine sir,thank you for asking and what about you sir.")
            return None
        if "hemanta" in query.lower() or "hamanta" in query.lower() or "hemant" in query.lower():
            speak("Oh, yeah I know him sir, he is principle of Genius school and I think he is pro in smoking")
            return None
        if "nikesh" in query.lower()  or "nikes" in query.lower() or "nikess" in query.lower():
            speak("yes offcourse sir, last time he become famous when he got drunk, he mesh up with abhishek sir too. His profile is in Alpha male group ")
            return None
        if "sumit" in query.lower()  or "summit" in query.lower() or "somit" in query.lower():
            speak("Oh, yeah I know him sir, he is coordinator of Genius school and I think he love to dance whe he is drunk.")
            return None
        if "abhishek" in query.lower()  or "abishek" in query.lower() or "avisek" in query.lower():
            speak("Oh, yes I know him sir, he always use word muji when he is drunk, he needs to eat a lot at single time.")
            return None
        if "puran" in query.lower()  or "poran" in query.lower() or "puuran" in query.lower():
            speak("Oh, yeah I know him sir, he is sport teacher, he plays basketball well.")
            return None
        if "rupes" in query.lower()  or "rupesh" in query.lower() or "ropesh" in query.lower():
            speak("Oh, yeah I know him sir, he is accountant in genius school, he always shakes hand with you when he meet with you.")
            return None
        if "exit" in query.lower() or "stop" in query.lower() or "suta" in query.lower() or "sut" in query.lower() or "sutaa" in query.lower() or "good night" in query.lower():
            current_hour = datetime.now().hour
            if current_hour >= 21 or current_hour < 6:
                speak("Good night, sir. Take care!, and please wake me up when you feel bored or if any help needed.")
            else:
                speak("Have a good day, sir!, and please wake me up when you feel bored or if any help needed.")
            return "exit"
        else:
            speak(choice(opening_text))
            return query
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Could you please repeat?")
        return None
    except sr.RequestError:
        speak("Sorry, there was an issue with the speech recognition service. Please try again to say.")
        return None

# def open_notepad():
#     os.startfile(paths['notepad'])

# def open_calculator():
#     sp.Popen(paths['calculator'])
    
def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)
def capture_photo():
    camera = cv2.VideoCapture(0)
    return_value, image = camera.read()
    cv2.imwrite('captured_photo.jpg', image)
    del(camera)
    speak("Photo captured successfully!")

def open_cmd():
    os.system('start cmd')

def extract_search_query(query):
    start_keywords = ["search for", "search","look for", "find", "about","search in","provide me","in","youtube" "on"]
    platform_keywords = ["youtube", "YouTube","google"]  # Add more platforms as needed
    
    # Split the query into words
    words = query.lower().split()
    
    # Initialize search query
    search_query = ""
    
    # Flag to check if platform keyword is encountered
    platform_flag = False
    
    # Iterate over words to extract search query
    for i, word in enumerate(words):
        if word in start_keywords:
            # Start of search query found
            search_query = " ".join(words[i + 1:])
            # break
        elif word in platform_keywords:
            # Platform keyword found, set flag to True
            platform_flag = True
    
    # If platform keyword is found, remove it from the search query
    if platform_flag:
        # Find the index of the platform keyword
        platform_index = words.index(word)
        if platform_index < len(words) - 1:
            # Combine the words after the platform keyword
            search_query = " ".join(words[platform_index + 1:])
    
    return search_query.strip()


def search_youtube(search_query):
    try:
        speak(",Okay sir,I am working for it.")
        base_url = "https://www.youtube.com/results?search_query="
        query_encoded = urllib.parse.quote(search_query)
        search_url = base_url + query_encoded
        webbrowser.open(search_url)
    except Exception as e:
        print("An error occurred:", e)

# Main function to execute the program
def main():
    greet_user()
    while True:
        user_input = take_user_input()
        if user_input == "exit":  
            break
    
    # if 'open notepad' in query.lower():
    #     open_notepad()

    # elif 'open calculator' in query.lower():
    #     open_calculator()
        # if user_input is None:
        #     break

if __name__ == "__main__":
    try:
        import pywhatkit as kit
        main()
    except Exception as e:# ImportError:
        speak("Pywhatkit is not available. Running without it. We are not using any internet connections.")
        main()
   







