import pyttsx3
import speech_recognition as sr
from datetime import datetime
from random import choice
import cv2
import tkinter as tk
from PIL import Image, ImageTk
import os
import subprocess as sp
import urllib.parse
import webbrowser

# Initialize text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 120)
engine.setProperty('voice', voices[1].id)
  # Replace 'nepali_voice_id' with the ID of the Nepali language voice
  # स्त्री आवाज सेट गर्नुहोस्


# स्पीच रिकग्नाइजर सेट गर्नुहोस्
recognizer = sr.Recognizer()
microphone = sr.Microphone()

# खोल्ने पाठ
opening_text = [
    "ठिक छ, म काम गरिरहेको छु।",
    "केहि समय कृपया।",
]

# प्रयोगकर्तालाई स्वागत गर्ने कार्य
def greet_user():
    current_hour = datetime.now().hour
    if 6 <= current_hour < 12:
        speak("सुप्रभात, सर!")
    elif 12 <= current_hour < 16:
        speak("नमस्ते, सर!")
    elif 16 <= current_hour < 21:
        speak("शुभ सन्ध्या, सर!")
    else:
        speak("नमस्ते, सर!")
    speak("म जार्विस, तपाईंको आवाज सहायक। तपाईंलाई कसरी म सहायता गर्न सक्छु?")

# पाठलाई आवाजमा परिवर्तन गर्ने कार्य
def speak(text):
    engine.say(text)
    engine.runAndWait()

# प्रयोगकर्ताबाट इनपुट सुन्ने कार्य

def take_user_input():
    with microphone as source:
        print("सुन्न अवस्थामा...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        print("पहिचान गर्दै...")
        query = recognizer.recognize_google(audio, language="NE")
        print("प्रयोगकर्ताले भने:", query)
        if "क्यामेरा खोल्नुहोस्" in query.lower() or "क्यामेरा" in query.lower() or "क्यामेरा खोल" in query.lower():
            open_camera()
            return None
        if "फोटो लिनु" in query.lower() or "फोटो" in query.lower() or "फोटो लिन" in query.lower() or "तस्वीर" in query.lower():
            capture_photo()
            return None
        if "युट्युब" in query.lower():
            search_query = extract_search_query(query)
            print("खोजको क्युरी:", search_query)
            search_youtube(search_query)
            return "निकास"
        # अन्य कुरा को लागि तयारी जारी राख्नुहोस्...
        if "चन्द्रमा" in query.lower() or "ईशिका" in query.lower() or "चन्द्रम" in query.lower():
           speak("हो, हो सर, उनी तपाईंकी पत्नी हुन्। तपाईंले सुन्दर कन्या संग विवाह गरिरहेका छौं सर।")
           return None
        if "बिजन" in query.lower() or "विजन" in query.lower() or "बेजन" in query.lower():
            speak("हो, हो सर, म उनलाई थाहा छु। वह तपाईंको छात्र हुन्। पढाइमा बोरेको लागि मानिस हुन्, तर उहाँले फुटबल खेल्न मन पर्छ। तपाईंलाई उनलाई राम्रो तरिकामा प्रशिक्षण दिनुपर्छ।")
            return None
        if "साहिल" in query.lower() or "साहेल" in query.lower() or "सव्हिल" in query.lower():
            speak("हो, हो सर, म उनलाई थाहा छु। वह तपाईंको छात्र हुन्। उहाँ A लेभलमा छ। तपाईंलाई उनलाई राम्रो तरिकामा प्रशिक्षण दिनुपर्छ।")
            return None
        if "रोशन" in query.lower() or "रोशान" in query.lower() or "रोशेन" in query.lower():
            speak("हो, हो म थाहा पाएँ। केहि दिन पहिले तपाईंले आफ्नो फोन हराएमा उसको बस्ता जाँच गर्नुभयो। वह वास्तवमा एक मुर्ख व्यक्ति हुन् सर।")
            return None
        if "असम" in query.lower() or "साथी" in query.lower() or "दोस्त" in query.lower():
            speak("हो, हो म थाहा पाएँ। उहाँले तपाईंलाई भोला प्रस्ताव गर्छन् सर।")
            return None
        if "संसार" in query.lower() or "संचार" in query.lower() or "संस्थान" in query.lower():
            speak("हो, हो म थाहा पाएँ। तपाईंले उनको सम्पर्क नम्बरलाई 'ह्यान्सी हीरो' रूपमा सुरक्षित गर्नुभयो सर।")
            return None
        if "ईशान" in query.lower() or "साथी" in query.lower() or "दोस्त" in query.lower():
            speak("हो, हो म थाहा पाएँ। उनी सधैं तपाईंसँग कलेज जाँदा आउँछन् सर।")
            return None
        if "तपाईंलाई कस्तो छ" in query.lower() or "के छ?" in query.lower() or "के गरिरहेको छौ" in query.lower():
            speak("म ठिक छु सर, तपाईंको फेरि सोध्नको लागि धन्यवद")
            return None
        if "निकास" in query.lower() or "रोक" in query.lower() or "सुत" in query.lower() or "शुत" in query.lower() or "सुता" in query.lower() or "शुभ रात्री" in query.lower():
            current_hour = datetime.now().hour
            if current_hour >= 21 or current_hour < 6:
                speak("शुभ रात्री, सर। ध्यान गर्नुहोस्!, र कृपया मलाई जाग्रत गर्नुहोस् जब तपाईंलाई उबाल लाग्छ वा कुनै मद्दत चाहिएको हो।")
            else:
               speak("दिन शुभ हो, सर। र कृपया मलाई जाग्रत गर्नुहोस् जब तपाईंलाई उबाल लाग्छ वा कुनै मद्दत चाहिएको हो।")
            return "निकास"
        else:
            speak(choice(opening_text))
            return None

    except sr.UnknownValueError:
        speak("क्षमा गर्नुहोस्, म सुन्न पाउँदिनँ। के तपाईं कृपया पुनः अवधि गर्न सक्नुहुन्छ?")
        return None
    except sr.RequestError:
        speak("क्षमा गर्नुहोस्, भाषा पहिचान सेवामा समस्या भएको थियो। कृपया पुनः प्रयास गर्नुहोस्।")
        return None

def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)

