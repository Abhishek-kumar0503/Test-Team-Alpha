# importing the module
from cgitb import text
from re import X
from tkinter import Variable
from youtube_transcript_api import YouTubeTranscriptApi
from gtts import gTTS
import time
import os
# retrieve the available transcripts
transcript_list = YouTubeTranscriptApi.list_transcripts('4EuuL4utvAs')
# iterate over all available transcripts
m = []
for transcript in transcript_list:
 #print(transcript.fetch())
 m.append(transcript.translate('hi').fetch())

mytext=[]
# to print only text from the fetched transcript (either original or translated)
for i in m:
    for x in i:
        print(x['text'])
        mytext.append(x['text'])

#print(mytext)
# Language we want to use 
#language = 'hi'
#myobj = gTTS(text=mytext, lang=language, slow=False) 
#myobj.save("output.mp3") 
  
# Play the converted file 
#os.system("start output.mp3")

