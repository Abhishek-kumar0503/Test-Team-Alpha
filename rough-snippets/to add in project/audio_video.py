# importing the module

from cgitb import text
from re import S
from tkinter import Variable
from gtts import gTTS
from youtube_transcript_api import YouTubeTranscriptApi
import time
import os
import pytube
# Import everything needed to edit video clips
from moviepy.editor import *

# retrieve the available transcripts

v="tlcaQgc4QW0"
transcript_list = YouTubeTranscriptApi.list_transcripts(v)
# iterate over all available transcripts
m = []
for transcript in transcript_list:
 #print(transcript.fetch())
 m.append(transcript.translate('hi').fetch())

ask = ''
# to print only text from the fetched transcript (either original or translated)

for i in m:
    #if i==m[0]:
       # ask += "'''"
        #print("'''", end="")
    for x in i:
        ask += "\t"+x['text']+"\n"
        ask += ' '
        #print(x['text'])
        x['text']
    #if i==m[-1]:
       # ask += "'''"
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
myobj.save("output01.mp3") 
  # Play the converted file 
#os.system("output01.mp3") 

link = "https://www.youtube.com/watch?v="+v 
yt = pytube.YouTube(link)
stream = yt.streams.get_highest_resolution()
stream.download()