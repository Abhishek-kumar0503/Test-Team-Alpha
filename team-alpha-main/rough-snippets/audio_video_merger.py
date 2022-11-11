# Import everything needed to edit video clips
from moviepy.editor import *
  
# loading video gfg
clip = VideoFileClip("Bengaluru From Boom to Bust How Indias Best City Is Being Ruined  Nothing But the Truth.mp4")
  
# getting only first 5 seconds
clip = clip.subclip(0, 1620)
  
# loading audio file
audioclip = AudioFileClip("output001.mp3").subclip(0, 1620)
  
# adding audio to the video clip
videoclip = clip.set_audio(audioclip)
  
# showing video clip
videoclip.ipython_display()