import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser as wb
import os



wb.register('chrome', None)
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good evening!")
    speak("I am Jarvis Sir. Please tell me how may I help you")

def takeCommand():

    # it takes microphone input from yhe user and returns string output

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening......")
        r.adjust_for_ambient_noise(source, duration=1)
        r.pause_threshold = 1
        
        audio=r.listen(source)
    try:
        print("Recognizing....")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said:{query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    # while True:
    if 1:
        query=takeCommand().lower()

        if 'wikipedia'in query:
            speak("Searching Wikipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=3)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube'in query:
            wb.open('https://www.youtube.com')
        elif 'open google' in query:
            wb.open("https://www.google.com")
        elif 'play music' in query:
            music_dir="C:\\Users\\Dell\\Desktop\\thapa\\Chat_Application\\assets"
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[2]))
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'open code' in query:
            codePath="C:\\Users\\Dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
     
