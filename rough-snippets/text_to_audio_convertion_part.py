# importing the module
from cgitb import text
from re import S
from tkinter import Variable
from youtube_transcript_api import YouTubeTranscriptApi
import time
import os
# retrieve the available transcripts
transcript_list = YouTubeTranscriptApi.list_transcripts('mhkAkZXOD3A')
# iterate over all available transcripts
m = []
for transcript in transcript_list:
 #print(transcript.fetch())
 m.append(transcript.translate('hi').fetch())

ask = ''
# to print only text from the fetched transcript (either original or translated)

for i in m:
    if i==m[0]:
        ask += "'''"
        #print("'''", end="")
    for x in i:
        ask += x['text']
        ask += ' '
        #print(x['text'])
        x['text']
    if i==m[-1]:
        ask += "'''"
        #print("'''", end="\b")
        
print(ask)
# Import the Gtts module for text  
# to speech conversion 

  
# import Os module to start the audio file
import os 

# Language we want to use 
language = 'hi'
  
#for i in m:
#    if i==m[0]:
#        print("'''")
#    for x in i:
#        print(x['text'])
#    if i==m[-1]:
#        print("'''")
  
myobj=gTTS(text=ask,lang=language, slow=False)
myobj.save("output001.mp3") 
  # Play the converted file 
os.system("output001.mp3") 