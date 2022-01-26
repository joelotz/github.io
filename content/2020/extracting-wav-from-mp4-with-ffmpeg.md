---
Title: Extracting wav Audio File from mp4 Video with FFmpeg in Ubuntu
Date: 2020-04-24
Tags: Ubuntu, FFmpeg, GoPro, Davinci Resolve 16
Author: Joe
Excerpt: This article shows how to save audio from an .mp4 video file into a high-quality audio file. 
Keywords: ubuntu 20.04, ffmpeg, gopro, davinci resolve 16, mp4, mov, gopro
Version: OS, Ubuntu 20.04 LTS, FFmpeg,4.2.2-1, DavinciResolve, 16.1.2-1
---

In a [previous post](https://joelotz.github.io/converting-mp4-videos-to-mov-with-ffmpeg.html) I showed a work-around for importing H.264 mp4 files into the free Linux version of Davinci Resolve 16 (DR16). For many reasons, I made the decision to purchase the full Studio version. This lets me directly import mp4 videos <u>but</u>, the audio still doesn’t work. Linux DR16 doesn’t import AAC audio. I read on the BlackMagic forums that it is a licensing thing. 

![DR16 Input Codecs](/images/2020/DR16_InputAudio.png)

Since we are on Ubuntu and are comfortable with the command line and scripts…right??… we can just use ffmpeg to pop us out a PCM encoded .wav file that can be imported into the DR16 timeline and linked to the clip.

```bash
ffmpeg -i input.mp4 -acodec pcm_s16le -ac 1 -ar 16000 input_audio.wav
```

You could also turn this into a Nautilus shell script and run it by right-clicking on an .mp4 file, the [instructions are here](https://joelotz.github.io/running-shell-scripts-on-files-from-nautilus.html).

