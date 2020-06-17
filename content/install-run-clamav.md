Title: Installing ClamAV on Ubuntu
Date: 2020-06-05
Tags: Ubuntu, ClamAV
Author: Joe
Keywords: ubuntu 20.4, anti-virus, clamav
Version: OS, Ubuntu 20.04 LTS, ClamAv, 0.102.3

Linux is not immune to security threats like malware and viruses, however, there is a large debate around whether or not anti-virus software is needed on linux. 

- [Why You Don’t Need an Antivirus On Linux (Usually)](https://www.howtogeek.com/135392/htg-explains-why-you-dont-need-an-antivirus-on-linux-and-when-you-do/)
- [Why You Still Don’t Need Antivirus Software on Linux in 2020](https://linuxhint.com/why_no_antivirus_linux/)
- [Do I need anti-virus software?](https://help.ubuntu.com/stable/ubuntu-help/net-antivirus.html.en)
- [Does Linux need antivirus?](https://www.comparitech.com/antivirus/does-linux-need-antivirus/)

This post will explain why I choose to install anti-virus software, how to install, and how to setup a cron job for automatically executing it.

If you quickly browse the articles listed above or do your own google search you find strong advocates on both sides of the fence. The official Ubuntu website says "Anti-virus software does exist for Linux, but you probably don’t need to use it. Viruses that affect Linux are still very rare. " I largely follow this logic but add a little twist - I think if you engage in risky behavior you need to protect yourself. So let's say, for example, that someone downloads music torrents or cracked ebooks, hypothetically. These come from shady sources and are great opportunities for infecting your system with virus, [rootkits](https://nakedsecurity.sophos.com/2012/11/27/flaming-retort-linux-rootkit-news-provides-some-comic-relief/), [ransomware](https://www.zdnet.com/article/this-new-ransomware-is-targeting-windows-and-linux-pcs-with-a-unique-attack/), or botnets. So while I don't scan the entire system, every night I scan my ~/Downloads/, ~/Torrents/, and ~/Music/ directories. I think if you host any servers like an email server, FTP server, or a Samba File server you should probably scan those too. If you agree with me, I'll show you how to easily install and setup [ClamAV](https://www.clamav.net/). 

Simply update and install the packages;
```bash
sudo apt update
sudo apt install clamav clamav-daemon
```
You can verify installation;
```bash
clamscan --version
```
By default, ClamAV will do a check for new virus definitions every hour, if you want to change this parameter you can edit the file `/etc/clamav/freshclam.conf`.
```bash
gedit /etc/clamav/freshclam.conf
```
And change the following line:
```bash
# Check for new database 24 times a day
Checks 24
```
to
```bash
# Check for new database 1 times a day
Checks 1
```
The virus database is going to most-likely be out of date since it hasn't had a chance to update. "Freshclam" is the daemon that updates the database. To manually update the virus database, first stop the freshclam service;
```bash
systemctl stop clamav-freshclam
```
Then update the database;
```bash
sudo freshclam
```
Then restart it and enable to run on system boot/startup;
```bash
systemctl start clamav-freshclam
systemctl is-enabled clamav-freshclam
```
Here are some good articles on all the different options you can use:

- https://vitux.com/secure-ubuntu-with-clamav-antivirus/
- https://kifarunix.com/install-and-use-clamav-on-ubuntu-20-04/

Here is my command;
```bash
clamscan --remove=yes --recursive=yes --verbose /home/joe/Downloads/ /mnt/DataDrive/Music/ | grep FOUND >> /home/joe/VirusScanReports/virus-scan-report-`date +"%Y-%m-%d"`.txt
```
You can view the options via `clamscan --help`, but I'll decipher my choices.

- `--remove=yes` means "Remove any infected files", this can be slightly dangerous if you are scanning system files as removing a file can bonk-up things. In my case I'm scanning files that I know are "meaningless" so blast them away if they are infected.
- `--recursive=yes` means "Scan sub-directories recursively", this is obvious.
- `--verbose` means...well, "Be verbose". It can take a while to scan large directories, especially if you choose the whole system, and when it's scanning and not showing anything I get scared that maybe something locked up. So I like to see the output to know that it's actually working and scanning. 
- And then you list your directory/directories afterwards. 
- You could even exclude a directory from being scanned with a flag like this `--exclude-dir="^/systemDir"
- Finally, pipe the report on any “found” viruses to a text file.

As a side note, my commands are verbose as well. I tend to not use the flags, like `-v` instead of `–-verbose`  because 3 months from now when I look back I have a tendency to forget what the flags stand for.  So while I could use `-r` I like to completely “spell it out” as `--recursive=yes`.

### Cron tab

Access the system or root cron tab via `sudo crontab -e` or you can specify your favorite text editor with `sudo EDITOR=gedit crontab -e`. I have it specified to run every night at 2am, before my [backup](running-freefilesync-backup-from-crontab-on-ubuntu.html) runs.

```bash
0 2 * * * clamscan --remove=yes --recursive=yes --verbose /home/joe/Downloads/ /mnt/DataDrive/Music/ | grep FOUND >> /home/joe/VirusScanReports/virus-scan-report-`date +"%Y-%m-%d"`.txt
```

### Optional Credit
I think I can improve on this by only saving a file if a virus is found. Currently, there is a log file saved everyday and if there is no virus then the file is empty. That’s a whole bunch of empty files to be looking at all the time. I could write a script that looks at the results and *only if* it is *not empty* then I could push the results to a Zenity message box or email myself. Since these are non-essential media files I think it would be easiest to just initiate a message box. 