Title: ImageMagick Converting png Images to a Custom pdf
Date: 2020-04-30
Category: 
Tags: Ubuntu, ImageMagick
Author: Joe
Summary:
Keywords: ubuntu 20.04, imagemagick

### Installing ImageMagick on Ubuntu 20.04

```bash
sudo apt update
sudo apt build-essential checkinstall # provides all the libraris for compiling
sudo apt build-dep imagemagick # install compilation dependencies
```

The first time I did this installation the program complained and errored that it was missing [delegates]( http://www.imagemagick.org/download/delegates/) when I tried to manipulate the png images. [This page](https://askubuntu.com/questions/745660/imagemagick-png-delegate-install-problems) from StackExchange explained how to install the image libraries. I didn’t know which ones were important or how often they are used so I installed them all.

```bash
sudo apt install libx11-dev libxext-dev zlib1g-dev libpng12-dev libjpeg-dev libfreetype6-dev libxml2-dev
```

This should install all the needed image libraries. Unfortunately, ImageMagick itself can’t be installed the same way. We need to build it. 

First download the binary tar, extract it, and move into the newly extracted directory.

```bash
wget https://www.imagemagick.org/download/ImageMagick.tar.gz
tar xf ImageMagick.tar.gz
cd ImageMagick-7*
```

While in the source code directory execute the `configure` command. 

```
./configure
```

Next compile with the `make` command.

```bash
make
```

Install ImageMagick.

```bash
sudo make install
```

This will install the compiled binaries. Now run `ldconfig` command to link the static libraries. 

```bash
sudo ldconfig /usr/local/lib
```

Confirm installation and final check. Run the `identity` command to confirm that “something” is installed. 

```bash
indentify -version
```

 The I[mageMagick website](https://imagemagick.org/script/download.php) also has a couple commands to verify installation.

```bash
identify logo.gif
display logo.gif
```

### Converting a Bunch of Images to a pdf

I have a bunch of scan images of an old handwritten recipe book. The originals are in [A5 paper size](https://en.wikipedia.org/wiki/Paper_size) and I’d like each page of the pdf to be the same size. This is pretty simple with ImageMagick’s `convert` command. 

```bash
cd ImageDir
convert *.png \
	-resize 595x421 \
	-background white \
	-gravity North \
	-extent 595x421 \
	output.pdf
```

OK, this is complicated and took a couple hours to figure out. So what is going on here?

1. It’s converting all files in the current directory with the file type .png, so be careful. You can also specify the images explicitly by just listing them out.

2. The scanned images are high resolution and pretty big, something around 1200x900. I want to save and keep these but the size is too big. The `-resize` option is sizing the images to imagemagick 595x421. [This is the A5 page size (dots per inch) in landscape.](https://imagemagick.org/script/command-line-options.php#page)

3. `-gravity` [must go before `-extent`](https://imagemagick.org/script/command-line-options.php#extent). You can find all the options for an argument using `identify -list <option>`. “North” means center the images on the page horizontally and top-aligned vertically. 

4. `-extent` sets the image size. At [page size is dots per inch for A5](https://imagemagick.org/script/command-line-options.php#page) is 421x595.

5. Note: you can specify the dpi with the `-density` option. The [default is 72dpi](https://imagemagick.org/script/command-line-options.php#density) so I left it as is. 

#### Lower Res/ Smaller File

You can make a lower resolution and smaller file size for web or email.

```bash
convert *.png -compress jpeg -resize 595x421 -background white \
	-gravity North -extent 595x421 output.pdf
```

### Exiftool Adds pdf Metadata

Easily install [Exiftool](https://exiftool.org/) on Ubuntu.

```bash
sudo apt install libimage-exiftool-perl
```

There are a bunch of [tutorials](https://linoxide.com/linux-how-to/install-use-exiftool-linux-ubuntu-centos/) on using Exiftool.

Changing the exif data within the pdf file to add some fields is quite easy.

```bash
exiftool \
	-Creator="Joe Lotz" \
	-keywords="recipebook;recipes" \
	-Author="Grandma" output.pdf
```

