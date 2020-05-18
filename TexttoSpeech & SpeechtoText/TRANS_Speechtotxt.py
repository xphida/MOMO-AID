# -*- coding: utf-8 -*-
"""
Created on Fri May  8 14:33:15 2020

@author: xphid
"""


import speech_recognition as sr
# referenze libreria: https://github.com/Uberi/speech_recognition/blob/master/reference/library-reference.rst#speech-recognition-library-reference
from googletrans import Translator

text= str()
recognizer_instance = sr.Recognizer() # Crea una istanza del recognizer

with sr.Microphone() as source:
    recognizer_instance.adjust_for_ambient_noise(source)
    print("I'm listening ...")
    audio = recognizer_instance.listen(source)
    print("Ok! I'm loading the message!")
try:
    text = recognizer_instance.recognize_google(audio, language="en-EN")
    print("Google understood: \n", text)
except Exception as e:
    print(e)
    
translator = Translator()
translated = translator.translate(text, dest='it', src='en') #posso 

print(translated.text)