# 1st project from Golden Project
import speech_recognition as sr
import pyttsx3
import pywhatkit as kit
import datetime
import webbrowser
listener = sr .Recognizer()
engine = pyttsx3.init()
voices =  engine.getProperty('voices')               # Replace this with the index of the desired voice
                                                     # Set the selected voice
engine.setProperty('voice', voices[1].id)
#################################################################################
def talk(text):
    engine.say(text)  
    engine.runAndWait()
#################################################################################
def search_on_google(query):
    kit.search(query)
##################################################################################
def open_website(command):
    print(command)
    website_mappings = {
        "open google": "https://www.google.com",
        "open gpt": "https://chat.openai.com//",
        "open whatsapp": "https://web.whatsapp.com/",
        
        # Add more website mappings here
    }
    url = website_mappings.get(command.lower(), None)
    if url:
        webbrowser.open(url)
        print(f"Opening {url}")
    else:
        print("Website not recognized. Please try again.")
###################################################################################
def take_command():
    try:
        with sr.Microphone() as source:
            print("listening.....")
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source)
            comand = listener.recognize_google(voice)
            comand = comand.lower()
            if 'alexa' in comand:
                comand = comand.replace('alexa','')
            print(comand)
               
    except:
        talk("can't recognise your voice ......")
        comand=""
    return comand

def run():
    command=take_command()
    if command=="":
        talk("sorry ")
        run()
    if 'play' in command:
        song = command.replace('song','').replace('play','')
        print(song)
        talk('here is the song.....'+ song +'..for you')
        kit.playonyt(song)

    elif"search" in command and "google" in command:
        query = command.replace("search", "").replace("google", "").strip()
        talk('here is the result..')
        search_on_google(query)

    elif 'time' in command :
        if 'what' in command or 'tell' in command:
            time=datetime.datetime.now().strftime('%I:%M %p')
            talk('current time is '+time)
            print(time)
        else:
            talk("sorry")

    elif 'date' in command:
        date=datetime.datetime.today().strftime('%A, %d %B %Y')
        talk('the current date is..'+date)
        print(date)

    elif "open"in command:
        if 'gpt' in command:
            open_website(command.lstrip(' '))
        elif 'google' in command:
            open_website(command.lstrip(' '))
        elif'youtube' in command:
             open_website(command.lstrip(' '))

    elif "exit" in command:
        print("Exiting the program.")
        exit
    else:
        talk('please say the command again.......')
run()