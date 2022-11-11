# importing modules
from youtube_transcript_api import YouTubeTranscriptApi
# using the srt variable with the list of dictonaries
# obtained by the .get_transcript() function
srt = YouTubeTranscriptApi.get_transcript("PZ7lDrwYdZc") 
# creating or overwriting a file "subtitles.txt" with
# the info inside the context manager
with open("subtitles1.txt", "w") as f:
    for i in srt:
        f.write("{}\n".format(i))
print(srt)
contextlib.redirect_stdout(srt)