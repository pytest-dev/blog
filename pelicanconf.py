#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Pytest authors'
SITENAME = u'pytest blog'
SITEURL = ''

EMAIL = 'pytest-dev@python.org'

PATH = 'content'
STATIC_PATHS = ('extra/favicon.ico',)
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

TIMEZONE = 'Europe/Stockholm'

DEFAULT_LANG = u'en'
SITEMAP = {'format': 'xml'}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = 'theme'

DEFAULT_PAGINATION = False
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['assets', 'sitemap']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


RESOURCE_LINKS = [
    ('http://pytest.org/latest/', 'Documentation'),
]
