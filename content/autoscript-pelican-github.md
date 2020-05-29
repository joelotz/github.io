Title: Pelican Generate and Publish to Github Pages on Ubuntu
Date: 2020-05-29
Tags: Ubuntu, Pelican
Author: Joe Lotz
Keywords: pelican, pelican static site generator, ubuntu 20.4, ghp-import, github, github pages
Status: Draft

I thought I’d share an automation script I wrote that builds my Pelican site, asks for a commit message, then pushes it to github pages. This script assumes [zenity](https://packages.ubuntu.com/focal/zenity) is installed on the system. If not, easily install via:
```bash
sudo apt update
sudo apt install zenity
```
```
#!/bin/bash

# ==============================================
# Automated script to build Pelican blog, ask for a commit message, then
#   push to github pages.
#
# Assumes zenity is installed
# Assumes github credentials are stored locally
#
inputStr=$(zenity --entry --title="Commit Message"\ 
    --text="What is your commit message?" --width=600)

pelican content -o output -s publishconf.py
ghp-import -m "$inputStr" --no-jekyll -b master output
git push origin master
git add content
git commit -m "$inputStr"
git push origin content
```
Starting on line 10, a zenity input box is used to capture the commit message. 




