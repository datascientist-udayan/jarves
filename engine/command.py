import pyttsx3
import speech_recognition as sr
import time
import eel

@eel.expose
def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Set the voice to the first voice in the list
    engine.setProperty('rate', 175)
    engine.say(text)
    engine.runAndWait()

# @eel.expose
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening ...')
        eel.DisplayMessage('Listening ...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        
        audio = r.listen(source, timeout=10, phrase_time_limit=6)

    try:
        print('Recognizing...')
        eel.DisplayMessage('Recognizing ...')
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
        eel.DisplayMessage(query)
        speak(query)
        # time.sleep(5)
        # eel.ShowHood()
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""
    except Exception as e:
        print(f"An error occurred: {e}")
        return ""
    
    return query.lower()

@eel.expose
def chat():
    Talk = True
    while Talk == True:
        userSaid = takeCommand()
        if "hello" in userSaid:
            speak("hello")
        if "bye" in userSaid:
            speak("goodbye")
        if "how are you" in userSaid:
            speak("Doing well")
        if "stop" in userSaid:
            speak("Stopping sir")
            break
        if "exit" in userSaid:
            speak("ending program")
            break
    eel.ShowHood()
    time.sleep(2)