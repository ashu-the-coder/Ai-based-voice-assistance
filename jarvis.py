import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser
import os
import smtplib

engin=pyttsx3.init('sapi5')
voices = engin.getProperty('voices')
# print(voices[0].id)
engin.setProperty('voice',voices[0].id)

def speak(audio):
    engin.say(audio)
    engin.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour is hour>=0 and hour<12:
        speak("Good Morning!")
    
    elif hour>=12 and hour<18:
        speak("Good Evening!")
    speak("I am Jarvis sir. Please tell me how may I help you")

def takeCommand():
    #it takes microphone input from user and returning string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio,language = 'en-in')
        print(f"User said:{query}\n")

    except Exception as e:
        print(f"Error:{e}")

        print("Say that again please ....")
        speak("Say that again please .....")
        return "None"
    return query



def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("youremail@email.com", 'password')                   #update email and password
    server.sendmail('ashutoshaianule@gmail.com', to, content)
    server.close()




    
if __name__ == "__main__":
    wishMe()
    while True:
        query =takeCommand().lower()

        # Logic executing tasks based on query 
        if 'wikipedia' in query:
            speak('Searching wikipedia ...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            # print(results)
            speak(results)

        elif "open youtube" in query:
            url="https://www.youtube.com"
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"  # Change this path based on your installation path
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open(url)

        elif "google" in query:
            url="https://www.google.com"
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"  # Change this path based on your installation path
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open(url)

        elif "stack overflow" in query:
            url="https://stackoverflow.com/"
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"  # Change this path based on your installation path
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open(url)

        elif "play music" in query:
            music_dir ="c:"             #Give music file path
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir , songs[0]))
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%h:%M:%S")
            speak(f" sir,The time is{strTime}")

        elif "open code " in query:
            code_path ="C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)

        elif "email to ashu" in query:
            try:
                speak("whats should I say?")
                content = takeCommand()
                to ="senderemail@email.com"                  #update email to send email
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry my friend ashu bhai. I am not able to send this email")
        
        elif "quit" in query:
            exit()

                