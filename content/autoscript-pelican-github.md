Title: Pelican Generate and Publish to Github Pages on Ubuntu
Date: 2020-05-29
Tags: Ubuntu, Pelican
Author: Joe Lotz
Keywords: pelican, pelican static site generator, ubuntu 20.4, ghp-import, github, github pages
Version: Version: OS, Ubuntu 20.04 LTS, bash, 5.0.16(1)-release, python, 2.7.4, Pelican, 4.2.0

I thought I’d share an automation script I wrote that builds my Pelican site, asks for a commit message, then pushes it to github pages. This script assumes [zenity](https://packages.ubuntu.com/focal/zenity) is installed on the system. If not, easily install via:
```bash
sudo apt update
sudo apt install zenity
```
I would highly recommend setting up `ghp-import` and this script assumes you have. Follow [these instructions](https://opensource.com/article/19/5/run-your-blog-github-pages-python) if you  need to install/configure it. 

Here’s the script, save it in the root directory of your pelican blog and make it executable.
```bash
#!/bin/bash

# ========================================================================
# Automated script to build Pelican blog, ask for a commit message, then
#   push to github pages.
#
# Requirement:
#   Assumes zenity is installed, ghp-import is installed, and
#       assumes github credentials are stored locally
#

# Input user commit message
inputStr=$(zenity --entry --title="Commit Message" \
    --text="What is your commit message?" --width=600)

# If the canceled button is pressed, exit script
if [ "$?" != 0 ]
then
    echo "Commit message was canceled, abandoning script"
    exit
fi

# If the commit message is empty, exit script
if [ -z "$inputStr" ] 
then    
    echo "Commit message is empty, abandoning script"
    exit
else # Else, run 

    # Build the blog    
    pelican content -o output -s pelicanconf.py
    # collect and push the blog output folder to github pages
    #  in a branch called 'master'
    ghp-import -m "$inputStr" -b master output
    git push origin master
    # save the "non-compiled" files of blog and push to a
    #  branch called 'content'
    git add --all
    git reset output/* plugins/* __pycache__/*
    git commit -m "$inputStr"
    git push origin content
fi
```
A zenity input box is used to capture the commit message. 
![pelicanGithub-01](/images/pelicanGithub-01.png)
```bash
pelican content -o output -s publishconf.py
```
This is your [standard command](https://docs.getpelican.com/en/stable/publish.html) for generating and deploying a pelican blog. This next line is where things get interesting. 
```bash
ghp-import -m "$inputStr" --no-jekyll -b master output
git push origin master
```
This command is saying, “take the contents of the folder ‘/output’, add to the master branch, make the commit message what you typed into the input box". Then push the local master branch to the remote repo. I am assuming you have already locally cached your github credentials so you don't need to enter them, [[1]](https://help.github.com/en/github/using-git/caching-your-github-password-in-git) and [[2]](https://git-scm.com/docs/git-credential-store).

```shell
git add --all
git reset output/* plugins/* __pycache__/*
git commit -m "$inputStr"
git push origin content
```

This last bit is a little tricky. First, I want to add everything in my blog folder then remove from staging the output folder (which I’m already pushing to the master branch), the plugin folder, and the \__pycache__ folder. I believe you can also accomplish this with a .gitignore file. Next, commit and push the ‘source’ files or all my non-generated pages to the content branch and push to the remote repo. This way I can host my html generated files as a website on github pages but I can also store/backup my source files. This prevents the need to have multiple repositories, one for hosting the blog and one for backing up the files. 

![pelicanGithub-02](/images/pelicanGithub-02.png)

In your <name>github.io repository, click the branch button and you will see the ‘master’ which is default and contains the generated html files. You can also click the ‘content’ branch and see your source files.