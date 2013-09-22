#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Adam Greig'
SITENAME = u'Negative Acknowledge'
SITEURL = 'http://negativeacknowledge.com'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

FILENAME_METADATA = r'(?P<date>\d{4}-\d{2}-\d{2})_(?P<slug>.*)'

TYPOGRIFY = True

THEME = 'themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'slate'
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'

ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{slug}'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{slug}/index.html'

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

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
