import os
from moviepy.editor import VideoFileClip
dir='memes/'

for i in os.listdir(dir):
    clip = VideoFileClip(dir+i)
    # print(clip.duration)
    b=300
    if clip.duration < 30:
        b=600
    elif clip.duration > 30 and clip.duration < 100:
        b=400
    elif clip.duration > 100 and clip.duration < 200:
        b=300
    elif clip.duration > 300:
        b=200
    # print(b)
    os.system(f'ffmpeg -i {dir+i} -b:v {b}k {dir+"1_"+i}')