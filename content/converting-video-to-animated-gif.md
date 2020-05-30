Title: Converting Video to Animate Gif with FFmpeg
Date: 2020-05-07
Category: 
Tags: Ubuntu, FFmpeg
Author: Joe Lotz
Keywords: ubuntu 20.04, ffmpeg
Version: OS, Ubuntu 20.04 LTS, bash, 5.0.16(1)-release, python, 2.7.4, FFmpeg,4.2.2-1,

Source is from an [excellent answer](https://superuser.com/questions/556029/how-do-i-convert-a-video-to-gif-using-ffmpeg-with-reasonable-quality) on SuperUser StackExchange.
```bash
ffmpeg input.mp4 -vf "fps=15,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop 0 output.gif
```
You can define the frames per second via the ”fps” argument. The standard for an animated gif is [between 15 and 24](https://www.bluefrogdm.com/blog/best-practices-for-creating-animated-gifs), but the more frames the larger the output file. 

The split commands splits the video into two streams for generate a color palette and downsampling the incoming video. 

The loop argument defines how many times you want the gif to loop.
- 1 = no looping
- 1 = loop once
- n = loop n times
- 0 = loop infinite = “forever”