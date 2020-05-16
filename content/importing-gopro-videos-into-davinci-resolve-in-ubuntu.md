Title: Importing GoPro Vids into Davinci Resolve 16 on Ubuntu
Date: 2020-05-16
Tags: Ubuntu, FFmpeg, GoPro, Davinci Resolve 16
Author: Joe Lotz
Summary:
Keywords: ubuntu 20.04, ffmpeg, gopro, davinci resolve 16, mp4, mov, gopro

In a [previous post](https://joelotz.github.io/converting-mp4-videos-to-mov-with-ffmpeg.html) I showed a work-around for importing H.264 mp4 files into the free Linux version of Davinci Resolve 16 (DR16). For many reasons, I made the decision to purchase the full Studio version. This lets me directly import mp4 videos <u>but</u>, the audio still doesn’t work. Linux DR16 doesn’t import AAC audio. I read on the BlackMagic forums that it is a licensing thing. 

Since we are on Ubuntu and are comfortable with the command line and scripts…right??… we can just use ffmpeg to pop us out a PCM encoded .wav file that can be imported into the DR16 timeline and linked to the clip.

```bash
ffmpeg -i input.mp4 -acodec pcm_s16le -ac 1 -ar 16000 input_audio.wav
```

You could also turn this into a Nautilus shell script and run it by right-clicking on an .mp4 file, the [instructions are here](https://joelotz.github.io/running-shell-scripts-on-files-from-nautilus.html).

