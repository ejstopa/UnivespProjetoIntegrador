import os  
from io import BytesIO
import pyttsx3
 
        
class TextToSpeachConverterPyttsx3:
    
    def ConvertAndPlay(self, textToConvert : str):
        
        engine = pyttsx3.init("sapi5") 
        engine.say(textToConvert)

        engine.runAndWait()
        

        