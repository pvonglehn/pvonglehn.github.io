#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Patrick von Glehn'
SITENAME = 'Patrick von Glehn'
SITEURL = 'http://localhost:8000'

PATH = 'content'

TIMEZONE = 'Europe/Madrid'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('github', 'https://github.com/pvonglehn'),
          ('linkedin', 'https://linkedin.com/in/patrickvonglehn'),
          ('stack-overflow', 'https://stackoverflow.com/users/10716823/patrick-von-glehn'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
MARKUP = ("md", "ipynb")

from pelican_jupyter import markup as nb_markup
PLUGINS = [nb_markup]
STATIC_PATHS = ['img', 'static', 'pdf','siteImages']
IGNORE_FILES = [".ipynb_checkpoints"]
THEME = "themes/Flex"
SITELOGO  = 'https://avatars1.githubusercontent.com/u/42738386?s=460&u=c9aa8b78019cbd51a097484639149f307bf7e108&v=4'
#SITELOGO = SITEURL + "/images/profile.png"
USE_FOLDER_AS_CATEGORY = False
SITENAME = "Patrick von Glehn"
SITETITLE = SITENAME
SITESUBTITLE = 'A Blog'
#SITEURL = "https://pvonglehn.github.io"
SITEDESCRIPTION = "My Blog"
MAIN_MENU = True

MENUITEMS = (('Archives', '/archives.html'),
            ('About','/pages/about.html'),
            ('CV','/pdf/Patrick_von_Glehn_CV_LinkedIn.pdf')
             )
