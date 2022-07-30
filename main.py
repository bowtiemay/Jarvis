import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def say(text):
    engine.say(text)
    engine.runAndWait()

say('Hello, I am Jarvis. What can I do for you?')

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                print(command)

    except:
        pass

    return command

def run_jarvis():
    command = take_command()
    if 'play' in command:
        music = command.replace('play', '')
        say('playing' + music)
        pywhatkit.playonyt(music)

    elif 'time' in command:
        time = datetime.datetime.now().strfttime('%H:%M %p')
        say('Current time is ' + time)

    elif 'who is' in command or 'where is' in command or 'what is' in command:
        thing = command.replace('who is', '')
        thing = command.replace('where is', '')
        thing = command.replace('what is', '')

        info = wikipedia.summary(thing, 1)
        say(info)

    elif 'joke' in command:
        say(pyjokes.get_joke())
    
    else:
        say("Sorry, I didn't catch that.")

while True:
    run_jarvis()