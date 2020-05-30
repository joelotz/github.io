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
    pelican content -o output -s publishconf.py
    # collect and push the blog output folder to github pages
    #  in a branch called 'master'
    ghp-import -m "$inputStr" --no-jekyll -b master output
    git push origin master
    # save the "non-compiled" files of blog and push to a
    #  branch called 'content'
    git add content theme plugins publishconf.py pelicanconf.py blogmakeandgit.sh
    git commit -m "$inputStr"
    git push origin content
fi
