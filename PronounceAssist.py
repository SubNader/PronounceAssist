from gtts import gTTS
from playsound import playsound
import os
import vlc

# Convert text to speech using gTTS
def say(message,selected_language):
    speech = gTTS(text=message, lang=selected_language)
    speech.save("audio/temp.mp3")
    play("audio/temp.mp3")


# Play file with cross-platform handling
def play(path):
	try:
		vlc.MediaPlayer(path).play()
	except:
		print "VLC is not installed."


# Welcome message
print "Hi, I'm PronounceAssist!"
play("audio/welcome.mp3")

# Set language (English / Arabic)
language_input = raw_input("Enter 'English' or 'Arabic': ").lower()
while language_input != 'english' and language_input != 'arabic':
    language_input = raw_input("Invalid language choice. Enter 'English' or 'Arabic': ").lower()
if language_input == 'english':
    language = 'en-US'
else:
    language = 'ar'

# Fetch and pronounce input indefinitely
while True:
    message = raw_input("Text: ")
    if message != '':
        say(message,language)

