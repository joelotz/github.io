Title: Operating a Pelican Website
Date: 2020-05-03
Category: 
Tags: Ubuntu, Pelican
Author: Joe
Summary: These are my notes 
Keywords: ubuntu 20.04, pelican
Status: draft

These are my notes that I can refer back to if I have any questions.

### “Building” the Site, aka Site Generation

https://docs.getpelican.com/en/4.2.0/publish.html#site-generation

To generate a single file:

`pelican content` or `pelican content -o output -s pelicanconf.py`	

`make html`

`invoke build`

### Killing the Webserver

During development I often invoke the server

`pelican –listen` 

`make devserver`

`invoke serve` or `invoke livereload`

but I don’t always shut it down correctly. 

https://stackoverflow.com/questions/12647196/how-do-i-shut-down-a-python-simplehttpserver

https://stackoverflow.com/questions/4465959/python-errno-98-address-already-in-use

### Pushing to Github Pages

https://pages.github.com/

```bash
cd output
git add --all
git commit -m "this is my commit message"
git push -s origin master	
```



 