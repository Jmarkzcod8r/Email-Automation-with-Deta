# Python program to translate
# speech to text and text to speech
 
 
# import speech_recognition as sr
# import pyttsx3
 
# # Initialize the recognizer
# r = sr.Recognizer()
 
# # Function to convert text to
# # speech
# def SpeakText(command):
     
#     # Initialize the engine
#     engine = pyttsx3.init()
#     engine.say(command)
#     engine.runAndWait()
     
     
# # Loop infinitely for user to
# # speak
 
# while(1):   
     
#     # Exception handling to handle
#     # exceptions at the runtime
#     try:
         
#         # use the microphone as source for input.
#         with sr.Microphone() as source2:
             
#             # wait for a second to let the recognizer
#             # adjust the energy threshold based on
#             # the surrounding noise level
#             r.adjust_for_ambient_noise(source2, duration=0.2)
             
#             #listens for the user's input
#             audio2 = r.listen(source2)
             
#             # Using google to recognize audio
#             MyText = r.recognize_google(audio2)
#             MyText = MyText.lower()
 
#             print("Did you say "+MyText)
#             SpeakText(MyText)
             
#     except sr.RequestError as e:
#         print("Could not request results; {0}".format(e))
         
#     except sr.UnknownValueError:
#         print("unknown error occured")


# ______________________________________________________________________________________________________

# Import the required module for text 
# to speech conversion
from gtts import gTTS
  
# This module is imported so that we can 
# play the converted audio
import os
  
# The text that you want to convert to audio
# mytext = 'Welcome to geeksforgeeks! This is awesome'

mytext = f"Daniel in the lions' den (chapter 6 of the Book of Daniel) tells of how the biblical Daniel is saved from lions by the God of Israel 'because I was found blameless before him' (Daniel 6:22).[2] It "
# Language in which you want to convert
language = 'en'
  
# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)
  
# Saving the converted audio in a mp3 file named
# welcome 
myobj.save("welcome.mp3")
  
# Playing the converted file
os.system("mpg321 welcome.mp3")

# os.system("start hello.mp3")

# ----------------------------------------------------------------------------------------------------------------------

# # Python program to show
# # how to convert text to speech
# import pyttsx3
  
# # Initialize the converter
# converter = pyttsx3.init()
  
# # Set properties before adding
# # Things to say
  
# # Sets speed percent 
# # Can be more than 100
# converter.setProperty('rate', 150)
# # Set volume 0-1
# converter.setProperty('volume', 0.7)
  
# # Queue the entered text 
# # There will be a pause between
# # each one like a pause in 
# # a sentence
# converter.say("Hello GeeksforGeeks")
# converter.say("I'm also a geek")
  
# # Empties the say() queue
# # Program will not continue
# # until all speech is done talking
# converter.runAndWait()