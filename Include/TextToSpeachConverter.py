from gtts import gTTS 
import os  
from io import BytesIO
import pyttsx3
 
        
class TextToSpeachConverterPyttsx3:
    
    def ConvertAndPlay(self, textToConvert : str):
        
        engine = pyttsx3.init() 
        engine.say(textToConvert)

        engine.runAndWait()
        

        