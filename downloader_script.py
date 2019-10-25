#Koushik Narayan 

from __future__ import unicode_literals
import os
import youtube_dl
from sys import argv

#download data and config from youtube_dl module

download_options={
    'format': 'bestaudio/best',     #to get the audio in the best format possible
    'outtmpl': '%(title)s.%(ext)s', #saving audio file 
    'nocheckcertificate': True,          #not to check socket certificate
    'postprocessors':[{
        'key':'FFmpegExtractAudio', #module to extract audio    
        'preferredcodec': 'mp3',  # preferred codec format
        'preferredquality': '192',  # preferred quality format
    }],  
}

#song directory to save the files into 

if not os.path.exists('Songs'):
        os.mkdir('Songs')

else:
    os.chdir('Songs')        


#Download songs

with youtube_dl.YoutubeDL(download_options) as dl:    #shortcutting
    with open('../' + argv[1],'r')as f:   #assuming ../ is songs and script is present there
       
        for song_url in f:
            dl.download([song_url])
