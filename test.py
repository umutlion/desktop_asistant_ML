import os
import time
import playsound
import portaudio
import speech_recognition as sr
from gtts import gTTS


def speak(text):

    tts = gTTS(text=text, lang="en-US")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception "+str(e))
    return said

speak("hello umut")
get_audio()
