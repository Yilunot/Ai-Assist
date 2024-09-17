#AI Assistant
#python 3.11.6
#speech to text and text to speech
#pip install SpeechRecognition
#pip install pyttsx3
#pip install python-dotenv
#pip install openai

#AI Assistant
#python 3.11.6
#speech to text and text to speech
#pip install SpeechRecognition
#pip install pyttsx3
#pip install python-dotenv
#pip install openai
#pip install PyAudio
#pip install setuptools

import speech_recognition as sr
import pyttsx3
import os
import subprocess
import webbrowser
from dotenv import load_dotenv
load_dotenv()
import openai
OPENAI_KEY = os.getenv('OPENAI_KEY')
openai.api_key = OPENAI_KEY


#error checking for API key
if OPENAI_KEY is None:
    raise ValueError("OPENAI_KEY environment variable is not set.")

# Python program to translate
# speech to text and text to speech

# Initialize the recognizer 
r = sr.Recognizer() 

# Function to convert text to
# speech
import pyttsx3

# Function to convert text to speech with a specified voice
def SpeakText(command, voice_id=None):
    try:
        # Initialize the engine
        engine = pyttsx3.init()
        
        # List available voices
        voices = engine.getProperty('voices')
        for i, voice in enumerate(voices):
            print(f"Voice {i}: {voice.name}")

        # Set the desired voice if specified
        if voice_id is not None:
            engine.setProperty('voice', voices[voice_id].id)
        else:
            # Set to default voice or the first available voice
            engine.setProperty('voice', voices[2].id)

        engine.say(command) 
        engine.runAndWait()
    except Exception as e:
        print(f"Error in SpeakText function: {e}")

# Example usage:
SpeakText("Hello, this is the default voice.")
# To use a different voice, pass the index of the desired voice:
SpeakText("Hello, this is a different voice.", voice_id=1)

# File to store transcriptions
transcription_file = "transcriptions.txt"

def save_transcription(role,text):
    try:
        with open(transcription_file, "a") as file:
            file.write(f"{role.capitalize()}: {text}\n")
    except Exception as e:
        print(f"Error saving transcription: {e}")
# Loop infinitely for user to
# speak
def record_text():
    while True:
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                print("Say Hey Jarvis")
                audio2 = r.listen(source2, timeout=10)
                wake_word = r.recognize_google(audio2).lower()
                

                if "hey jarvis" in wake_word:
                    print("Jarvis activated. Please speak...")
                    SpeakText("Yes Sir")
                    audio2 = r.listen(source2)
                    MyText = r.recognize_google(audio2)
                    return MyText

        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except sr.UnknownValueError:
            print("Waiting for your command")
        except Exception as e:
            print(f"Error in record_text function: {e}")


def open_application(application_name):
    try:
        if "notepad" in application_name.lower():
            subprocess.Popen(["notepad.exe"])
        if "spotify" in application_name.lower():
            subprocess.Popen(["C:\\Users\\Yilunot\\AppData\\Roaming\\Spotify\\spotify.exe"])
        elif "browser" in application_name.lower():
           webbrowser.open("https://www.google.com")
        elif "youtube" in application_name.lower():
           webbrowser.open("https://www.youtube.com")

        else:
            print(f"Unknown application: {application_name}")
    except Exception as e:
        print(f"Error opening {application_name}: {e}")


def send_to_chatGPT(messages, model= "gpt-3.5-turbo"):
    response = openai.ChatCompletion.create(
        model= model,
        messages = messages,
        max_tokens =200,
        n=1,
        stop=None,
        temperature = 0.5,
      )
    message = response.choices[0].message.content
    messages.append(response.choices[0].message)
    return message
   
   
messages = [{"role": "user","content": "You are an AI Assistant."}]

