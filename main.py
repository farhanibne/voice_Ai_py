from gtts import gTTS
import os
my_text = "welcome to DZ"
language = "en"
myobj = gTTS(text=my_text,lang=language,slow=False)
myobj.save('output.mp3')
os.system("mpg321 output.mp3")
