Title: Running Shell Scripts on Files from Nautilus
Date: 2020-05-03
Tags: Ubuntu, bash
Author: Joe Lotz
Summary:
Keywords: ubuntu 20.04, nautilus, bash

​In a [previous post](fmpeg-converting-mp4-videos-to-mov.html) I wrote a script to transcode a video in an mp4 container to mov container. It would be really cool to simply right-click on the file and run the script. [AskUbuntu](https://askubuntu.com/questions/1031807/how-to-integrate-run-as-shell-script-in-right-click-menu-of-file-manager) had a decent guide that explained how.

First create a new file in the `/.local/share/nautilus/scripts/` folder using vi, gedit, or your favorite text editor.

```bash
cd ~/.local/share/nautilus/scripts/
gedit <name of script>
```

Now, of course, make the script executable.

```bash
chmod +x ~/.local/share/nautilus/scripts/<name of script.
```

### Writing the Video Transcode Script with FFMpeg

Here is the script I wrote, encorporating the ffmpeg command from the previous post. The variables allow the output file to be the same size/resolution as the input file. Depending on the size of the file it could take some time, so I added a zenity popup box so you have to install zenity (`sudo apt install zenity`) or comment out the pop-ups. It may be useful to add an progress-box for the future…

```bash
#!/bin/bash

## assumes FFPMEG is installed
## converts a mp4 vidoe file to mov container in order ot use in DVR

# strip new line char passed by Nautilus
FILENAME=$(echo $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS | sed -e 's/\r//g')

#convert to lowercase in order to check extension...i can't work the lowercase into the logic below so this is a work around
FILENAME2=${FILENAME,,}

#check to see if file ends with .mp4
if [ ${FILENAME2: -4} == ".mp4" ]
then
	# cut off the extension and rename to file.mov
	FILENAME3=$(echo "$FILENAME" | cut -f 1 -d '.') 
	NEWFILE="${FILENAME3}.mov"


	# determined width and height of the video
	# the assumption is the output file is desired to be the same same as input	
	WIDTH=$(ffprobe -v error -show_entries stream=width -of default=noprint_wrappers=1:nokey=1 "${FILENAME}")
	HEIGHT=$(ffprobe -v error -show_entries stream=height -of default=noprint_wrappers=1:nokey=1 "${FILENAME}")
	FRAMERATE=$(ffprobe -v error -select_streams v:0 -show_entries stream=avg_frame_rate -of default=noprint_wrappers=1:nokey=1 "${FILENAME}")

	# this is the processing magic, notice I use the original FILENAME variable due to my goofy hack
	# https://askubuntu.com/questions/907398/how-to-convert-a-video-with-ffmpeg-into-the-dnxhd-dnxhr-format
	ffmpeg -i "${FILENAME}" -c:v dnxhd -profile:v dnxhr_hqx -vf "scale=${WIDTH}:${HEIGHT},fps=${FRAMERATE},format=yuv422p10le" -c:a pcm_s16le "${NEWFILE}"

	# finished message box
	zenity --info --title "Procesing completed" --text "${FILENAME3}.mp4 has been transcoded to a .mov file at size ${WIDTH}:${HEIGHT} and framerate=${FRAMERATE}" --width=600

else # it does not end in .mp4 so do not process
	zenity --error --title "This is not an .mp4 file" --text "File must end with extension '.mp4'" --width=600
fi
```

