Title: Running FreeFileSync Backup from Crontab on Ubuntu
Date: 2020-05-26
Tags: Ubuntu
Author: Joe Lotz
Excerpt: Documenting my solution to running FreeFileSync backup from a crontab. 
Keywords: ubuntu 20.04, ffs, freefilesync, Error: Unable to initialize GTK+, is DISPLAY set properly?

It took me half a day, maybe 4 hours, to solve this problem and I want to document the solution. I wanted to use [FreeFileSync](https://www.linux-magazine.com/Online/Features/FreeFileSync/(offset)/3) to backup all my files to an external hard drive. I looked at [a bunch of other software](https://www.capterra.com/file-sync-software/) but what I want to do is pretty basic and everything else was too complicated for me. Regardless, I installed [FreeFileSync](https://freefilesync.org/), setup the configuration, and saved the “batch job”. Everything works smooth when manually run, but of course I want to automate the process and setup a cron job. 

I kept getting error messages. Many solutions suggested to use gnome-schedule but that appears to be defunct and no longer available for Ubuntu 20.04. I went down the path of trying to build it from source and yadda yadda. That wasted some time. Another error message I got was `Failed to load module canberra-gtk-module` - which was easily fixed.

```bash
sudo apt install libcanberra-gtk3-module
```

The error that really stumped me was `Error: Unable to initialize GTK+, is DISPLAY set properly?` After much googling the answer always headed into setting the DISPLAY variable but the solution of setting it to 0 or 0.0 wasn’t working. Maybe it was because I have two monitors, I really don’t know. Again, I don’t understand the details or why it works, but setting the DISPLAY to 1.0 worked for me. 

```bash
0 3 * * * env DISPLAY=:1.0 /usr/bin/FreeFileSync/FreeFileSync /home/joe/FreeFileSyncBackup/SyncSettings.ffs_batch
```

Where:

- `0 3 * * *` is the frequency that I want the cron to run, every night at 3am
- `/usr/bin/FreeFileSync/FreeFileSync` is the location of the program 
- `/home/joe/FreeFileSyncBackup/SyncSettings.ffs_batch` is my batch file that I created and saved within the FreeFileSync program

### Extras

In case you don’t know, `crontab -e` opens the file allowing you to add or edit the user-level cron jobs. Also, you can specify your editor as `EDITOR=gedit crontab -e` if you don’t want to use vi or nano or whatever is your default bash editor. 

I was also successful in putting this command in a shell script and running the shell script from cron - just in case you want to do something more complicated. 

### Update

When this script ran I received errors about “Unable to find or create trash directory.” Googling it looked like I was missing the trash dir `.Trash-1000` but that wasn’t the case. In the end, for some reason, it seems like only root can delete files from my external NTFS drive….but it worked when I performed the delete manually or from the program. To get around this I moved the above cron job from my user to root crontab via `sudo EDITOR=gedit crontab -e`. I am not sure if it’s a good idea to be running this as root…I’ll do more experiments and try to find a better solution.