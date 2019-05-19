#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

SITENAME = "Loïc Pinsard"
BIO_TEXT = "Lead Character TD on Project Borealis"
SITEURL = "https://muream.github.io"

SITE_AUTHOR = "Loïc Pinsard"
TWITTER_USERNAME = "@muream"
INDEX_DESCRIPTION = (
    "Website and blog of Loïc Pinsard, a Character Rigger and video games lover."
)
FOOTER_TEXT = 'Powered by <a href="http://getpelican.com">Pelican</a> and <a href="http://pages.github.com">GitHub&nbsp;Pages</a>.'

# SIDEBAR_LINKS = ['<a href="/about/">About</a>', '<a href="/archive/">Archive</a>']

DEFAULT_LANG = "en"

SIDEBAR_LINKS = [
    '<a href="/extra/resume.pdf">Resume</a>',
    '<a href="/about-me/">About</a>',
    '<a href="/archive/">Archive</a>',
]

# Social widget
SOCIAL_ICONS = [
    ("mailto:muream@gmail.com", "Email (muream@gmail.com)", "fa-envelope"),
    ("http://twitter.com/muream", "Twitter", "fa-twitter"),
    ("http://github.com/muream", "GitHub", "fa-github"),
    ("https://www.linkedin.com/in/loicpinsard/", "LinkedIn", "fa-linkedin"),
]

# Pelican settings
RELATIVE_URLS = True
SITEURL = "http://muream.github.io"
TIMEZONE = "Europe/Paris"
DEFAULT_DATE = "fs"
DEFAULT_DATE_FORMAT = "%B %d, %Y"
DEFAULT_PAGINATION = False
SUMMARY_MAX_LENGTH = 100


# Disable authors, categories, tags, and category pages
DIRECT_TEMPLATES = ["index", "archives"]
CATEGORY_SAVE_AS = ""
TAGS_SAVE_AS = ""
AUTHORS_SAVE_AS = ""
CATEGORIES_SAVE_AS = ""

THEME = "pneumatic"

PATH = "content"

PLUGIN_PATHS = [
    os.path.join(
        os.path.expanduser("~"), "projects", "pelican-addons", "pelican-plugins"
    )
]
PLUGINS = ["neighbors", "assets"]

ICONS_PATH = "images/icons"
STATIC_PATHS = ["images", "extra"]
ARTICLE_EXCLUDES = ["extra"]


ARTICLE_URL = "{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = ARTICLE_URL + "index.html"

PAGE_URL = "{slug}/"
PAGE_SAVE_AS = PAGE_URL + "index.html"

ARCHIVES_SAVE_AS = "archive/index.html"
YEAR_ARCHIVE_SAVE_AS = "{date:%Y}/index.html"
MONTH_ARCHIVE_SAVE_AS = "{date:%Y}/{date:%m}/index.html"

DELETE_OUTPUT_DIRECTORY = True

TYPOGRIFY = True

GOOGLE_FONTS = ["Menlo"]

