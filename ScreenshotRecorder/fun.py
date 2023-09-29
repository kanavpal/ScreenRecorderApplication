import os
import datetime
import re

def newrecording(name):
    f = open("name.txt", "w")
    f.write(name)
    f.close()


def rename():
    my_source="recording.mp4"
    username=foldername()
    filename=fname()
    my_dest=f"static/screenrecordings/{username}/{filename}"
    os.rename(my_source, my_dest)



def foldername():
    f = open("name.txt", "r")
    name=f.read()
    f.close()
    return name

def fname():
    x = datetime.datetime.now()
    y=re.sub(r'[ :-]', '', str(x)[:-7])
    fname = f'VID{y}.mp4'
    return fname