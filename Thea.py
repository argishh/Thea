#####        This is an program which works on user's Voice Commands!            #####
#####        Just like an Personal Assistant, Its got its own name -- Thea!      #####
#####        This program has its own voice and can speak to reply!              #####

''' 
This program can specifically open:
     -- Google
     -- Yahoo
     -- Youtube
     -- Netflix
     -- Gmail
     -- Stackoverflow
     -- Spotify 
     -- Wikipedia
     -- Twitter
     -- Facebook
     -- Instagram
     -- Reddit
     -- Amazon
     -- Flipkart
     -- Python(IDLE)
     -- Visual Studio Code (VSCode)

This program can also:
     -- Perform a wikipedia search
    -- Perform a google search
     -- Tell the time
     -- Play Music
     -- Send an email
     -- Tell a random number
     -- Crack a Joke
     -- Can reply to certain keywords
'''

#  To search on wikipedia, say "Search <topic> on wikipedia". 
#  To play music, say "Play Music". This will play a random song from the folder assigned.

#  Importing Modules

import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import random
import re
import randomSong

# Defining text to speech engine and properties
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-15)

# Defining Functions

def speak(audio):

    print(audio,'\n')
    engine.say(audio)
    engine.runAndWait()


def WishMe():

    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak('Good Morning!')

    elif hour>=12 and hour<18:
        speak('Good Afternoon!')   

    else:
        speak('Good Evening!')  

    speak('I am Thea! How may I help you sir?') 


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('\nListening...')
        r.pause_threshold = 0.5
        audio = r.listen(source)
        # audio = input('Enter: ')      # For testing purpose

    try:
        print("\nRecognizing...")    
        query = r.recognize_google(audio, language='en-us')
        # query = audio                 # For testing purpose
        print(f"\nUser said: {query}")

    except Exception as e:
        print('\nSay that again please...')  
        return 'None'
    return query


def SendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your_email_id@gmail.com', 'your_password')    # Using password here is not safe. I reccomend storing it in your environment variables.
    server.sendmail('your_email_id@gmail.com', to, content)
    server.close()

def mathgame():
    global name
    global num1
    import random
    if num1 == 0:
        number = random.randint(0,9999)
        num1 = number
    else:
        number = num1
    print(f'Your Number is: {number}\n')
    guess = int(input('Add or Subtract: '))
    if guess<0:
        ans = number + guess 
        print(f'\n{number} - {guess} = {ans}')
    else:
        ans = number + guess 
        print(f'\n{number} + {guess} = {ans}')
    
    j = ''
    a = str(ans)
    z = a[0]
    length = len(a)

    while length!=0:
        j += z
        length -= 1

    if int(ans) != int(j) :
        print('\nThat is Incorrect!\n') 
        print('Try again!\n')
        mathgame()
    elif int(ans) == int(j):
        print(f'That is Correct!\nWell Done {name}!\n')
        choice()
    return ''

def choice():
    global num1
    print('\nPress 1 to restart\nPress 2 to exit\n')
    query = re.sub('[a-zA-z,.:()" "]','',query)
    if query == 'one':
        query = 1
    elif query == 'two':
        query = 2
    if query == 1:
        num1 = 0
        mathgame()
    if query == 2:
        exit()
    else:
        print("Enter a valid selection!",choice())

# Main program starts from Here!
# An infinite while loop is made, which will keep on listening to user's commands.

