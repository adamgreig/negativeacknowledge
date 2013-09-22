#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Adam Greig'
SITENAME = u'Negative Acknowledge'
SITEURL = 'http://negativeacknowledge.com'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

FILENAME_METADATA = r'(?P<date>\d{4}-\d{2}-\d{2})_(?P<slug>.*)'

THEME = 'themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'slate'
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

DEFAULT_PAGINATION = 10

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'
DAY_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/index.html'

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# Blogroll
LINKS = (('adamgreig.com', 'https://adamgreig.com'),
         ('CU Spaceflight', 'http://cusf.co.uk'),
         ('UK High Altitude Society', 'http://ukhas.org.uk'),
         )

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/adamgreig'),
          ('github', 'https://github.com/adamgreig'),
          ('flickr', 'http://www.flickr.com/photos/randomskk'),
          )

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
