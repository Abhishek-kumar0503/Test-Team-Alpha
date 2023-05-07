# importing the necessary modules
from cgitb import text
from re import S
from tkinter import Variable
from gtts import gTTS
from youtube_transcript_api import YouTubeTranscriptApi
import time
import os
import pytube
from moviepy.editor import *

# retrieve the available transcripts
v = "tlcaQgc4QW0"
transcript_list = YouTubeTranscriptApi.list_transcripts(v)

# iterate over all available transcripts and translate them to Hindi
m = []
for transcript in transcript_list:
    m.append(transcript.translate('hi').fetch())

# join all the text from the transcript
text_from_transcript = ''
for i in m:
    for x in i:
            start_time= time.strftime('%H:%M:%S', time.gmtime(x['start']))
            end_time =time.strftime('%H:%M:%S', time.gmtime(x['start'] + x['duration']))
            m+=text_from_transcript += f"{start_time} --> {end_time}\n{x['text']}\n"

# convert the text to Hindi audio using the gTTS library
language = 'hi'
myobj = gTTS(text=text_from_transcript, lang=language, slow=False)
myobj.save("output01.mp3") 

# download the video from YouTube
link = "https://www.youtube.com/watch?v="+v 
yt = pytube.YouTube(link)
stream = yt.streams.get_highest_resolution()
video_path = stream.download()

# create a video object using the moviepy library
video_clip = VideoFileClip(video_path)

# create an audio object using the converted audio file
audio_clip = AudioFileClip("output01.mp3")

# get the duration of the video
video_duration = video_clip.duration

# get the duration of the audio
audio_duration = audio_clip.duration

# calculate the difference between video duration and audio duration
duration_diff = video_duration - audio_duration

# add silence to the audio clip to make it the same duration as the video clip
if duration_diff > 0:
    silence_duration = duration_diff
    audio_clip = audio_clip.set_duration(audio_duration+silence_duration)

# set the start time of the audio clip to match the start time of the video clip
audio_clip = audio_clip.set_start(video_clip.start)

# merge the video and audio clips
final_clip = video_clip.set_audio(audio_clip)

# write the final clip to a file
final_clip.write_videofile("final_clip.mp4")

