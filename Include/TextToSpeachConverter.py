from json import decoder
import os
os.environ['SDL_AUDIODRIVER'] = 'dsp'
from io import BytesIO
import pyttsx3
from gtts import gTTS 
from playsound import playsound
from pathlib import Path
import pygame
import pyglet
import time


class TextToSpeachConverterPyttsx3:
    
    def ConvertAndPlay(self, textToConvert : str):
        
        engine = pyttsx3.init() 
        engine.say(textToConvert)

        engine.runAndWait()
        
        
class TextToSpeachConverterGtts:
       
    def ConvertAndPlay(self, textToConvert : str, language : str = 'pt-br'):
        
        BASE_DIR = Path(__file__).resolve().parent.parent
        staticRoot = os.path.join(BASE_DIR,'staticfiles')
        # outputFileName = os.path.join(staticRoot,'output.mp3')
        outputFileName = BytesIO()
        # outputFileName = TemporaryFile()
        myObj = gTTS(text=textToConvert, lang= str(language), slow=False)   
        # myObj.save(outputFileName) 
        myObj.write_to_fp(outputFileName)   
        outputFileName.seek(0)

        # playsound(outputFileName)


        # pygame.init()
        # pygame.mixer.init()
    
        # pygame.mixer.music.load(outputFileName, 'mp3')
        # pygame.mixer.music.play()

        # while pygame.mixer.music.get_busy():
        #     pygame.time.Clock().tick(10)

        from pyglet.media.codecs import gstreamer
        
        music = pyglet.media.load("", outputFileName, streaming=False )
        music.play()
        pyglet.app.run()


        time.sleep(music.duration) #prevent from killing


        # os.remove(outputFileName)


    



        