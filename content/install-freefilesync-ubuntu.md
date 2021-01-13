Title: Installing FreeFileSync in Ubuntu
Date: 2021-01-13
Tags: Ubuntu, FreeFileSync
Author: Joe
Keywords: ubuntu 20.4, FreeFileSync installation,
Version: OS, Ubuntu 20.04 LTS, FreeFileSync, 11.5


Go to https://freefilesync.org/download.php and download the latest version for Ubuntu. For most browsers, the default download location is the directory `~/Downloads`. 

Where do you install your personal software? This is something you may or may not have an opinion about, either way you need to make a decision. When you install software through Software Updater or `apt-get` the location is `/bin/<package>` but it’s generally accepted that you don’t put manually-installed packages there. 

> The [Linux Standard Base](http://en.wikipedia.org/wiki/Linux_Standard_Base) and the [Filesystem Hierarchy Standard](http://en.wikipedia.org/wiki/Filesystem_Hierarchy_Standard) are arguably the standards of where and how you should install software on a Linux system and would suggest placing software that isn't included in your distribution either in /opt or /usr/local/ or rather subdirectories therein (/opt/<package>  /opt/<provider>  /usr/local/bin).
>
> — from https://unix.stackexchange.com/questions/127076/into-which-directory-should-i-install-programs-in-linux

For me, I “install” in `/opt/` so these instructions assume that location. 

```bash
sudo tar -zxvf ~/Downloads/FreeFileSync_*_Linux.tar.gz -C /opt
```
This command extracts the compressed tar and puts the contents in the `/opt/` directory. The contents are already contained within a directory named `FreeFileSync`, so need to create one. 

Next we need to create a shortcut. There is an example shortcut file provided as `/opt/FreeFileSync/FreeFileSync.Example.desktop` that you can copy and then edit, but I find it easier just to create a blank file and copy/paste text. Type this command to create a file and open it in an editor.

```bash
gedit ~/.local/share/applications/FreeFileSync.desktop
```
Copy the text below into the empty file, save, and close.
```
[Desktop Entry]
Type=Application
Name=FreeFileSync
Comment=Keep files and folders synchronized
Terminal=false
Icon=/opt/FreeFileSync/Resources/FreeFileSync.png
Exec=/opt/FreeFileSync/FreeFileSync %F 
NoDisplay=false
Terminal=false
Categories=Utility;FileTools;
StartupNotify=true
```
You can do the same for RealTimeSync if you want.
```bash
gedit ~/.local/share/applications/RealTimeSync.desktop
```
Copy the text below, save, and close.
```
[Desktop Entry]
Type=Application
Name=RealTimeSync
Exec=/opt/FreeFileSync/RealTimeSync %f
Icon=/opt/FreeFileSync/Resources/RealTimeSync.png
NoDisplay=false
Terminal=false
Categories=Utility;FileTools;
StartupNotify=true
```

### Updating FreeFileSync

When you want to update versions, simply “install” the latest version into your installation directory per the instructions above. For example, let’s say you have version 11.1 and want to update to the latest version which happens to be 11.5. In this example, I assume you have previously put the package in `\opt\FreeFileSync\`. 

Download the tar.gz file, uncompress it into the existing `\opt\FreeFileSync\` directory. Done. 