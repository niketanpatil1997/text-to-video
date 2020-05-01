from gtts import gTTS 
from moviepy.editor import *



import os 
'''
mytext = 'Shivaji Bhosale I was an Indian warrior-king and a member of the Bhonsle Maratha clan'
  

language = 'en'
  

myobj = gTTS(text=mytext, lang=language, slow=False) 
  
myobj.save("welcome.mp3") 
audio = AudioFileClip('welcome.mp3')'''
#print(audio.duration)
list=[["shivaji","adilshah"]]
default = 'C:\Users\lenovo\Documents\Django projects\bing\\'
image_clip1 =  ImageClip("shivaji.jpg", duration=2)

image = '\adil.jpg'

image_clip2 =  ImageClip(default + list[0][1] + image, duration=2)

imagelist=[]
imagelist.append(image_clip2)
imagelist.append(image_clip1)

result = concatenate_videoclips(imagelist, method="compose")

#result = CompositeVideoClip(imagelist)
result.write_videofile('some.mp4',fps=24)






