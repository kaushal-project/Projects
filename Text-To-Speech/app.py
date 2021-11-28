# 

from gtts import gTTS
import os

def Text_To_Speech(myText,language):
    output = gTTS(text=myText,lang=language,slow=False)

    outputPath = os.getcwd() + "/Text-To-Speech/output/" + language + "-language.mp3"

    output.save(outputPath)


# myText = "Hello !! My name is kaushal"
myText = '''
it's all right
'''
language = "ja"

Text_To_Speech(myText,language)
