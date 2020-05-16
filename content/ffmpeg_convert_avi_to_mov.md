Title: Converting mp4 to mov with FFmpeg in Ubuntu
Date: 2020-04-25
Tags: Ubuntu, FFmpeg
Author: Joe
Summary:
Keywords: ubuntu 20.04, ffmpeg, gopro, davinci resolve 16, H.264, mp4, mov

*Update:* [Please see the post](running-shell-scripts-on-files-from-nautilus.html) on how I turned this into a script that can be executed on a file by right-clicking. 

----

GoPro outputs video in H.264 mp4 containers and the Hero6 and Hero7 now can output in the more efficient HVEC H.265 mp4 container. This is great because:

1. nearly everything can read and play H.264 mp4 files
2. since the H.265 mp4 is more space efficient you can save even more video to your memory card.

Yeah! But wait…. Not everything can read/play the new H.265 mp4.

FYI, here are some great posts by havecamerawilltravel that you should read:

- [Hero7 Black Modes](https://havecamerawilltravel.com/gopro/gopro-hero7-black-video-modes/)
- [How to Convert H.265 to H.264 in Handbrake](https://havecamerawilltravel.com/gopro/convert-hevc-h265-video-codec/)

My goal is to edit and color correct my home videos in Davinci Resolve 16 (DR16) but it turns out it doesn’t import these GoPro video files directly, at least not in the Linux free version. 

In the [support notes of DR16](https://documents.blackmagicdesign.com/SupportNotes/DaVinci_Resolve_16_Supported_Codec_List.pdf) it states that :

- macOS will read mp4 in both DR16 (free version) and DR16 Studio (paid version)
- Windows will read mp4 in DR16 Studio only
- **Linux** will read mp4 in DR16 Studio only

![DR16 Input Codecs](/images/DR16_InputCodecs.png)

[Handbrake](https://handbrake.fr/) is a GUI front-end to ffpmeg and is awesome, I’m sure it could do it but I wanted something that I could run from a shell script and I wasn’t exactly sure what it was doing under the hood. My goal was to preserve the highest resolution and quality during the conversion or “transcode” to work with in DR16. 

### Installing FFmpeg on Ubuntu 20.04

This is pretty simple, as described in this [tutorial instructions](https://linuxconfig.org/ubuntu-20-04-ffmpeg-installation).

```bash
sudo apt install ffmpeg
```

### Converting my Video from mp4 to mov

In my research and experimentation I found success in two codecs; Apple [ProRes](https://en.wikipedia.org/wiki/Apple_ProRes) and [Avid DNxHD](Avid DNxHD). You can view all the installed and available codecs on your machine with `ffmpeg -codecs`. If you search through the long list you will see a bunch of H.264 decoders. I don’t know which ones are better or if they are, but I’ve seen these two used and recommended on the interwebs. 

As I said, I tried both codecs and didn’t find any difference between the two. They both decoded high-res 4k video and converted [AAC](https://en.wikipedia.org/wiki/Advanced_Audio_Coding) audio into [PCM](https://en.wikipedia.org/wiki/Pulse-code_modulation) audio. I’ll tell you later why that’s important. The advantage of using ProRes is that the command line is a bit easier:

```bash
ffmpeg -i input.mp4 -c:v prores -profile:v 3 -c:a pcm_s16le output.mov
```

The advantage of using DNxHD is that you can specify all the nerdy details if you want to, but that’s a double edge sword because you can’t leave them out and still work. You must specify all the nerdy details. 

Here is the final command, assuming 4k resolution at 23.967 (aka 24) fps.

```bash
ffmpeg -i input.mp4 \
	-c:v dnxhd \
	-profile:v dnxhr_hqx \
	-vf "scale=3840:2160,fps=24000/1001,format=yuv422p10le" \
	-b:v 110M \
	-c:a pcm_s16le \
	output.mov
```

#### Audio Transcoding

Referring back to the [Black Magic Support Codecs](https://documents.blackmagicdesign.com/SupportNotes/DaVinci_Resolve_16_Supported_Codec_List.pdf), we see that mp3 and AAC are <u>not</u> supported in either free nor Studio Linux version. That sucks…So this is why we have to convert the audio when we convert the video.

![DR16_InputAudio](/media/joe/Working/Blog/content/images/DR16_InputAudio.png)

#### FFmpeg Options/Arguments

- `-i` defines the input file

- `-c:v` (or the alias `-vcodec`) defines the codec to use for the video

  `-profile:v` defines the profile to use for the video.

  - Accepted values are: `dnxhd`, `dnxhr_444`, `dnxhr_hqx`, `dnxhr_hq`, `dnxhr_sq`, `dnxhr_lb`.

  - I was able to convert 1920x1080 videos but kept getting an error when attempting 4k 3840x2160 videos. I was stuck at this point for a while until I found a post on [askubuntu](https://askubuntu.com/questions/907398/how-to-convert-a-video-with-ffmpeg-into-the-dnxhd-dnxhr-format) explaining that a different profile was needed.

  - `dnxhd`: The lists of available/possible resolutions can be [looked up here](https://en.wikipedia.org/wiki/List_of_Avid_DNxHD_resolutions), but they do not go bigger than 1080p.

  - ##### DNxHR Profiles

    - DNxHR LB: `dnxhr_lb` - Low Bandwidth. 8-bit 4:2:2 (`yuv422p`). Offline Quality.
    - DNxHR SQ: `dnxhr_sq` - Standard Quality. 8-bit 4:2:2 (`yuv422p`). Suitable for delivery format.
    - DNxHR HQ: `dnxhr_hq` - High Quality. 8-bit 4:2:2 (`yuv422p`).
    - DNxHR HQX: `dnxhr_hqx` - High Quality. 10-bit 4:2:2 (`yuv422p10le`). UHD/4K Broadcast-quality delivery.
    - DNxHR 444: `dnxhr_444` - Finishing Quality. 10-bit 4:4:4 (`yuv444p10le`). Cinema-quality delivery.

    The above list was adapted from [DNxHR codec](https://en.wikipedia.org/wiki/DNxHR_codec). Note that the pix_format must match the profile! 

- `-vf` is as alias for `-filter:v` and creates the filtergraph that is used to filter the stream. You can specify each value but this is easier, for example `-pix_fmt=yuv422p10le`. 

  - `scale=`width x height 
  - `fps=`
    - 23.967 = 24000/1001 (or use the alias `ntsc-film`)
    - 29.97 = 30000/1001 (or use the alias `ntsc`)
    - 59.94 = 60000/1001
    - 119.88 = 120000/1001
  - `pix_fmts=`
    - For `dnxhr_lb` , `dnxhr_sq`, or `dnr_hq` = yuv422p
    - For `dnxhr_hqx` or `dnxhr_444`=  yuv422p10le

- `-c:a` defines the codec to use for the audio
