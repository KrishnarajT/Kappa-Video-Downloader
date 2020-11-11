"""This file contains the class implementation of the video downloader with the progress bar, in case i get lost"""

import urllib
import lxml
from lxml import etree
from bs4 import BeautifulSoup as bs  # importing BeautifulSoup
import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk
from pytube import YouTube
from pytube import Playlist
import os
import ffmpeg
from pytube.cli import on_progress
import re
import pytube
from threading import *

# Function responsible for the updation
# of the progress bar value
import time


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.button = ttk.Button(text="start", command=self.begins)
        self.button.pack()
        self.progress = ttk.Progressbar(self, orient="horizontal",
                                        length=200, mode="determinate")
        self.progress.pack()

        self.bytes = 0
        self.maxbytes = 0

    def on_progress_dothis(self, stream, chunk: bytes, bytes_remaining: int) -> None:  # pylint: disable=W0613
        self.bytes = self.maxbytes - bytes_remaining
        percent = (100 * (self.maxbytes-bytes_remaining)) / self.maxbytes
        self.progress["value"] = self.bytes
        self.update_idletasks()

    # Grabs the file path for Download
    @staticmethod
    def file_path():
        home = os.path.expanduser('~')
        download_path = os.path.join(home, 'Downloads')
        return download_path

    def begins(self):
        t1 = Thread(target=self.download)
        t2 = Thread(target=self.read_bytes)
        t1.start()
        t2.start()

    def download(self):
        self.progress["value"] = 0
        print("Your video will be saved to: {}".format(self.file_path()))
        yt_url = 'https://www.youtube.com/watch?v=IpN_wAlYZSs'
        print("Accessing YouTube URL...")
        video = YouTube(yt_url, on_progress_callback=self.on_progress_dothis)
        video_type = video.streams.filter(progressive=True, file_extension="mp4").first()
        print("Fetching")
        self.maxbytes = video_type.filesize
        self.progress["maximum"] = self.maxbytes
        video_type.download(self.file_path())

    def read_bytes(self):
        self.progress["value"] = self.bytes
        if self.bytes < self.maxbytes:
            self.after(100, self.read_bytes)

#app = SampleApp()
# app.mainloop()


def download():
    url = 'https://www.youtube.com/watch?v=LXb3EKWsInQ&t=48s'
    yt = YouTube(url)
    # to see all the streams
    for i in yt.streams:
        print(i)
    # to see just the audio
    #print(yt.streams.filter(only_audio = True))

    # there are 2 types of videos that you can download, because of how youtube handles streaming and downloading videos and
    # playing them. There is progressive, and then there is DASH, which stands for dynamic adaptive streaming by HTTP.
    # this means that you can download the progressing things, but that will only be available for 360p and 720p
    # now because of us using 4g, and most people using 4g, you cant really download the the entire video packets efficiently
    # so they split that into the audio, and video. Due to this, we have to also get them separately, and then combine them using
    # things like FFmpeg or other stuff like that.

    # the progressive streams
    #print(yt.streams.filter(progressive = True))

    # the dynamic streams
    #print( yt.streams.filter( progressive = False ) )

    # every stream has a tag and stuff, so you can access it using that as well
    print(yt.streams.get_by_itag(23))

    # we can also downlaod the captions
    # print(yt.captions)

    # to download the captions
    #caption = yt.captions[ 'en' ]
    # print(caption.generate_srt_captions())

    # We will now try to download the streams separately, and then use ffmpeg to combine and output the final video
    # this should wrap up downloading any type of video from youtube
    print('\n\n\n\n')
    # this gets the 1080p version of the video
    # yt.streams.get_by_itag(137).download()

    # this gets the audio
    # yt.streams.get_by_itag(250).download()

    videos = 'sth.mp4'
    audios = 'sth.webm'
    # this should convert and then output the video
    #ffmpeg.concat( videos, audios, v = 1, a = 1 ).output( './processed_folder/finished_video.mp4' ).run()

    input_video = ffmpeg.input('sth.mp4')

    input_audio = ffmpeg.input('sth.webm')

    ffmpeg.concat(input_video, input_audio, v=1, a=1).output('Jupyter/sth.mp4').run()


def combine_audio(vidname, audname, outname, fps=25):
    import moviepy.editor as mpe
    my_clip = mpe.VideoFileClip(vidname)
    audio_background = mpe.AudioFileClip(audname)
    final_clip = my_clip.set_audio(audio_background)
    final_clip.write_videofile(outname, fps=fps)


def checkingonplaylists():
    playlists = Playlist('https://www.youtube.com/playlist?list=PL6gx4Cwl9DGCkg2uj3PxUWhMDuTw3VKjM')
    playlists._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
    for i in playlists.video_urls:
        print(scrape_info('https://www.youtube.com/watch?v=IpN_wAlYZSs'))


#from requests_html import HTMLSession
#session = HTMLSession()


def get_video_info(url):
    # download HTML code
    response = session.get(url)
    # execute Javascript
    response.html.render(sleep=1)
    # create beautiful soup object to parse HTML
    soup = bs(response.html.html, "html.parser")
    # open("index.html", "w").write(response.html.html)
    # initialize the result
    result = {}
    return result


# checkingonplaylists()
youtube = etree.HTML(urllib.urlopen("http://www.youtube.com/watch?v=KQEOBZLx-Z8").read())
video_title = youtube.xpath("//span[@id='eow-title']/@title")
print(video_title)
