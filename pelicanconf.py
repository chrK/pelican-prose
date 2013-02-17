#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Basic Site Information
AUTHOR = u'Your Name'
SITENAME = u'Your Site Name'
SITEURL = 'http://example.com'

# Localization
TIMEZONE = 'Europe/Berlin'
DEFAULT_LANG = u'de'
LOCALE = ('de_DE', )
DEFAULT_DATE_FORMAT = '%-d. %B %Y'
DEFAULT_DATE = (2012, 3, 2, 14, 1, 1)

DEFAULT_PAGINATION = False

THEME = 'pelican-prose'
STATIC_PATHS = ["images", "audio", ]
MARKUP = ('markdown', 'md', )
MD_EXTENSIONS = ['footnotes', ]

REVERSE_CATEGORY_ORDER = True

ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}/index.html'
