---
Title: Changing mp4 CreationDates with Exiftool
Date: 2020-11-14
Tags: Exiftool
Author: Joe
Keywords: ubuntu 20.4, mp4, ffmpeg, exiftool, changing dates, exif, GoPro
Version: OS, Ubuntu 20.04 LTS, Exiftool, 11.88
---

I assume there is a tiny cell battery inside my GoPro that keeps the settings and such for a short period while the main battery is removed or charging. I had removed the battery and let the GoPro set for a while and the date setting reset. I hadn’t noticed when I inserted a battery and started filming all the videos had a creation date of 2016-04-23 which was exactly 1600 days before the real date. I don’t know why… I’m sure there is a [real-time clock](https://en.wikipedia.org/wiki/Real-time_clock) inside and the reset date has to do with some default value. 

So the problem is - how do I change a bunch of exif date data-fields in my mp4s? I want to change the date but also I want to keep the time. 

### Enter Exiftool!

I [really like](/tag/exiftool.html) [exiftool](https://exiftool.org/), it is an amazing utility. Let’s start by looking at all the data fields that contain dates. 

```bash
exiftool -time:all -a -G0:1 -s filename.mp4
```
As you would expect there are multiple date fields set by GoPro in the mp4 container.

![Image1](/images/2020/ChangingMp4Date_01.png)

 There are multiple solutions… we could set each field individually and explicitly. 

```bash
exiftool -CreateDate="2020:08:20 00:46:59" -ModifyDate="2020:08:20 00:46:59" -Track*Date="2020:08:20 00:46:59" -Media*Date="2020:08:20 00:46:59" test.MP4
```

Not surprisingly, Phil Harvey (the awesome author of exiftool) has created a magic tag names “time:all”. This makes our command a bit easier.

```bash
exiftool -time:all="2020:08:20 00:46:59" test.MP4
```

![Image2](/images/2020/ChangingMp4Date_03.png)

This would work for a file or two, but I want to change a couple dozen files and the above solution would require me to enter the date and time for each file. The solution is time-shifting. As stated earlier in this post, the files are 1600 days behind the current date. We can time-shift the dates *forward* by 1600 days. 

```bash
exiftools -time:all+="00:00:1600 0" test.MP4
```

The format for the date/time is *YY:MM:DD HH:MM:SS*. Note that “0” in the time field is shorthand for 00:00:00 and if you enter a time value then it won’t work. 

The final command to shift all MP4 files in a directory forward by 1600 days is:

```bash
exiftools -time:all+="00:00:1600 0" *.MP4
```

### Bonus Command

My Android camera names pictures as *YYYYMMDD_xxxxxx.jpg* and I’ve grown to like this convention. It allows me to sort, filter, find pictures easier by looking at the date in the file name. I’d like my GoPro videos to follow the same convention so that when I combine photos and videos in a directory I have a built-in timeline. 

```bash
exiftool -r '-FileName<CreateDate' -d '%Y%m%d_%%f.%%e' *.MP4
```

This was found in the exiftools online forum: https://exiftool.org/forum/index.php?topic=8552.0

