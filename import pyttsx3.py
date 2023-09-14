import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[7].id)
engine.setProperty('rate', 170)


def Speak(Audio):
    print(f": {Audio}")
    engine.say(Audio)
    engine.runAndWait()


def takecommand(): 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"Your Command :  {query}\n")
    except:   
        return None
    return query.lower()


def TaskExe():
    while True:
        query = takecommand()
        if 'hello' in query:
            Speak("Hello Sir, How Are You ?")
        else:
            Speak("No Command Found!")
