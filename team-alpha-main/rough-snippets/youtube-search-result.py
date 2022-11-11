import requests

YOUTUBE_DATA_API_KEY = 'AIzaSyC2xbwS_4_i9gTQHKCjalSFCobYyRX5bzA'

search_url = 'https://www.googleapis.com/youtube/v3/search'

params = {
    'part' : 'snippet',
    'q' : 'learn python',
    'key' : YOUTUBE_DATA_API_KEY,
    'maxResults': 9,
}
r = requests.get(search_url, params = params)
results = r.json()['items']
print(results)

import json
with open('youtube-search-result.json', 'w') as json_file:
    json.dump(results, json_file)