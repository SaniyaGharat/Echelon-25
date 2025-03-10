import os
import random
import speech_recognition as sr
from gtts import gTTS
import pygame
import time

def speak(text):
    filename = f'voice_{int(time.time())}.mp3'
    tts = gTTS(text=text, lang='en')
    tts.save(filename)

    # Initialize pygame mixer
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    
    # Wait until the sound has finished playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    # Clean up
    pygame.mixer.music.stop()
    pygame.mixer.quit()
    os.remove(filename)

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service.")
            return ""

def respond(command):
    if "hello" in command:
        return "Hey, Lishang Gajendra; How can I assist you today?"
    elif "your name" in command:
        return "I am a simple AI chatbot created to assist you."
    elif "how are you" in command:
        return "I'm just a program, but thanks for asking!"
    elif "bye" in command:
        return "Goodbye! Have a great day!"
    else:
        return "I'm not sure how to respond to that."

def main():
    print("Chatbot is ready! You can start talking to it.")
    speak("Hey, Lishang Gajendra; How can I assist you today?")
    
    while True:
        command = listen()
        if command:
            response = respond(command)
            speak(response)
            if "bye" in command:
                break

if __name__ == "__main__":
    main()
