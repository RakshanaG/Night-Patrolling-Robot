import os

os.system('raspivid -t 20000 -w 640 -h 480 -fps 25 -b 20000 -p 0,0,640,480 -o /home/pi/Documents/camWebServer/Videos/video.h264')
os.system('MP4Box -add /home/pi/Documents/camWebServer/Videos/video.h264 /home/pi/Documents/camWebServer/Videos/video.mp4')
os.system('rm /home/pi/Documents/camWebServer/Videos/video.h264')

