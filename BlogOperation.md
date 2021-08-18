#### Notes

1. On Win10 open and run from Anaconda Prompt
2. On Win10, it seems to rename the file extension as capital which is screwing up everything. 

#### Pulling Remote into Local

```bash
git pull remotename branchname
```



#### My Build Workflow

```bash
pelican content -o output -s pelicanconf.py

cd output
git add .
git status 
git commit -m ""
git push origin master

cd ..
git add .
git status
git commmit -m ""
git push origin content
```

#### Other useful commands

```bash
git reset FILE #pulls file out of staging
git rm FILE #deletes file locally and from repo
git rm -r DIR #deletes dir and contents locally/repo
git rm --cached FILE #deletes file only from repo
git rm -r --cached DIR #deletes dir only from repo

ls -a #lists hidden files in dir
```

#### Rebuilding Fresh from Start

```bash
joe@Praimfaya:/mnt/DataDrive$ git clone -b content https://github.com/joelotz/joelotz.github.io.git Blog
joe@Praimfaya:/mnt/DataDrive$ cd Blog
joe@Praimfaya:/mnt/DataDrive/Blog$ git clone -b master https://github.com/joelotz/joelotz.github.io.git output

<<Double Checking>>
joe@Praimfaya:/mnt/DataDrive/Blog$ git pull origin content
joe@Praimfaya:/mnt/DataDrive/Blog$ cd output
joe@Praimfaya:/mnt/DataDrive/Blog/output$ git pull origin master

<<Move new files into folder>>

<<Stage new files>>
joe@Praimfaya:/mnt/DataDrive/Blog$ git add .

<<Check what is staged>>
git diff --name-only --cached

<<Commit and push>>
joe@Praimfaya:/mnt/DataDrive/Blog$ git commit -m "message"
joe@Praimfaya:/mnt/DataDrive/Blog$ git push origin content

```

Show all hidden files = ls -ld .?*

```
git rm --cached -r .
# Remove everything from the index.

git reset --hard
# Write both the index and working directory from git's database.
```

### Serving html on python3 server

`python -m http.server `

Defaults to port 8000

`python -m http.server 7800`

Starts on port 7800

### Killing a process on Port 8000

```
sudo kill -9 `sudo lsof -t -i:8000`
```