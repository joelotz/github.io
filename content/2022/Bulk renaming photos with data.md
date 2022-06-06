---
Title: Bulk Rename Photos to Date Taken with Exiftool
Date: 2022-03-25
Tags: Exiftool, Ubuntu
Author: Joe
Keywords: exiftool, ubuntu 20.04
Version: Ubuntu, 20.04.4 LTS, Exiftool, 11.88
---

In this post I document the Exiftool bash command for renaming a folder of photo files according to their creation date/time.  I like this because my wife’s phone saves images as “IMG_YYMMDD_XXXXX.JPG” and my phone saves images as “YYMMDD_XXXXX.jpg”. So this combination doesn’t allow me to sort a folder full of images according to filename properly. If I do any sort of editing on her images the ModifiedDate is changed and then I can’t even sort by that in the file explorer. 

So here is the command:

```bash
exiftool '-filename<CreateDate' -d %Y%m%d_%H%M%S%%-c.%%le -ext jpg -r /mnt/Drive/Folder/	
```

Source; https://ninedegreesbelow.com/photography/exiftool-commands.html#rename

- **'-filename<CreateDate'** means rename the image file using the image's creation date and time.
- **-d** means "[Set format for date/time values](http://owl.phy.queensu.ca/~phil/exiftool/exiftool_pod.html)".
- **%Y%m%d_%H%M%S%%-c.%%le**, used in conjunction with "**-d**" specifies the format to use for the date and time when renaming the file. Breaking the format down:
	- **%Y%m%d_** means the first part of the new file name should be composed of the four digit creation-date year, followed by the two digit month month and day, both represented by two digits. The underscore **_** means put in an underscore after the date part of the file name.
	- **%H%M%S** means add the hour, minute, and second of the creation time, all represented by two digits. This ensures a *mostly* unique filename, the next option will ensure it. 
	- **%%-c** means that if two images have the same file name up to this point in the naming process, add "[a copy number which is automatically incremented](http://owl.phy.queensu.ca/~phil/exiftool/exiftool_pod.html)" to give each image a unique name. The "-" before the "c" isn't really necessary, but it puts a dash before the copy number.
	- **.%%le** means keep the original file name extension, but make it lower-case if it was originally upper-case, a nice option if the cameras uses "JPG" instead of "jpg". 
- **-ext jpg -ext mp4** means only rename files with the "jpg" or “mp4” extension. To rename all image files in the source folder, don't specify any extensions. 
- **-r** means execute this command recursively for every image file in the top "source" folder (that is, the folder where all the files to be renamed are located), and also for the image files in all the source folder's subfolders, sub-subfolders, and so on.
- **/mnt/drive/folder** is the absolute path to the top folder holding all the images to be renamed (your path will be different, of course).

