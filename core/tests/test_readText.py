import pytest
from Include import TextToSpeachConverter
from django.http import JsonResponse

def readText(text):
    
    Convert = TextToSpeachConverter.TextToSpeachConverterGtts()
    Convert.ConvertAndPlay(text)
    data={'valor':'teste'}
    return JsonResponse(data)


def test_readTxt():
    try:
        readText("Teste conversão texto")
    except:
        pytest.fail("Ocorreu um erro na conversão do texto.")