if __name__ == '__main__':
    speak('Online!')  

    WishMe()

    speak("Try asking 'What can you do?' ")

    while True:
        query = takeCommand().lower()

        if 'thea' in query:
            speak("Yes Sir i'm right here, what can I do for you?")
        
        elif 'hi' in query:
            speak('Hi Sir, How are you?')
        
        elif 'fine' in query:
            speak("I'm Glad you are fine Sir!")

        elif 'thank you' in query:
            speak('Its my Honour Sir!')

        elif 'hey thea' in query:
            speak(f'Hello Sir, What can I do for you?')

        elif 'who are you' in query:
            speak('I am Thea, Your personal Artificial Intellegence!') 

        elif 'what can you do' in query:
            speak('I can perform a wikipedia search, open youtube, spotify and many more websites!')
            
            speak('I can send an email!')
            
            speak('I can play music for you, or tell a joke!')
            
            speak('I can pick a random number for you!')
           
            speak('I can also tell you the time, and much more')

        elif 'open wikipedia' in query:
            speak('Opening Wikipedia!')
            webbrowser.open('wikipedia.com')
        
        elif 'open youtube' in query:
            speak('Opening Youtube!')
            webbrowser.open('youtube.com')

        elif 'open netflix' in query:
            speak('Opening Netflix!')
            webbrowser.open('netflix.com')
        
        elif 'open google' in query:
            speak('Opening Google!')
            webbrowser.open('google.com')

        elif 'open stackoverflow' in query:
            speak('Opening Stackoverflow!')
            webbrowser.open('stackoverflow.com')
        
        elif 'open gmail' in query:
            speak('Opening Gmail!')
            webbrowser.open('gmail.com')

        elif 'open yahoo' in query:
            speak('Opening Yahoo!')
            webbrowser.open('yahoo.com')

        elif 'open reddit' in query:
            speak('Opening Reddit!')
            webbrowser.open('reddit.com')
        
        elif 'open spotify' in query:
            speak('Opening Spotify!')
            webbrowser.open('spotify.com')

        elif 'open twitter' in query:
            speak('Opening Twitter!')
            webbrowser.open('twitter.com')

        elif 'open facebook' in query:
            speak('Opening Facebook!')
            webbrowser.open('facebook.com')

        elif 'open instagram' in query:
            speak('Opening Instagram!')
            webbrowser.open('instagram.com')

        elif 'open amazon' in query:
            speak('Opening Amazon!')
            webbrowser.open('amazon.com')

        elif 'open flipkart' in query:
            speak('Opening Flipkart!')
            webbrowser.open('flipkart.com')

        elif 'open whatsapp' in query:
            speak('Opening Whatsapp!')
            webbrowser.open('web.whatsapp.com')

        elif 'open translate' in query:
            speak('Opening Google Translate!')
            webbrowser.open('translate.google.co.in')

        elif 'open google drive' in query:
            speak('Opening Google Drive!')
            webbrowser.open('drive.google.com')

        elif 'open code' in query: 
            speak('Opening VScode!')
            codePath = "Path to VSCode on your system"  # Reference path is below
            # codePath = "C:\\Users\\User\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        elif 'open python' in query:
            speak('Opening Python!')
            path = "Path to python idle on your system" # Reference path is below
            # path = "C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python38-32\\Lib\\idlelib\\idle.pyw"
            os.startfile(path)

        elif 'wikipedia' in query: 
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia', '', 1)
            results = wikipedia.summary(query, sentences=5)
            speak('According to Wikipedia')
            speak(results)

        elif 'play music' in query: 
            speak('Playing Music!')
            music_dir ='F:\\Music'      # Enter your music directory here.
            songs =os.listdir(music_dir)
            random_music = random.randint(0,len(songs)-1)
            os.startfile(os.path.join(music_dir, songs[random_music]))

        elif 'a joke' in query: 
            speak('Okay') or speak("Here's One")
            jokes= open(jokes.txt).read().splitlines()
            random_joke = random.choice(jokes)
            speak(random_joke)
            
            # Most of my jokes/ puns are from https://parade.com/1040121/marynliles/one-liners/ 
            # Thanks a chunk @marynliles! saved me time to come up with jokes and puns myself!

        elif 'the time' in query: 
            strTime = datetime.datetime.now().strftime('%H:%M:%S')    
            speak(f'The time is {strTime}')

        elif 'send email' in query:  
            try:
                speak('What should I say?')
                content = takeCommand()
                MailTo = input("reciever's email: ")  # Reciever's email is to be entered manually to reduce chances of sending mail to wrong email-address.
                SendEmail(MailTo, content)
                speak('Email has been sent!')
            except Exception as e:
                print(e)                              # To check the error faced while sending the email.
                speak('Failed to send the email.') 

        elif 'random number' in query:
            ranint = random.randint(0,100)
            speak(ranint)

        elif 'youtube' in query:
            speak("Searching Youtube!")
            query = query.replace('search','', 1)
            query= query.replace('youtube','', 1)
            webbrowser.open(f"https://www.youtube.com/results?search_query={query}")

        elif 'search' and 'google' in query:
            query = query.replace('search','', 1)
            query = query.replace('google','', 1)
            webbrowser.open(f'https://www.google.com/search?q={query}')
        # eg:you wanna search 'python' on google, then speak,"Search Python Google" OR "google search python" OR vice versa
        
        elif 'math game' in query:
            num1 = 0
            name = input('Enter your Name: ')
            print('\nHow To Play?\n\nAdd or subtract a number of your choice to create a repeating number.\nFor eg. 1111 or 888 or 44 \n')
            mathgame()

        elif 'bye' in query:
            speak('Bye Sir! Have a good day!')
            exit()
