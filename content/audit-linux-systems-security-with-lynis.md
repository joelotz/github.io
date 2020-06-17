Title: Auditing Linux Systems with Lynis
Date: 2020-05-01
Tags: Ubuntu, Pelican, lynis
Author: Joe
Keywords: pelican, pelican static site generator, ubuntu 20.4, lynis, security
Version: OS, Ubuntu 20.04 LTS, ClamAv, 0.102.3
Status: draft

Linux is not immune to security threats like malware.

Assuming you are on Ubuntu 20.04, the Lynis package in the repos is nearly guaranteed to be out of date. They always are. So, you can install from repos as `sudo apt install lynis` but you will receive an audit warning. At the time of this writing, version 2.6.6 was available, released on 2018-07-06, being nearly 2 years old. A better option is to install the latest from github. 

```bash
cd /usr/local/bin # this is where all the apps go
sudo git clone https://github.com/CISOfy/lynis
```
On a side-note, my system seemed to want to install the package named `menu`, I'm not an expert but you may want to install this 

```bash
cd lynis
sudo ./lynis audit system --use-cwd
```

I believe the flag `--use-cwd`  is equivelant to the older flag `--quickstart` 
https://cisofy.com/documentation/lynis/get-started/#first-run

The results are displayed on screen during the system scan. Additional details are logged in a separate file (default: /var/log/lynis.log).

### Activating Firewall
iptables no rules are active
Ubunut comes with a software firewall, but the rules or iptables are empty. It seems like they should have a default setting that can be configured during OS installation

`sudo apt install gufw`
https://askubuntu.com/questions/178616/do-i-need-to-activate-the-firewall-i-only-use-ubuntu-for-a-home-desktop-use
https://help.ubuntu.com/community/DoINeedAFirewall
https://ubuntuforums.org/showthread.php?t=1876124
https://kifarunix.com/install-and-use-clamav-on-ubuntu-20-04/

### Installing Antivirus
https://vitux.com/secure-ubuntu-with-clamav-antivirus/
https://kifarunix.com/install-and-use-clamav-on-ubuntu-20-04/
```bash
sudo apt update
sudo apt install clamav clamav-daemon clamtk
```
Verify installation `clamscan --version`

Manually update the virus database. First stop the freshclam service;
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
By default, ClamAV will do a check for new virus definitions every hour, if you want to change this parameter you can edit the file `/etc/clamav/freshclam.conf`.

```nano /etc/clamav/freshclam.conf```
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

https://askubuntu.com/questions/591964/clamav-cant-read-file-error
```
sudo clamscan --infected --remove --exclude-dir="^/sys" --recursive /
```
