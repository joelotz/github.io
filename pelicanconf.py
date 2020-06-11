#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Joe'
SITENAME = 'Delving into Delusion'
SITEURL = 'https://joelotz.github.io'
PATH = 'content'
TIMEZONE = 'Asia/Kolkata'
DEFAULT_LANG = 'en'

THEME = "theme/flaskymod"

## FLASKY CONFIGURATION #############################################
# Navigation sections and relative URL:
SECTIONS = [('Blog', 'index.html'),
        ('Archive', 'archives.html'),
        ('Tags', 'tags.html')]
#        ('Projects', 'pages/projects.html'),
#        ('Talks', 'pages/talks.html'),
#        ('About', 'pages/about-me.html')]

DEFAULT_CATEGORY = 'Uncategorized'
DATE_FORMAT = { 'en': '%B %d, %Y' }
DEFAULT_DATE_FORMAT = '%B %d, %Y'
DEFAULT_PAGINATION = 15
PDF_GENERATOR = False
REVERSE_CATEGORY_ORDER = True

FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/{slug}.rss.xml'

OUTPUT_PATH = 'output/'
# static paths will be copied under the same name
STATIC_PATHS = ["images"]

TYPOGRIFY = True

# Optional social media links
# =============================
#DISQUS_SITENAME = "your_disqus_user"
TWITTER_USERNAME = 'lotzjoe'
LINKEDIN_URL = 'https://www.linkedin.com/in/joelotz/'
GITHUB_URL = 'http://github.com/joelotz'
#FACEBOOK_URL = 'http://www.facebook.com/you'
#GOOGLEPLUS_URL = 'https://plus.google.com/your_profile_id/posts'
#PINTEREST_URL = 'http://pinterest.com/you'
#MAIL_USERNAME = 'your_user'
#MAIL_HOST = 'gmail.com'

# Optional analytic trackers
# =============================
GOOGLE_ANALYTICS_ACCOUNT = 'UA-48351953-1 '
#PIWIK_URL = 'myurl.com/piwik'
#PIWIK_SSL_URL = 'myurl.com/piwik'
#PIWIK_SITE_ID = '1'

# A list of files to copy from the source to the destination
#FILES_TO_COPY = (('extra/robots.txt', 'robots.txt'),)

LOAD_CONTENT_CACHE = False
CACHE_CONTENT = False

RELATIVE_URLS = False
## FLASKY CONFIG END ###########################################


## IPYNB PLUGIN CONFIGURATION ##################################
MARKUP = ('md', 'ipynb')
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup', 'stardate', 'pelican-gist']

# if you create jupyter files in the content dir, snapshots are saved with the same
# metadata. These need to be ignored. 
IGNORE_FILES = [".ipynb_checkpoints"]  

## END IPYNB PLUGIN CONFIG ##################################

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

#DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
