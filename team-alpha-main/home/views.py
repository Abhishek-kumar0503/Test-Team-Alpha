
from re import search
from urllib import request
from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
import requests

from isodate import parse_duration

from django.conf import settings

# Create your views here.
def index(request):
    context = {
        "variable":"This is sent by Alpha"
    }
    if request.method == 'POST':
         request.POST.get['Search']
         
            
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
    videos = []
    
    search_url = 'https://www.googleapis.com/youtube/v3/search'
    video_url = 'https://www.googleapis.com/youtube/v3/videos'
    
    search_params = {
        'part' : 'snippet',
        'q' : request.POST['Search'],           #request.POST['index/search']
        'key' : settings.YOUTUBE_DATA_API_KEY,
        'maxResults': 9,
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
        'maxResults': 9
    }
    
    r = requests.get(video_url, params = video_params)
    
    results= r.json()['items']
    
    
    for result in results:
        video_data = {
            'title' : result['snippet']['title'],
            'id' : result['id'],
            'url' : f'https://www.youtube.com/watch?v={ result["id"] }',
            'duration' : int(parse_duration(result['contentDetails']['duration']).total_seconds() // 60),
            'thumbnail' : result['snippet']['thumbnails']['high']['url']
        }
    
        videos.append(video_data)
    
    context = {
        'videos': videos
    }  
    return render(request,'migration/search.html', context)

def directing(request):
    return render(request, 'migration/directing.html')

def translate (request):  
    return render(request,'migration/translate.html')

