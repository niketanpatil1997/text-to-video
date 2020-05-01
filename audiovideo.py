from moviepy.editor import *

import os 

audio = AudioFileClip("hello.mp3")
audioduration = audio.duration
imagelist=[]
image_clip1 =  ImageClip("0.jpg", duration=audioduration/2)

image_clip2 =  ImageClip("1.jpg", duration=audioduration/2)

imagelist.append(image_clip1)
imagelist.append(image_clip2)

result = concatenate_videoclips(imagelist, method="compose")

#result.write_videofile('some.mp4',fps=24)

result.write_videofile("some.mp4", audio="hello.mp3",fps=24)





