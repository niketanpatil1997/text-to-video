
from gtts import gTTS 
from moviepy.editor import *
from textblob import TextBlob
from itertools import chain 

text = "Shivaji was born in the hill-fort of Shivneri, near the city of Junnar in what is now Pune district. Scholars disagree on his date of birth. The Government of Maharashtra lists 19 February as a holiday commemorating Shivaji's birth.Shivaji was named after a local deity, the goddess Shivai. Shivaji's father Shahaji Bhonsle was a Maratha general who served the Deccan Sultanates.His mother was Jijabai, the daughter of Lakhuji Jadhavrao of Sindhkhed, a Mughal-aligned sardar claiming descent from a Yadav royal family of Devagiri."
months = ['January','February','March','April','May','June','July','August','September','October','November','December']
textsplit = text.split(".")[:-1]
listnouns = []

for txt in textsplit:
    blob = TextBlob(txt)
    lst=[]
    for noun in blob.noun_phrases:
        if not noun.startswith("'s"):
            if noun.capitalize() not in months:
                noun=noun.replace(" ", "_")
                lst.append(noun)
                twolst = lst[:2]
    listnouns.append(twolst)

flatten_list = list(chain.from_iterable(listnouns)) 

print(listnouns)


#-------- flatten list in order to make .txt file for image downloading----
#print(flatten_list)     
'''
--------------working file writing code-----------------
f= open("sample.txt","w+")


for i in flatten_list:
    f.write(i + '\n')

f.close()    

'''

audiopath='/home/prime/Desktop/bing/audio/'
i = 0
audioDuration=[]
for txt in textsplit:
    myobj = gTTS(text=txt, lang='en')
    myobj.save(audiopath + str(i)+'.mp3')
    audio = AudioFileClip(audiopath +str(i)+'.mp3')
    
    audioDuration.append(audio.duration)
    i+=1

audioDuration = [x + 0.1 for x in audioDuration] 

text_clip_list=[]
for i in range(0,len(textsplit)):
        sent_txt_clip = TextClip(textsplit[i],font='Courier-Bold',fontsize=50,color='yellow',bg_color='black',stroke_width=30).set_pos('bottom').set_duration(audioDuration[i])
        text_clip_list.append(sent_txt_clip)
path = '/home/prime/Desktop/bing/bing/'
j=0
video_list=[]
for  i  in  listnouns:
    imagelist = []
    if len(i) == 1:
        image_clip1 =  ImageClip(path + i[0]+'/0.jpg', duration=audioDuration[j])
        imagelist.append(image_clip1)
    if len(i) == 2:
        image_clip1 = ImageClip(path + i[0]+'/0.jpg', duration=audioDuration[j]/2)
        image_clip2 = ImageClip(path + i[1]+'/0.jpg', duration=audioDuration[j]/2)            
        imagelist.append(image_clip1)
        imagelist.append(image_clip2)
    
    result = concatenate_videoclips(imagelist, method="compose")
    result.write_videofile(str(i)+'.mp4',fps=24)   
    j+=1
    video_list.append(result)
txt_clip=concatenate_videoclips(text_clip_list).set_position('bottom')
main = concatenate_videoclips(video_list,method="compose")    

result=CompositeVideoClip([main,txt_clip])
result.write_videofile('main.mp4',fps=24) 

result.set_audio('hello.mp3')
