# importing the module
from youtube_transcript_api import YouTubeTranscriptApi
# retrieve the available transcripts
transcript_list = YouTubeTranscriptApi.list_transcripts('BQcp1ZNWgTs')
# iterate over all available transcripts
for transcript in transcript_list:
 print(transcript.fetch())
 print(transcript.translate('hi').fetch())

with open("captionfile.docx", "w") as f:
    for i in transcript.translate('hi').fetch():
        f.write("{}\n".format(i))
print(transcript.translate('hi').fetch())
open('captionfile.docx')


 
 