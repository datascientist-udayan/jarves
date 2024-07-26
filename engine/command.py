import pyttsx3
import speech_recognition as sr

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Set the voice to the first voice in the list
    engine.setProperty('rate', 175)
    engine.say(text)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        # eel.DisplayMessage('listening....')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        
        audio = r.listen(source, timeout=10, phrase_time_limit=6)

    try:
        print('Recognizing...')
        # eel.DisplayMessage('recognizing....')
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
        # eel.DisplayMessage(query)
        # time.sleep(2)
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

if __name__ == "__main__":
    text = takecommand()
    if text:
        speak(text)
    else:
        speak("I didn't understand what you said. Please try again.")