def capture_photo():
    camera = cv2.VideoCapture(0)
    return_value, image = camera.read()
    cv2.imwrite('captured_photo.jpg', image)
    del(camera)
    speak("फोटो सफलतापूर्वक लिइएको छ!")

# खोज क्युरी निकाल्ने कार्य
def extract_search_query(query):
    start_keywords = ["खोजी", "खोज", "खोज्नुहोस्", "हेर्नुहोस्", "बारेमा", "खोजमा", "मलाई", "यूट्युब", "मा"]
    platform_keywords = ["युट्युब", "यूट्युब", "गूगल"]  # अझै कुरा थप्नुहोस् जस्तो प्लेटफर्महरू
    
    # क्वेरीलाई शब्दहरूमा बाँट्नुहोस्
    words = query.lower().split()
    
    # खोज क्वेरीको आरम्भ गर्ने लागि सेट गर्नुहोस्
    search_query = ""
    
    # प्लेटफर्म कीवर्डको लागि झण्डा लगाउने फ्ल्याग
    platform_flag = False
    
    # खोज क्वेरी निकाल्ने शब्दहरूमा गर्ने लागि शब्दहरूमा ट्रावर्स गर्नुहोस्
    for i, word in enumerate(words):
        if word in start_keywords:
            # खोज क्वेरीको सुरुवात फेला पार्नुभयो
            search_query = " ".join(words[i + 1:])
        elif word in platform_keywords:
            # प्लेटफर्म कीवर्ड पाइएको, झण्डा लगाउने
            platform_flag = True
    
    # प्लेटफर्म कीवर्ड पाइएमा, तपाईंले खोज क्वेरीबाट ती लाई हटाउनुहोस्
    if platform_flag:
        # प्लेटफर्म कीवर्डको इन्डेक्स फेलाउनुहोस्
        platform_index = words.index(word)
        if platform_index < len(words) - 1:
            # प्लेटफर्म कीवर्डपछि शब्दहरूलाई एकत्र गर्नुहोस्
            search_query = " ".join(words[platform_index + 1:])
    
    return search_query.strip()

# युट्युबमा खोज गर्ने कार्य
def search_youtube(search_query):
    try:
        speak("हाँ, ठीक छ, म यसमा काम गर्दैछु।")
        base_url = "https://www.youtube.com/results?search_query="
        query_encoded = urllib.parse.quote(search_query)
        search_url = base_url + query_encoded
        webbrowser.open(search_url)
    except Exception as e:
        print("त्रुटि देखा पर्यो:", e)

# मुख्य कार्य गर्ने कार्य
def main():
    greet_user()
    while True:
        user_input = take_user_input()
        if user_input == "निकास":  
            break


if __name__ == "__main__":
    try:
        import pywhatkit as kit
        main()
    except Exception as e:
        speak("पाइथनकिट उपलब्ध छैन। यसको बिना चलाउनुहोस्। हामी कुनै इन्टरनेटको कनेक्सन प्रयोग गर्दैनौं।")
        main()

