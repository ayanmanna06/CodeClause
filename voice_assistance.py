# 1st project from Golden Project from CodeClause
''' This assistance can only open google,youtube,chatgpt
    and it can search anything in google and play anything on youtube.
    Also it can told the current time and date.'''
# This Assistance is developed by Mr. Ayan Manna 
################################## Program Start ##########################
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
    #print(command)
    website_mappings = {
        "open google": "https://www.google.com",
        "open gpt": "https://chat.openai.com//",
        "open whatsapp": "https://web.whatsapp.com/",
        "open youtube":"https://www.youtube.com/",
        # Add more website mappings here
    }
    url = website_mappings.get(command.lower(), None)
    if url:
        webbrowser.open(url)
        #print(f"Opening {url}")
    else:
        talk("Website not recognized. Please try again.")
############################### Talk Voice Command ##################################
def take_command():
    try:
        with sr.Microphone() as source:
            print("listening.....")
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source)
            comand = listener.recognize_google(voice)
            comand = comand.lower()
            if 'alex' in comand:
                talk("Hello , How can I Help you?")
                comand = comand.replace('alex','')
                comand = 'a'
            #print(comand)
               
    except:
        talk("can't recognise your voice ......")
        comand=""
    return comand
######################### Accroding the command Output ##################
def run():
    command=take_command()
    if(command=='a'):
        run()
    elif command=="":
        talk("Say again!")
        run()
    elif 'play' in command:
        song = command.replace('song','').replace('play','')
        #print(song)
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
            #print(time)
        else:
            talk("sorry")

    elif 'date' in command:
        date=datetime.datetime.today().strftime('%A, %d %B %Y')
        talk('the current date is..'+date)
        #print(date)

    elif "open"in command:
        if 'gpt' in command:
            talk("Here is your result")
            open_website(command.lstrip(' '))
        elif 'google' in command:
            talk("Here is your result")
            open_website(command.lstrip(' '))
        elif'youtube' in command:
             talk("Here is your result")
             open_website(command.lstrip(' '))

    elif "exit" in command:
        print("Exiting the program.")
        exit
    else:
        talk('please say the command again.......')
        run()
run()