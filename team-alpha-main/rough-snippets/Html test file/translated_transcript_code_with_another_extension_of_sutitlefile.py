# importing the module
from re import X
from tkinter import Variable
from youtube_transcript_api import YouTubeTranscriptApi
# retrieve the available transcripts
transcript_list = YouTubeTranscriptApi.list_transcripts('07yMvq5WxAs&ab')
# iterate over all available transcripts
for transcript in transcript_list:
 print(transcript.fetch())
 print(transcript.translate('hi').fetch())

with open("transcript.json", 'w', encoding='utf-8') as f:
   f.write("[")
   for i in transcript.translate('hi').fetch():
      f.write("{},\n".format(i))
   f.write("]")