while True:
    try:
        text =record_text()
        messages.append({"role": "user","content": text})
        print(f"\x1b[31mMe:{text}\x1b[0m")
        save_transcription("Me:",text)

        if "open Notepad" in text:
            open_application("notepad")
        elif "open Spotify"in text:
            open_application("spotify")
        elif "open browser" in text:
            open_application("browser")
        elif "open YouTube" in text:
            open_application("youtube")
        elif "bye" in text:
            print(f"\x1b[32mAssistant:Good Bye\x1b[0m")
            break;
        else:
            print(f"\x1b[32mAssistant: Thinking...\x1b[0m")
            response = send_to_chatGPT(messages)
            print(f"\x1b[32mAssistant:{response}\x1b[0m")
            SpeakText(response)
            save_transcription("AI:",response)
    except KeyboardInterrupt:
        print("\nUser interrupted the program. Exiting.")
        break;

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
import speech_recognition as sr
import pyttsx3
import os
import subprocess
import webbrowser
from dotenv import load_dotenv
load_dotenv()
import openai
OPENAI_KEY = os.getenv('OPENAI_KEY')
openai.api_key = OPENAI_KEY


#error checking for API key
if OPENAI_KEY is None:
    raise ValueError("OPENAI_KEY environment variable is not set.")

# Python program to translate
# speech to text and text to speech

# Initialize the recognizer 
r = sr.Recognizer() 

# Function to convert text to
# speech
def SpeakText(command):
    try:
        # Initialize the engine
        engine = pyttsx3.init()
        engine.say(command) 
        engine.runAndWait()
    except Exception as e:
        print(f"Error in SpeakText function: {e}")

# File to store transcriptions
transcription_file = "transcriptions.txt"

def save_transcription(role,text):
    try:
        with open(transcription_file, "a") as file:
            file.write(f"{role.capitalize()}: {text}\n")
    except Exception as e:
        print(f"Error saving transcription: {e}")
# Loop infinitely for user to
# speak
def record_text():
    while True:
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                print("Say Hey Ian")
                audio2 = r.listen(source2, timeout=10)
                wake_word = r.recognize_google(audio2).lower()
                

                if "hey ian" in wake_word:
                    print("IAN activated. Please speak...")
                    audio2 = r.listen(source2)
                    MyText = r.recognize_google(audio2)
                    return MyText

        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except sr.UnknownValueError:
            print("Waiting for your command")
        except Exception as e:
            print(f"Error in record_text function: {e}")


def open_application(application_name):
    try:
        if "notepad" in application_name.lower():
            subprocess.Popen(["notepad.exe"])
        if "spotify" in application_name.lower():
            subprocess.Popen(["C:\\Users\\Yilunot\\AppData\\Roaming\\Spotify\\Spotify.exe"])
        elif "browser" in application_name.lower():
           webbrowser.open("https://www.google.com")
        elif "youtube" in application_name.lower():
           webbrowser.open("https://www.youtube.com")

        else:
            print(f"Unknown application: {application_name}")
    except Exception as e:
        print(f"Error opening {application_name}: {e}")


def send_to_chatGPT(messages, model= "gpt-3.5-turbo"):
    response = openai.ChatCompletion.create(
        model= model,
        messages = messages,
        max_tokens =200,
        n=1,
        stop=None,
        temperature = 0.5,
      )
    message = response.choices[0].message.content
    messages.append(response.choices[0].message)
    return message
   
   
messages = [{"role": "user","content": "You are an AI Assistant."}]

while True:
    try:
        text =record_text()
        messages.append({"role": "user","content": text})
        print(f"\x1b[31mMe:{text}\x1b[0m")
        save_transcription("Me:",text)

        if "open Notepad" in text:
            open_application("notepad")
        elif "open Spotify"in text:
            open_application("spotify")
        elif "open browser" in text:
            open_application("browser")
        elif "open YouTube" in text:
            open_application("youtube")
        elif "bye" in text:
            print(f"\x1b[32mAssistant:Good Bye\x1b[0m")
            break;
        else:
            print(f"\x1b[32mAssistant: Thinking...\x1b[0m")
            response = send_to_chatGPT(messages)
            print(f"\x1b[32mAssistant:{response}\x1b[0m")
            SpeakText(response)
            save_transcription("AI:",response)
    except KeyboardInterrupt:
        print("\nUser interrupted the program. Exiting.")
        break

    except Exception as e:
        print(f"An unexpected error occurred: {e}")