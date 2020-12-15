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
joe@Praimfaya:/mnt/DataDrive/Blog$ git add --all

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

pelican content -o output -s pelicanconf.py

ghp-import -m "I have no clue what I’m doing…" --no-jekyll -b master output

git push origin master