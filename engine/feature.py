from playsound import playsound
import eel
import os
from engine.config import ASSISTANT_NAME

@eel.expose
def playAssistantSound():
    music_dirt = "www//assets//audio//start_sound.mp3"
    playsound(music_dirt)

def opencommand(quary):
    quary = quary.replace(ASSISTANT_NAME,"")
    quary = quary.replace("open","")
    quary.lower()
    
    if quary!="":
        speak("Opening ",+quary)
        os.system('start '+ quary)
    else:
        speak("not found")