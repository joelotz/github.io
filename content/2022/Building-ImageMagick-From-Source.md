---
Title: Building Imagemagick 7.1 with HEIC Support from Source
Date: 2022-07-01
Tags: ImageMagick, Ubuntu
Author: Joe
Keywords: imagemagick, ubuntu 22.04, HEIC
Version: Ubuntu, 20.04 LTS, ImageMagick, 7.1.0-39
---

I upgraded my Ubuntu distro from 20.04 to 22.04 and ImageMagick didn’t come along for the ride… I’m not sure what happened. In this post I build ImageMagick 7.1.0-39 with HEIC support from source on Ubuntu 22.04.  

I first installed from the apt package manager (with no errors) but when verifying the installation I got this code:

`convert: error while loading shared libraries: libwebp.so.6: cannot open shared object file: No such file or directory`

After some Googling around I decided to try building from source with HEIC support as I now have an iPhone from work and would like to use ImageMagick to convert .heic to .jpg. Building from source turned out to be surprisingly easy.

I found a gist from github user [Alexandr Evstigneev](https://gist.github.com/hurricup) and made some tweaks to his [installation gist](https://gist.github.com/hurricup/e14ae5bc47705fca6b1680e7a1fb6580).

Here is mine:

[gist:id=901b3d21b171a64b9e1a4191edc061da]

You can obviously run it as a script or if you are timid (like me) you can copy/paste each line and look for errors. 