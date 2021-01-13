Title: Useful git Commands
Date: 2020-09-13
Tags: Ubuntu
Author: Joe
Keywords: ubuntu 20.4,
Status: Draft



```bash
ghp-import -m "<MESSAGE>" --cname=="www.joelotz.com" -b master output
```

List of staged files
```
git diff --name-only --cached
```

Unstage - remove files from git staging area
```
git reset
```

```
git status
```

https://stackoverflow.com/questions/6612630/git-add-all-except-ignoring-files-in-gitignore-file
`git add .` adds all files except those in .gitignore

If you want to add a directory in .gitignore file, `DIRECTORY/*` does not work, use `DIRECTORY`

delete file and remove from git
```
git rm FILE
git remove -r DIR
```
do not delete locally, just remove from git
```
git rm --cached FILE
```
