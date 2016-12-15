from gtts import gTTS
from playsound import playsound


# Convert text to speech using gTTS
def say(message,selected_language):
    speech = gTTS(text=message, lang=selected_language)
    speech.save("audio/temp.mp3")
    playsound("audio/temp.mp3")

# Welcome message
print "Hi, I'm PronounceAssist!"
playsound("audio/welcome.mp3")

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

