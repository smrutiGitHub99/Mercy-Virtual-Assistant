import speech_recognition as sr
import playsound
import random
from gtts import gTTS
import webbrowser
import ssl
import certifi
import time
import os
import subprocess
from PIL import Image
import pyautogui
import pyttsx3
import bs4 as bs
import urllib.request

class person:
    name = ''
    def setName(self, name):
        self.name = name

class asis:
    name = ''
    def setName(self, name):
        self.name = name

def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True

def engine_speak(text):
    text = str(text)
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer()

def record_audio(ask=""):
    with sr.Microphone() as source: # microphone as source
        if ask:
            engine_speak(ask)
        audio = r.listen(source, 5, 5)  # listen for the audio via source
        print("Command Received")
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)  # convert audio to text
        except sr.UnknownValueError: # error: recognizer does not understand
            engine_speak('Sorry sir, I did not get that')
        except sr.RequestError:
            engine_speak('Sorry Sir, the service is down') # error: recognizer is not connected
        print(">>", voice_data.lower()) # print what user said
        return voice_data.lower()

def engine_speak(audio_string):
    audio_string = str(audio_string)
    tts = gTTS(text=audio_string, lang='en') # text to speech(voice)
    r = random.randint(1,20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file) # save as mp3
    playsound.playsound(audio_file) # play the audio file
    print(asis_obj.name + ":", audio_string) # print what app said
    os.remove(audio_file) # remove audio file

def respond(voice_data):
    # greeting
    if there_exists(['hey','hi','hello']):
        greetings = ["hello, how can I help you" + person_obj.name, "hey, what's up?" + person_obj.name, "I'm listening" + person_obj.name, "how can I help you?" + person_obj.name, "hello" + person_obj.name]
        greet = greetings[random.randint(0,len(greetings)-1)]
        engine_speak(greet)
    # name
    if there_exists(["what is your name","what's your name","tell me your name"]):
        if person_obj.name:
            engine_speak("My name is Mercy. ")
        else:
            engine_speak("I am Mercy.I am your assistant.")

    # 3: greeting
    if there_exists(["how are you","how are you doing"]):
        engine_speak("I'm very well, thanks for asking " + person_obj.name)

    # 4: time
    if there_exists(["what's the time","tell me the time","what time is it","what time it is"]):
        time = ctime().split(" ")[3].split(":")[0:2]
        if time[0] == "00":
            hours = '12'
        else:
            hours = time[0]
        minutes = time[1]
        time = hours + " hours and " + minutes + "minutes"
        engine_speak(time)
    # search google
    if there_exists(["search for"]) and 'youtube' not in voice_data:
        search_term = voice_data.split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for" + search_term + "on google")

    # search youtube
    if there_exists(["youtube","open youtube"]):
        search_term = voice_data.split("for")[-1]
        url = "https://www.youtube.com/results?search_query=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for " + search_term + "on youtube")
    # search for music
    if there_exists(["play music","open spotify"]):
        search_term= voice_data.split("for")[-1]
        url="https://open.spotify.com/search/"+search_term
        webbrowser.get().open(url)
        engine_speak("You are listening to"+ search_term +"enjoy sir")
    #search for amazon.com
    if there_exists(["amazon.com","open amazon.com"]):
        search_term = voice_data.split("for")[-1]
        url="https://www.amazon.in"+search_term
        webbrowser.get().open(url)
        engine_speak("here is what i found for"+search_term + "on amazon.com")
    #make a note
    if there_exists(["make a note","I want to make a note"]):
        search_term=voice_data.split("for")[-1]
        url="https://keep.google.com/#home"
        webbrowser.get().open(url)
        engine_speak("Here you can make notes")
    #open instagram
    if there_exists(["open instagram"]):
        search_term=voice_data.split("for")[-1]
        url="https://www.instagram.com/"
        webbrowser.get().open(url)
        engine_speak("opening instagram")
    #open twitter
    if there_exists(["open twitter"]):
        search_term=voice_data.split("for")[-1]
        url="https://twitter.com/"
        webbrowser.get().open(url)
        engine_speak("opening twitter")
    #8 weather
    if there_exists(["weather","tell me the weather report","whats the condition outside","how's the weather"]):
        search_term = voice_data.split("for")[-1]
        url = "https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5"
        webbrowser.get().open(url)
        engine_speak("Here is what I found for on google")
    #open gmail
    if there_exists(["open my mail","gmail","check my email","check my mail"]):
        search_term = voice_data.split("for")[-1]
        url="https://mail.google.com/mail/u/0/#inbox"
        webbrowser.get().open(url)
        engine_speak("here you can check your gmail")
    # calc
    if there_exists(["plus","minus","multiply","divide","power","+","-","*","/"]):
        opr = voice_data.split()[1]

        if opr == '+':
            engine_speak(int(voice_data.split()[0]) + int(voice_data.split()[2]))
        elif opr == '-':
            engine_speak(int(voice_data.split()[0]) - int(voice_data.split()[2]))
        elif opr == 'multiply':
            engine_speak(int(voice_data.split()[0]) * int(voice_data.split()[2]))
        elif opr == 'divide':
            engine_speak(int(voice_data.split()[0]) / int(voice_data.split()[2]))
        elif opr == 'power':
            engine_speak(int(voice_data.split()[0]) ** int(voice_data.split()[2]))
        else:
            engine_speak("Wrong Operator")
    # screenshot
    if there_exists(["capture my screen","screenshot","take a screenshot"]):
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(r"C:\Users\ankur\Pictures\Screenshots")

    if there_exists(["exit", "quit", "goodbye"]):
        engine_speak("As you say...Shutting down the engine...see u again good bye")
        exit()
time.sleep(1)

person_obj = person()
person_obj.name = 'Ankur'
asis_obj = asis()
asis_obj.name = 'Mercy'
engine = pyttsx3.init()


while(1):
    voice_data = record_audio("Recording") # get the voice input
    print("Done")
    print("Q:", voice_data)
    respond(voice_data) # respond