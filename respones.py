from audioRecog import recognize_speech
import audioRecog
from playsound import playsound
from pathlib import Path
def Res():
    global audioRecog
    recognize_speech()

    # condition

    if audioRecog.text == "helo":
        pass
    elif audioRecog.text == "hello":
        playsound(".vscode/assets/hel-1v.mp3")
    elif audioRecog.text == "hai":
        playsound(".vscode/assets/hel-2v.mp3")
    elif audioRecog.text == "Apa hobi anda":
        playsound(".vscode/assets/es-v1.mp3")
    elif audioRecog.text == "Apa hobimu":
        playsound(".vscode/assets/es-v1.mp3")
    else:
        playsound(".vscode/assets/Ndata.mp3")