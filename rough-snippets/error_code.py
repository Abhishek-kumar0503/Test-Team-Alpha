# importing the module
from cgitb import text
from re import X
from tkinter import Variable
from youtube_transcript_api import YouTubeTranscriptApi
from gtts import gTTS
import time
import os
# retrieve the available transcripts
transcript_list = YouTubeTranscriptApi.list_transcripts('C2tjnJOy7Hw')
# iterate over all available transcripts
m = []
for transcript in transcript_list:
 #print(transcript.fetch())
 m.append(transcript.translate('hi').fetch())
 language = 'hi'
mytext=[]
# to print only text from the fetched transcript (either original or translated)
for i in m:
    for x in i:
        print(x['text'])
        mytext.append(x['text'])
#print(mytext)
myobj = gTTS(text=mytext, lang=language, slow=True)
myobj.save("audiotest1.mp3")
os.system("audiotest1.mp3")