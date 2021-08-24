import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes

listener = sr.Recognizer()
alexa = pyttsx3.init()

def talk(text):
  alexa.say(text)
  alexa.runAndWait()

def take_command():
 try:
     with sr.Microphone() as source:
         print('Listening....')
         voice=listener.listen(source)
         command=listener.recognize_google(voice)
         command=command.lower()
         print(command)
 except:
     pass
 return command

def run_alexa():
    command = take_command()
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'play' in command:
        song = command.replace('play','')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'tell me about' in command:
        about = command.replace('tell me about' , '')
        info = wikipedia.summary(about, 1)
        talk(info)
    elif 'joke' in command:
        joke =pyjokes.get_joke()
        print(joke)
        talk(joke)
    elif 'search' in command:
        khuja = command.replace('search' , '')
        talk('searching' + khuja)
        pywhatkit.search(khuja)
    else:
        talk('please tell me again , I did not understand properly')
while True:
  run_alexa()