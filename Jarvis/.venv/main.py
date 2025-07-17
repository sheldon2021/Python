import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os


NEWS_API_KEY = "149d998acb8549ba8c534045d35faa49"
OPENAI_API_KEY = "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"
client = OpenAI(api_key=OPENAI_API_KEY)

# pip install pocketsphinx

recognizer = sr.Recognizer()
engine = pyttsx3.init() 
# newsapi = "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"

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3') 

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3") 

def aiProcess(command):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
            {"role": "user", "content": command}
        ]
    )
    return completion.choices[0].message.content

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Print the headlines
            for article in articles:
                speak(article['title'])

    else:
        # Let OpenAI handle the request
        output = aiProcess(c)
        speak(output) 





if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
         
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Ya")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)


        except Exception as e:
            print("Error; {0}".format(e))


#             # ChatGPT said:
# Absolutely! Let's go step by step through your speak(text) function and explain what each line does, why it's needed, and what is happening.

# 🔊 Purpose of This Function
# This function converts text into speech using:

# ✅ gTTS (Google Text-to-Speech) to generate the audio

# ✅ pygame to play the audio

# 📜 Code Breakdown
# python
# Copy
# Edit
# def speak(text):
# Defines a function called speak that takes text (a string).

# This text is the message you want the computer (Jarvis) to say out loud.

# python
# Copy
# Edit
#     tts = gTTS(text)
# Calls Google Text-to-Speech (gTTS) and passes your text into it.

# This creates a tts object that holds the speech audio.

# 🧠 Think of it like:

# “Google, read this text and prepare the audio for it.”

# python
# Copy
# Edit
#     tts.save('temp.mp3') 
# Saves the speech audio to a file called 'temp.mp3'.

# 🔊 This MP3 will later be played using Pygame.

# python
# Copy
# Edit
#     pygame.mixer.init()
# Initializes Pygame’s audio system (the mixer).

# Without this, you can’t play any sound.

# ✅ Must be done before loading or playing sound.

# python
# Copy
# Edit
#     pygame.mixer.music.load('temp.mp3')
# Loads the 'temp.mp3' file into the music player.

# python
# Copy
# Edit
#     pygame.mixer.music.play()
# Starts playing the MP3 file.

# 🧠 At this point, the speech is being heard through the speakers.

# python
# Copy
# Edit
#     while pygame.mixer.music.get_busy():
#         pygame.time.Clock().tick(10)
# What this does:
# pygame.mixer.music.get_busy() returns True while the audio is still playing.

# This loop keeps the program running until the sound is done.

# pygame.time.Clock().tick(10) slows down the loop to run at 10 frames per second to reduce CPU usage.

# 🧠 Without this loop, the script might end too fast, and the audio wouldn’t play fully.

# python
# Copy
# Edit
#     pygame.mixer.music.unload()
# This line unloads the music from memory.

# 🧹 It’s like closing the audio file after using it — good for memory management.

# ❗️Note: This line may raise an error in some versions of Pygame if unload() doesn't exist. You could safely skip it if needed.

# python
# Copy
# Edit
#     os.remove("temp.mp3")
# Deletes the 'temp.mp3' file after playing.

# 🧼 Cleans up temporary files so your project folder doesn't fill up with useless MP3s.

# ✅ Summary
# Line	What It Does
# gTTS(text)	Turns text into audio (using Google)
# .save('temp.mp3')	Saves audio to a temporary file
# pygame.mixer.init()	Sets up audio playback
# .load() + .play()	Plays the MP3
# while get_busy()	Waits until it's done playing
# .unload()	Unloads the file from memory
# os.remove()	Deletes the temporary file


#  What Does Jarvis Do?
# A basic Jarvis AI assistant typically:

# Listens to your voice

# Recognizes what you said (speech-to-text)

# Processes your request (e.g., ask OpenAI or perform a task)

# Responds out loud (text-to-speech)

# 🧱 Typical Structure of the Code
# Here’s the complete breakdown step-by-step:

# ✅ 1. Import Libraries
# python
# Copy
# Edit
# import speech_recognition as sr
# import pyttsx3
# import os
# import pygame
# from gtts import gTTS
# import openai
# speech_recognition – converts voice to text

# pyttsx3 – speaks text offline

# gTTS – speaks text online (Google)

# pygame – plays audio (MP3)

# openai – sends user’s question to ChatGPT (AI)

# ✅ 2. Initialize Engines
# python
# Copy
# Edit
# engine = pyttsx3.init()
# openai.api_key = "your_api_key_here"
# engine is the pyttsx3 text-to-speech voice system.

# You must set your OpenAI API key to use GPT.

# ✅ 3. Take User’s Voice Command
# python
# Copy
# Edit
# def takeCommand():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         audio = recognizer.listen(source)

#     try:
#         print("Recognizing...")
#         command = recognizer.recognize_google(audio)
#         print(f"You said: {command}")
#         return command.lower()
#     except Exception as e:
#         print("Sorry, I didn't get that.")
#         return ""
# 🔊 This function:

# Listens to the mic

# Converts speech to text

# Returns that text as a string

# ✅ 4. AI Process (ChatGPT Request)
# python
# Copy
# Edit
# def aiProcess(text):
#     completion = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",  # or "gpt-4"
#         messages=[
#             {"role": "user", "content": text}
#         ]
#     )
#     return completion.choices[0].message.content
# 🤖 This function:

# Sends your question (text) to ChatGPT

# Gets the response from the assistant

# Returns the text of the reply

# ✅ 5. Speak Out Loud
# python
# Copy
# Edit
# def speak(text):
#     tts = gTTS(text)
#     tts.save('temp.mp3')
#     pygame.mixer.init()
#     pygame.mixer.music.load('temp.mp3')
#     pygame.mixer.music.play()
#     while pygame.mixer.music.get_busy():
#         pygame.time.Clock().tick(10)
#     pygame.mixer.music.unload()
#     os.remove("temp.mp3")
# 🗣️ This function:

# Converts text into speech using Google

# Plays the speech out loud

# Deletes the temp file afterward

# ✅ 6. Main Loop (The Brain)
# python
# Copy
# Edit
# if __name__ == "__main__":
#     while True:
#         command = takeCommand()

#         if "stop" in command:
#             speak("Goodbye!")
#             break

#         elif "open youtube" in command:
#             os.system("start https://youtube.com")

#         else:
#             output = aiProcess(command)
#             speak(output)
# 🧠 Here's what it does:

# Keeps listening forever

# If you say "stop", it exits

# If you say "open youtube", it opens the website

# Otherwise, it sends your command to ChatGPT, gets a reply, and speaks it

# 🧩 How It All Connects
# Task	Function Used
# Listen to voice	takeCommand()
# Understand your input	recognize_google()
# Process AI reply	aiProcess(command)
# Speak the response	speak(output)

# ✅ Final Summary
# Jarvis listens, understands, thinks (with AI), and responds out loud. It’s made by combining:

# Speech Recognition

# OpenAI GPT

# Text-to-Speech

# Would you like me to show you the complete working code in one file? Or break it into pieces with exercises?