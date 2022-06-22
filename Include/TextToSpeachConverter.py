import os  
from io import BytesIO
import pyttsx3
from gtts import gTTS 
from playsound import playsound
from pathlib import Path
 
        
class TextToSpeachConverterPyttsx3:
    
    def ConvertAndPlay(self, textToConvert : str):
        
        engine = pyttsx3.init() 
        engine.say(textToConvert)

        engine.runAndWait()
        
        
class TextToSpeachConverterGtts:
       
    def ConvertAndPlay(self, textToConvert : str, language : str = 'pt-br'):
        
        BASE_DIR = Path(__file__).resolve().parent.parent
        outputFileName = os.path.join(BASE_DIR, 'output.mp3')
        myObj = gTTS(text=textToConvert, lang= str(language), slow=False)   
        myObj.save(outputFileName)       

        playsound(outputFileName)
        os.remove(outputFileName)

        