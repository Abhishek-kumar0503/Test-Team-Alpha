# Import the Gtts module for text  
# to speech conversion 
from gtts import gTTS 
  
# import Os module to start the audio file
import os 
  
mytext = '''इस वीडियो में मैं आपको
सबटाइटल सिंक इश्यू को हल करने के लिए दो तरीके दिखाने जा रहा हूं
, आइकन पर राइट-क्लिक करके नोटपैड के साथ ओपन सबटाइटल फाइल, फिर ओपन विथ पर क्लिक करें
और नोट पेट चुनें पहला
कदम एक डायलॉग चुनना और उसके समय की जांच करना है
'''
  
# Language we want to use 
language = 'hi'
  
myobj = gTTS(text=mytext, lang=language, slow=True) 
  

myobj.save("output.mp3") 
  
# Play the converted file 
os.system("start output.mp3") 