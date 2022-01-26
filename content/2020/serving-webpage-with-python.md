---
Title: Serving Local Webpages with Python
Date: 2020-07-16
Tags: Python
Author: Joe
Keywords: pelican, pelican static site generator, ubuntu 20.4, github pages, python
Version: OS, Ubuntu 20.04 LTS, python, 3.7.4
---

This article is less of instruction and more documentation for myself since I keep forgetting the Python3 syntax. You can easily serve web pages locally using a bunch of languages and tools, but my preferred method is with Python. It has a simple server that can be quickly launched without a LAMP stack or anything crazy. 

**Note: this is definitely for local usage and not for production or facing the internet!**

[Python3 http.server](https://docs.python.org/3/library/http.server.html) help page

```bash
python -m http.server 8080
```
Run the above syntax in a terminal window in the folder that you want to serve. In my example above, "python" is mapped to python3 and 8080 is the port I want to serve at. Typical is 8000 but that is the port I serve my blog at for development and testing.  To view the server, open a web browser and go to the address:
```
localhost:8080
```

or whatever port you defined.