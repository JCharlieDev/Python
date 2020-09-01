# import pyglet
# import moviepy.editor as mp
#
# clip = mp.VideoFileClip("D:\\GitHub Repos\\DAITOV\\Resources\\Videos\\I01.mp4")
# clip_resized = clip.resize(height=360)
# clip_resized.write_videofile("D:\\GitHub Repos\\DAITOV\\Resources\\Videos\\I01_resized.mp4")
#
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
#

name = "Jose"

print(name[:2])