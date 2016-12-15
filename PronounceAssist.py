from gtts import gTTS
from playsound import playsound


# Convert text to speech using gTTS
def say(message,selected_language):
    speech = gTTS(text=message, lang=selected_language)
    speech.save("temp.mp3")
    playsound("temp.mp3")

# Welcome message
print "Hi, I'm PronounceAssist!"
playsound("welcome.mp3")

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
    say(raw_input("Text: "), language)

