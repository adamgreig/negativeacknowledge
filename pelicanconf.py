#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Site Metadata
AUTHOR = u'Adam Greig'
SITENAME = u'Negative Acknowledge'
SITEURL = 'http://negativeacknowledge.com'
TIMEZONE = 'Europe/London'
DEFAULT_LANG = u'en'

# Path Settings
PATH = 'content/'
FILENAME_METADATA = r'(?P<date>\d{4}-\d{2}-\d{2})_(?P<slug>.*)'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'
DAY_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/index.html'
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
STATIC_PATHS = ['images', 'extra/favicon.ico']
EXTRA_PATH_METADATA = {'extra/favicon.ico': {'path': 'favicon.ico'}}

# Content settings
USE_FOLDER_AS_CATEGORY = False
DEFAULT_CATEGORY = 'Uncategorised'
ARTICLE_EXCLUDES = ['pages', '.ipynb_checkpoints']

# Appearance Settings
THEME = 'themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'journal'
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
DEFAULT_PAGINATION = 10

# Plugins
MARKUP = ('md', 'ipynb')
PLUGIN_PATHS = ['plugins/']
PLUGINS = ['ipythonnb']

# Development settings, overriden by deployconf.py
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
RELATIVE_URLS = True


# Web links
LINKS = (('adamgreig.com', 'https://adamgreig.com'),
         ('randomskk.net', 'https://randomskk.net'),
         ('M0RND.net', 'http://m0rnd.net'),
         )

# Social links
SOCIAL = (('twitter', 'https://twitter.com/adamgreig'),
          ('github', 'https://github.com/adamgreig'),
          ('flickr', 'http://www.flickr.com/photos/randomskk'),
          )
