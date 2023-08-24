import os
from pygame import mixer
from gtts import gTTS
import time

my_file=open('some.txt','r',encoding='utf-8')
my_string=my_file.read()

my_file.close()

mixer.init()

tts=gTTS(text=my_string,lang='ru')
tts.save('hello.mp3')
mixer.music.load('hello.mp3')
mixer.music.play()
while mixer.music.get_busy():
    time.sleep(1)
mixer.music.unload()
os.remove('hello.mp3')
