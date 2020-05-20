Title: Installing and Using youtube-dl on Ubuntu 20.04
Date: 2020-05-20
Category: 
Tags: Ubuntu, FFmpeg,
Author: Joe Lotz
Keywords: ubuntu 20.04, ffmpeg, youtube.dl	

I got bluetooth headphones for running since my old wired headphones were falling apart. I don’t need anything super-high quality since these are for running and I’ll be huffing and puffing - so I got what was available in India - [JBL Endurance Dive](https://in.jbl.com/JBL+Endurance+DIVE.html). I currently jog with my phone playing Amazon Music, so I was going to bluetooth to my phone until I get a small bluetooth player like the [SanDisk Clip Sport Plus](https://www.amazon.com/SanDisk-SDMX28-016G-G46K-Sport-Player-Black/dp/B01LW2F237/r). BUT, the JBL headphones have a built-in mp3 player with 1GB storage, so no external player needed! Of course, this is not the highest quality, but like I said I’m just running.

The next challenge is getting music for the player. I’m streaming music and don’t really want to get all into torrenting. After a short time searching I see cross-platform utility named [youtube-dl](https://github.com/ytdl-org/youtube-dl/blob/master/README.md). 

*Source: [https://linoxide.com/linux-how-to/install-use-youtube-dl-ubuntu/](https://linoxide.com/linux-how-to/install-use-youtube-dl-ubuntu/)*

```bash
sudo apt install youtube-dl
```

Now that it is installed, I recommend installing FFmpeg also. This is pretty simple, as described in this [tutorial instructions](https://linuxconfig.org/ubuntu-20-04-ffmpeg-installation). This is just a very useful utility to have and I use a bunch for transcoding video formats.

```bash
sudo apt install ffmpeg
```

Once you have chosen a youtube video, you can list all available audio/video formats and bitrates. Note, replace <id> with the actual ID of the video you want. Better yet, just copy/past the entire URL.

```bash
youtube-dl -F https://www.youtube.com/watch?v=<id>
```

If I run this command on the video “yYzrSGRzttk”, I see a whole list of audio and video files that are available. The first four; ID# 249, 250, 251, 140 are audio. The first three are in [webm](https://en.wikipedia.org/wiki/WebM) format and the last is [m4a](https://en.wikipedia.org/wiki/MPEG-4_Part_14#.MP4_versus_.M4A), both are optimized for delivering on the web. 

![youtube-dl](/images/youtube-dl.png)

You can select the specific stream you want and download it.

```bash
youtube-dl -f 278 https://www.youtube.com/watch?v=yYzrSGRzttk
```

The better method is to let youtube-dl choose the best audio stream and download it. 

*Source: [https://stackoverflow.com/questions/49804874/download-the-best-quality-audio-file-with-youtube-dl](https://stackoverflow.com/questions/49804874/download-the-best-quality-audio-file-with-youtube-dl)*

```bash
youtube-dl -f bestaudio https://www.youtube.com/watch?v=<id>
```

You can specify the name of the downloaded file. 

```bash
youtube-dl -f bestaudio https://www.youtube.com/watch?v=<id> --output "outputName.%(ext)s"
```

With FFmpeg installed, you can also convert to mp3. I know converting formats probably degrade the audio quality, but my cheap headphone mp3 player doesn’t play the webm file format. 

```bash
youtube-dl -x --audio-format mp3 https://www.youtube.com/watch?v=<id>
```

And then finally, you can download, convert to mp3, and rename the file. 

```bash
youtube-dl -x --audio-format mp3 https://www.youtube.com/watch?v=<id> --output "outputName.%(ext)s"]
```

### Audacity to Clean Up

```bash
sudo apt install audacity
```

*Source: [https://askubuntu.com/questions/246242/how-to-normalize-sound-in-mp3-files](https://askubuntu.com/questions/246242/how-to-normalize-sound-in-mp3-files)*

The audio files downloaded from the web probably have different loudness levels which can be undesirable. You can run a normalize and clean up batch process to all the downloaded folder. 

Select “Tools > Macros…”

![youtube-dl](/images/audacity_macros.png)

Make sure the macro “MP3 Conversion” is selected, then click “Files…”. This will open up a standard file browser where you can shift/select all the mp3 files you want to normalize. 

![youtube-dl](/images/audacity_macros2.png)

Then the magic happens! The modified files will be in a new folder named “macro-output”.