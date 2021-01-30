Title: Splitting Audio Files into Tracks Based on .cue File
Date: 2021-01-26
Tags: Audacity, Python
Keywords: Python, Audacity, label file, splitting tracks, cue file
Version: Audacity, 2.3.3, Python, 3.7.9



Here's a problem that I come across once in a while. Let’s say you’ve downloaded an album from torrent and the entire album is in a single file. Sure, you can load the .cue file into your favorite music player and play the different tracks but you really would like this album split into individual files for each track. 

!!! warning
	It's assumed that you are downloading ***legally*** obtained torrents. Don't sue me RIAA!!

You can, of course, load the flac/mp3 into [Audacity](https://www.audacityteam.org/), manually insert labels (for example at the arrow locations), and export tracks. But I'm going to show you a semi-automated method. 

![audacity_05](/images/2021/audacity_05.png)

Audacity has the ability to import label files. These are basically text files that tells the program at what starting/ending point to add the label and what the label’s… um… label should be. That’s great, but I don’t know where you get this label file from. This is not included with your (legally obtained!) torrent. But you do typically get a .cue file. If you got this file we are in the game.

<img src="/images/2021/audacity_01.png" alt="audacity_01" style="zoom:80%;" />

There is a site online that someone wrote that will convert for you here [http://grimblefritz.com/audacity/cue2lbl.php](http://grimblefritz.com/audacity/cue2lbl.php). 

Of course, being a geek I wrote my own Python script to do it for me!  Download the gist [here](https://gist.github.com/joelotz/49d99e6c464825a0e551146bd92369a3).

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Convert a music .cue file into a label file.

This module will accept an optional string attribute that specifies the input
.cue file. If this file is not provided in the call then file-select box will
be presented to the user. Output is a .txt file of labels that can be input
into Audacity.

Examples:
        $ python cue2labels.py
        $ python cue2labels.py "InputFile.cue"

"""

def stringtime_to_millisec(stringtime):
    """

    Parameters
    ----------
    stringtime : STRING
        A string in the form of "HH:MM:SS:MS", where MS are millisecs.
        Hours(HH) and Minutes(MM) are optional.
        Seconds(SS) and Millisecs(MS) are mandatory.
        Example: 10:05:12 = 10hrs, 5mins, 12ms

    Returns
    -------
    FLOAT
        Returns a the input stringtime as decimal seconds

    """
    hours, minutes, seconds, milliseconds = (["00", "00"] + stringtime.split(":"))[-4:]
    hours = int(hours[-2:])*360
    minutes = int(minutes[-2:])*60 
    seconds = int(seconds[-2:])
    milliseconds = float(milliseconds[-2:])/60
    return hours + minutes + seconds + milliseconds


def parse_cue(cue_filename):
    """
    
    Parameters
    ----------
    cue_filename : STRING
        The name of the .cue file to be read and parsed.

    Returns
    -------
    track_times : LIST
        The time that the audio track starts, as given in the .cue file, 
        in decimal seconds
    titles : LIST
        The title of the track, as given in the .cue file.

    """
    from re import findall
    
    file = open(cue_filename, 'r') 
    track_times = [float(0)]
    titles = []
    
    while True: 
        # Get next line from file 
        line = file.readline() 
      
        # if line is empty end of file is reached 
        if not line: 
            break
        if line.strip()[:5] == 'INDEX 01':
            stringtime = stringtime_to_millisec(line.strip())
            if stringtime != float(0):
                track_times.append(stringtime)
        elif line.strip()[:5] == 'TITLE':
            track = findall(r'"([^"]*)"', line)
            titles.append(track)                

    # I've had trouble in the past         
    if not titles or track_times[-1]==float(0):
         warning_string = '''There is someting wrong with the .cue file, it\'s not formatted properly.
         Unable to continue processing!'''
         sys.exit(warning_string)     
    file.close() 
    return track_times, titles

    
def write_labels(label_filename, track_times, titles):
    """

    Parameters
    ----------
    label_filename : STRING
        The desired path/name of the output label file.
    track_times : LIST        
        The time that the audio track starts, as given in the .cue file, 
        in decimal seconds
    titles : LIST
        The title of the track, as given in the .cue file.

    Returns
    -------
    bool

    """
    # Due to the format of the .cue file, the first track title may be the album title
    if len(titles) > len(track_times):
        titles.pop(0)
        
    file = open(label_filename, "w")
    # Write out in tab delimited format
    for i in range(len(titles)):
        line = f"{track_times[i]:.5f}\t{track_times[i]:.5f}\t{titles[i][0]}"
        file.write(line)
        file.write("\n")
    
    file.close()
    return True


if __name__ == "__main__":
    import sys
    import os
    
    # Check if .cue file was given in the python call
    try:
        cue_filename = str(sys.argv[1])
    # If not, ask user to select        
    except:
        from tkinter.filedialog import askopenfilename
        cue_filename = askopenfilename(title="Select a cue file", filetypes=(("cue files",'*.cue'),))
        ## EXIT if user selects cancel
    
    # Read cue file and parse out the times and titles
    track_times, titles = parse_cue(cue_filename)
    # Make a label file name
    label_filename = os.path.splitext(cue_filename)[0]+'_labels.txt'
    # Write times and tracks to label file in proper format
    write_labels(label_filename, track_times, titles)
    print("File created")
```

You can run this script with or without specifying the optional cue file string attribute. If you don’t specify it the script will present a popup for you to select it:

```bash
$ python cue2labels.py
```

or

```bash
$ python cue2labels.py "inputfile.cue"
```
Your cue file contains the albums information, like album title, metadata, track titles, starting position, etc. It will look something like this:
<img src="/images/2021/audacity_03.png" alt="audacity_03" style="zoom:80%;" />

At this point you can convert the cue to a label file, either online or with the Python script. If you ran the Python script you will have a new file in the same directory as the cue file. Like this:

<img src="/images/2021/audacity_02.png" alt="audacity_02" style="zoom:80%;" />

The label file will be pretty simple with the track starting times and title names and will look like this:

<img src="/images/2021/audacity_04.png" alt="audacity_04" style="zoom:80%;" />

Now we are on the home stretch! Open Audacity and import your music flac/mp3 file. Now go to `File > Import > Labels...`, select the label file.

The labels are now magically inserted at the track start times with the title filled in!

![audacity_06](/images/2021/audacity_06.png)

From here go to `File > Export > Export Multiple...` yadda, yadda. The result are individual files for each track as shown here:

<img src="/images/2021/audacity_07.png" alt="audacity_07" style="zoom:80%;" />

On a final and unrelated note, if you've never heard of [Tower of Power](https://en.wikipedia.org/wiki/Tower_of_Power) you are missing out. It's an R&B band started in the 70's that has a *killer* horn section.

<iframe width="560" height="315" src="https://www.youtube.com/embed/oAatPPEaZDA" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>