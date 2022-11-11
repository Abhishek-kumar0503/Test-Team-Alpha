import pytube
link = "https://www.youtube.com/watch?v=IqYfmckxeyE&ab_channel=AmitThinks" 
yt = pytube.YouTube(link)
stream = yt.streams.get_highest_resolution()
stream.download()
