# -*- coding: utf-8 -*-
"""
Created on Fri May  8 01:23:54 2020

@author: xphid
"""

 
from gtts import gTTS
import subprocess 
import os
import time

text = """ ciao a tutti  !"""



tts = gTTS(text=text, lang='it')

tts.save("tts_output_audio.mp3")

print("tutto fatto, file salvato!")

"""
import pygame
from pygame import mixer
mixer.init()
mixer.music.load("tts_output_audio.mp3")
mixer.music.play()



"""


os.startfile("tts_output_audio.mp3")
time.sleep(3)

os.remove("tts_output_audio.mp3")