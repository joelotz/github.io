Title: Converting Audible .aax Audiobook Files Into .mp3 on Ubuntu
Date: 2020-05-28
Tags: Ubuntu, FFmpeg
Author: Joe Lotz
Keywords: ubuntu 20.04, audible.com, .aax, convert aax to mp3
Excerpt: Audible lets you download your audiobooks but they are DRM'd. Crack the SHA hash with your authentication code and save the .aax files into other formats like .mp3 or even .ogg.
Version: OS, Ubuntu 20.04 LTS, bash, 5.0.16(1)-release, python, 2.7.4, FFmpeg,4.2.2-1,

I have a bunch of audio-books on Audible.com that I’ve collected in the past year or two. I’ve been meaning to cancel my monthly subscription but I don’t get around to it, which leads to more monthly credits, and then I don’t want to cancel and lose those unused credits…or lose the books I haven’t listed to. It’s a brilliant ploy on Audible’s part to keep their customers. So there’s the problem, I want to part ways and cancel my monthly subscription but I don’t want to lose the books that I’ve already paid for, both listened to and not. 

What I learned from googling around it that you convert the audible .aax audiobook files into other formats with [FFmpeg](https://ffmpeg.org/) ([one of my favorites!](/tag/ffmpeg.html)), but you have to have your unique “activation bytes” to decode the DRM. *That* is the tricky part. I found a couple of solutions that work great for other people but didn’t work for me with my unique hardware, configuration, situation, etc. I believe people when they say it works, it just didn’t work for me. I spent all day coming up with a solution. I tried [Audiblex](https://github.com/naueramant/Audiblex), [AAXtoMP3-easy](https://github.com/paladini/aax2mp3-easy), audible-activator, and others, and finally the one that worked for me was [inAudible-NG](https://github.com/inAudible-NG/tables). 

I won’t go into the long and torrid details of the failures, but rather describe the path for success. 

First, log into www.audible.com and download one of your audio-books. Login, go to Library, click Download, save the file. Next, you will need to determine the [SHA sum](https://en.wikipedia.org/wiki/Secure_Hash_Algorithms) of one of your .aax files that you downloaded. Of course, you will need to have FFMpeg installed.

```bash
ffprobe <inputfile.aax>
# Example
ffprobe TheGrapesofWrath.aax
```

![audibleConvert-01](/images/audibleConvert-01.png)

After all the stupid library declarations you’ll see the line `[aax] file checksum` and you want to copy that key that I circled in the image above. This is your checksum that is the input to RainbowCrack. [RainbowCrack](http://project-rainbowcrack.com/) is a hash cracking program that uses [rainbow tables](https://en.wikipedia.org/wiki/Rainbow_table) to decrypt… [passwords](https://en.wikipedia.org/wiki/Password_cracking) and stuff. We will be using it decrypt this hash and tell us our Audible code.

Follow the instructions on [inAudible-NG github](https://github.com/inAudible-NG/tables) and download the zip or clone into a directory. Then go into the tables directory where the script is located and run the crack on the checksum you found using ffprobe `./rcrack . h <your checksum here>`. After 2-3secs out pops the magic number.

```bash
# For example 
cd ~/Downloads/
git clone https://github.com/inAudible-NG/tables.git
cd tables/
./rcrack . h 123456789abcdef123456789abcdef
```

![audibleConvert-02](/images/audibleConvert-02.png)

It’s all gravy from here now that you have your unique code, you can remove the DRM from your audiobook files and decode into other other formats like mp3, mp4, m4a, m4b, flac, ogg, opus, etc, etc, etc. Note that the files you downloaded are hashed with your specific account, so it’s not like you can use my numbers, but I did obfuscate them in the images just in case.

You can use FFmpeg directly or some library front-end. I like the idea of a front-end because they most likely offer a variety of options, ease of use, and efficiency mastery that I would probably not know of. I found [AAXtoMP3](https://github.com/KrumpetPirate/AAXtoMP3) very robust, easy to use, and useful - ymmv. It is simply a bash script with useful FFmpeg calls. The author has a fun “Do What the Fuck You Want To” [Public License](https://github.com/KrumpetPirate/AAXtoMP3/blob/master/LICENSE). I had a bunch of .aax files to decode and I also wanted multiple outputs for archiving (.flac, .mp3, .m4a chapters) so that I wouldn’t have to come back and do it again in the future. The solution was a simply bash script that looped through each .aax file and made multiple calls to AAXtoMP3. Here’s my batch-script:

```bash
#!/bin/bash

for file in *.aax; do
	bash AAXtoMP3 -e:mp3 $file & 
	bash AAXtoMP3 --flac $file & 
	bash AAXtoMP3 -e:m4a --chaptered $file
done
```

### Extras

I have an 8-core CPU and there is no use in making it wait for each thread to process. We can call multiple decoding processes at once to each run on a single core…get it? That is what the “&” in the script above is doing. It says ‘start this process thread in the background and move on’, which the script then starts another decoding process, and another, and then loops around to grab a different file then starts another decoding process, until all the CPU cores are full. 