from gtts import gTTS
import os
from os import path

dosya=open("C:\Users\LENOVO\Desktop\azranınhikayesi.txt",encoding="utf-8")
yazı=dosya.read()
çikti=gTTS(text=yazı,lang='tr',slow=False)
çikti.save("azranınhikayesi.mp3")
os.system("azranınhikayesi.mp3")
dosya.close()
