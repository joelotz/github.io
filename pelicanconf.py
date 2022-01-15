#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Joe Lotz'
SITENAME = 'Delving into Delusion'
SITEURL = 'http://www.joelotz.com'
TIMEZONE = 'Asia/Kolkata'
DEFAULT_LANG = 'en-us'
THEME = "theme/flaskymod"
DATE_FORMAT = { 'en': '%B %d, %Y' }

SLUGIFY_SOURCE = 'title'
PDF_GENERATOR = False


## PATHS ##
SECTIONS = [('Blog', 'index.html'),
        ('Archive', 'archives.html'),
        ('Tags', 'tags/tags.html')]
RELATIVE_URLS = False
PATH = 'content/'
USE_FOLDER_AS_CATEGORY = True

OUTPUT_PATH = 'output/'
OUTPUT_RETENTION = [".git"]




## DEFAULT CONFIGS ##
#DEFAULT_CATEGORY = 'misc'
DEFAULT_DATE_FORMAT = '%B %d, %Y'  # Jan 01, 2000
DEFAULT_PAGINATION = 15

#REVERSE_CATEGORY_ORDER = True


## FEEDS ##
FEED_ALL_RSS = None
FEED_ALL_ATOM = 'blog/all.atom.xml'
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


## PAGES ##
CATEGORIES_SAVE_AS = ''
INDEX_SAVE_AS = 'blog/index.html'
TAGS_SAVE_AS = 'blog/tags/tags.html'
ARCHIVES_SAVE_AS = 'blog/archives.html'

ARTICLE_URL = 'blog/{date:%Y}/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{slug}.html'

TAG_URL = 'blog/tags/{slug}/'
TAG_SAVE_AS = 'blog/tags/{slug}/index.html'

CATEGORY_URL = ''
CATEGORY_SAVE_AS = ''

AUTHOR_URL = ''
AUTHOR_SAVE_AS = ''

DRAFT_URL = 'blog/drafts/'
DRAFT_SAVE_AS = 'blog/drafts/{slug}.html'


# static paths will be copied under the same name
#STATIC_PATHS = ['images', 'extra/CNAME', 'extra/.nojekyll', 'extra/index.html']
STATIC_PATHS = ['images', 'extra']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},'extra/.nojekyll': {'path': '.nojekyll'}, 'extra/index.html': {'path': 'index.html'}}

TYPOGRIFY = True
WITH_FUTURE_DATES = False #If disabled, content with dates in the future will get a default status of draft.

LOAD_CONTENT_CACHE = False
CACHE_CONTENT = False

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


## PLUGIN CONFIGURATION ##
MARKUP = ('md', 'ipynb')

## PLUGIN CONFIGURATION ##################################
PLUGIN_PATHS = ['./plugins']
from pelican_jupyter import markup as nb_markup
PLUGINS = [nb_markup, 'stardate', 'render_math']
# if you create jupyter files in the content dir, snapshots are saved with the same
# metadata. These need to be ignored. 
IGNORE_FILES = ['.ipynb_checkpoints', '.git', '.html']  
MATH_JAX = {'align':'left','indent':'2em'}
ARTICLE_EXCLUDES = ['extra'] 

PANDOC_ARGS = [
    "--mathjax",
]

#     "--citeproc",

PANDOC_EXTENSIONS = [
    "+abbreviations",
    "+backtick_code_blocks",
    "+emoji"
    ]



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
