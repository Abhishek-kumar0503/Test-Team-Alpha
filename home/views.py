
from re import search
from urllib import request
from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
import requests
import os
from moviepy.editor import *
from pytube import YouTube
from isodate import parse_duration

from django.conf import settings
vid = ""

def index(request):
    context = {
        "variable":"This is sent by Alpha"
    }
    
    if request.method == 'POST':
        search_query=request.POST.get['Search']
    # print("here")
    # search_query=request.POST['Search']
    # print(search_query)
        #results = MyModel.objects.filter(name__icontains=search_query)    
        #yt = YouTube(search) 
        #link = yt.watch_url   
    
    #print(link)
    return render(request,'index.html')
    
    
def about(request):
    return render(request,'about.html')
       # return HttpResponse("This is About page")
    
def services(request):
    return render(request,'services.html')
       # return HttpResponse("This is Services page")  
    
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
    return render(request,'contact.html')
       # return HttpResponse("This is Contact page")  
       
def search(request):
    global vid
    videos = []
    
    search_url = 'https://www.googleapis.com/youtube/v3/search'
    video_url = 'https://www.googleapis.com/youtube/v3/videos'
    
    search_params = {
        'part' : 'snippet',
        'q' : request.POST['Search'],           #request.POST['index/search']
        'key' : settings.YOUTUBE_DATA_API_KEY,
        'maxResults': 1,
        'type': 'video'
    }
    
    video_ids = []
    r = requests.get(search_url, params = search_params)
    
    results = r.json()['items']
    
    for result in results:
        video_ids.append(result['id']['videoId'])
    
    video_params = {
        'key' : settings.YOUTUBE_DATA_API_KEY,
        'part' : 'snippet,contentDetails',
        'id' : ','.join(video_ids),
        'maxResults': 1
    }
    
    r = requests.get(video_url, params = video_params)
    
    results= r.json()['items']
    
    
    for result in results:
        video_data = {
            'title' : result['snippet']['title'],
            'id' : result['id'],
            'embed' : f'https://www.youtube.com/embed/{ result["id"] }',
            'url' : f'https://www.youtube.com/watch?v={ result["id"] }',
            'sduration' : float(parse_duration(result['contentDetails']['duration']).total_seconds()),
            'duration' : int(parse_duration(result['contentDetails']['duration']).total_seconds() // 60),
            'thumbnail' : result['snippet']['thumbnails']['high']['url']
        }
    
        videos.append(video_data)
        vid= video_data['id']
    
    context = {
        'videos': videos
    }  
    return render(request,'migration/search.html', context)

def directing(request):
    return render(request, 'migration/directing.html')

def translate (request):  
    global vid
# importing the module

    import time
    from cgitb import text
    from tkinter import Variable
    from youtube_transcript_api import YouTubeTranscriptApi
    from re import S
    from gtts import gTTS
    import time
    import pytube
    
# retrieve the available transcripts
    # v='C9VLqW7q094'
    #v = vid
    transcript_list = YouTubeTranscriptApi.list_transcripts(vid)
    # iterate over all available transcripts
    m = []
    for transcript in transcript_list:
     #print(transcript.fetch())
     m.append(transcript.translate(request.GET['language']).fetch())

    ask = ''
    # to print only text from the fetched transcript (either original or translated)

    for i in m:
        #if i==m[0]:
        #    ask += "'''"
        #print("'''", end="")
        for x in i:
            start_time= time.strftime('%H:%M:%S', time.gmtime(x['start']))
            end_time =time.strftime('%H:%M:%S', time.gmtime(x['start'] + x['duration']))
            ask+=(start_time + " --> " + end_time + "\t\t" + x['text'] + "\n")
    
    text_from_transcript = ''
    for i in m:
            for x in i:
                text_from_transcript += "\t"+x['text']+"\n"    
    # convert the text to Hindi audio using the gTTS library
    language = request.GET['language']
    myobj = gTTS(text=text_from_transcript, lang=language, slow=False)
    myobj.save("output01.mp3") 
    
        #print(x['text'])
           # x['text']
       # if i==m[-1]:
          #  ask += "'''"
        #print("'''", end="\b")
    
# download the video from YouTube
    link = "https://www.youtube.com/watch?v="+vid 
    yt = pytube.YouTube(link)
    stream = yt.streams.get_highest_resolution()
    video_path = stream.download()
# create a video object using the moviepy library
    video_clip = VideoFileClip(video_path)

# create an audio object using the converted audio file
    audio_clip = AudioFileClip("output01.mp3")

# set the sample rate of the audio clip to match that of the video clip
    audio_clip = audio_clip.set_fps(video_clip.fps)

# get the start time of the video and audio
    video_start_time = video_clip.start
    audio_start_time = audio_clip.start

# calculate the start time difference between the video and audio
    start_time_diff = audio_start_time - video_start_time

# shift the audio clip to match the start time of the video clip
    audio_clip = audio_clip.subclip(start_time_diff)

# set the duration of the audio clip to match the duration of the video clip
    audio_clip = audio_clip.set_duration(video_clip.duration)

# merge the video and audio clips
    final_clip = video_clip.set_audio(audio_clip)

# write the final clip to a file
    final_clip.write_videofile("final_clip.mp4")
    print(ask)
    return render(request,'migration/translate.html', {'desc':ask})

