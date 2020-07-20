#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Igshaan Mesias'
SITENAME = '@imesias'
SITEURL = ''

THEME = 'themes/svbhack'
OUTPUT_PATH = 'output'
USER_LOGO_URL = SITEURL + '/images/avatar.png'
PATH = 'content'

TIMEZONE = 'Africa/Johannesburg'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

TAGLINE = 'Herder of large chunks of metal that turn electrical signals to binary. Maker of bugs, producer of noise.'
# Blogroll
LINKS = (('Fedora', 'https://imesias.fedorapeople.org'),
         ('Projects', 'https://github.com/imesias'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/imesias'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True