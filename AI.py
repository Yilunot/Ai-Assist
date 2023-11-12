#AI Assistant
#python 3.11.6
#speech to text and text to speech
#pip install SpeechRecognition
#pip install pyttsx3
#pip install python-dotenv
#pip install openai


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
	
	# Initialize the engine
	engine = pyttsx3.init()
	engine.say(command) 
	engine.runAndWait()

# File to store transcriptions
transcription_file = "transcriptions.txt"

def save_transcription(role,text):
    with open(transcription_file, "a") as file:
        file.write(f"{role.capitalize()}: {text}\n")
	
# Loop infinitely for user to
# speak
def record_text():
    while True:
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                print("Say Hey Ian")
                audio2 = r.listen(source2, timeout=5)
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