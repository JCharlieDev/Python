import pyglet
import os
from moviepy.editor import *
import moviepy.editor as mp


#   mp4 to mp3
videoList = os.listdir("D:\\GitHub Repos\\Python\\Python Programs\\DAITOVTEST\\Resources\\Videos\\Error\\EN")

for video in range(0, len(videoList)):

    videoToMp3 = VideoFileClip(os.path.join("D:\\GitHub Repos\\Python\\Python Programs\\DAITOVTEST\\Resources\\Videos\\Error\\EN", videoList[video]))
    videoToMp3.audio.write_audiofile(os.path.join("D:\\GitHub Repos\\Python\\Python Programs\\DAITOVTEST\\Resources\\Audio\\Dialogos\\Error\\EN", "EN" + str(video) + ".mp3"))


# #   Gets the Directory
# videoList = os.listdir("D:\\GitHub Repos\\Python\\Python Programs\\DAITOVTEST\\Resources\\Videos\\Noche")
#
# # clip = mp.VideoFileClip("D:\\GitHub Repos\\DAITOV\\Resources\\Videos\\I01.mp4")
# # clip_resized = clip.resize(height=360)
# # clip_resized.write_videofile("D:\\GitHub Repos\\DAITOV\\Resources\\Videos\\I01_resized.mp4")
#
# #   Mass conversion
# for video in range(0, len(videoList)):
#     print(videoList[video])
#
#     clip = mp.VideoFileClip("D:\\GitHub Repos\\Python\\Python Programs\\DAITOVTEST\\Resources\\Videos\\Noche\\" + videoList[video])
#     clip_resized = clip.resize(height=360)
#     clip_resized.write_videofile("D:\\GitHub Repos\\Python\\Python Programs\\DAITOVTEST\\Resources\\Videos\\Noche\\N_Resized\\N" + str(video) + "_resized.mp4")

# vidPath = clip_resized
# window = pyglet.window.Window(resizable=True)
# player = pyglet.media.Player()
# source = pyglet.media.StreamingSource()
# MediaLoad = pyglet.media.load(vidPath)
#
# player.queue(MediaLoad)
# player.play()
#
#
# @window.event
# def on_draw():
#     if player.source and player.source.video_format:
#         player.get_texture().blit(50, 50)
#
#
# pyglet.app.run()

