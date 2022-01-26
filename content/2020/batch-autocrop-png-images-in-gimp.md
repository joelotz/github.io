---
Title: Batch Autocrop png Images in Gimp
Date: 2020-07-10
Tags: Gimp
Author: Joe
Keywords: ubuntu 20.4, ffmpeg, gimp, batch autocropping
Version: OS, Ubuntu 20.04 LTS, Gimp, 2.10.18
---

This article is to document the solution I found for batch auto-cropping a bunch of images within [Gimp](https://www.gimp.org/). Keep in mind that this runs the “Crop to Content” command within the Image menu, so if you can’t achieve what you want *within* the program than this isn’t going to give you different results. 

To start, credit where credit is due. I didn’t want to learn how to write Gimp scripts so I found one from a Swede named Greg Hildström [here](http://www.hildstrom.com/projects/gimpscript/index.html), thanks Greg!

**batch-autocrop.scm**

```
  (define (batch-autocrop pattern)
  (let* ((filelist (cadr (file-glob pattern 1))))
    (while (not (null? filelist))
           (let* ((filename (car filelist))
                  (image (car (gimp-file-load RUN-NONINTERACTIVE
                                              filename filename)))
                  (drawable (car (gimp-image-get-active-layer image))))
                  
             (plug-in-autocrop RUN-NONINTERACTIVE
                                   image drawable)
                                   
             (gimp-file-save RUN-NONINTERACTIVE
                             image drawable filename filename)
             (gimp-image-delete image))
           (set! filelist (cdr filelist)))))
```

1. Copy the `batch-autocrop.scm` into the scripts folder 

Where do Gimp scripts and plugin live? It’s easy to find out. Open Gimp and within the top menu bar select `Edit\Preferences\Folders`, expand Folders out and Select “Scripts”. It is recommended to put your personal scripts into your configuration folder as circled in red below. 

![image of Gimp menu items](/images/2020/GimpCrop-00.png)

2. Within a terminal change into the directory of images you want to crop and run the script 
```bash
gimp -i -b '(batch-autocrop "*.PNG")' -b '(gimp-quit 0)'
```

![terminal view of batch command](/images/2020/GimpCrop-01.png)

If you are interested in what you just did continue reading. 

- `gimp` is the command, you can run `gimp -h` to view the help page 
- The flag `-i` means run without a user interface
- `-b` means run a batch command

Look up at the first line of the .scm script and you will see the definition of the batch command = “batch-autocrop pattern”. `batch-autocrop` is the command name and `pattern` is the input pattern of files you want to operate on. I don’t know why you need to wrap the batch command in both quotes and paranthesis, it seems to me that either one would be enough to differentiate the input, but regardless… the first batch command is `gimp -i -b '(batch-autocrop “*.PNG”)'` because I want to operate on everything in the current folder that ends with “.PNG”. For my particular configuration, capitalization was important; e.g. “.png” vs “.PNG” made a difference. 

Lastly we need to close out the session because we don’t have an interface. This is another batch command `-b  '(gimp-quit 0)'` meaning quite Gimp now. 

And there you have it!