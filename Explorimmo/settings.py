#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Scrapy settings for explorimmo project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

from __future__ import unicode_literals

BOT_NAME = 'explorimmo'

SPIDER_MODULES = ['explorimmo.spiders']
NEWSPIDER_MODULE = 'explorimmo.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.15

# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 16
CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'explorimmo.middlewares.BureauxlocauxSpiderMiddleware': 543,
# }

DOWNLOADER_CLIENT_TLS_METHOD="TLSv1.1"

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    #'explorimmo.middlewares_nabil.proxy': 1,
    'neukolln.middlewares.SmartRotateIpAddressMiddleware': 1,
    #'neukolln.middlewares.SmartRotateIpAddressMiddleware': None,
    'neukolln.middlewares.RotateUserAgentAndIpAddressMiddleware': None,  # <==== deactivate
    'neukolln.middlewares.RotateIpAddressMiddleware': None,  # <==== deactivate
    'neukolln.middlewares.RandomUserAgentMiddleware': None,  # <==== deactivate
    #   '$project_name.middlewares.MyCustomDownloaderMiddleware': 543,
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'neukolln.pipelines.CSV_JSON_TAB_Pipeline': 300,
    'explorimmo.pipelines.ExplorimmoPipeline': 400

}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 24 * 3600  # Save file for one full day
HTTPCACHE_DIR = 'FR_EXPLORIMMONEUF'  # ??'httpcache'
HTTPCACHE_IGNORE_HTTP_CODES = [500, 503, 504, 400, 408, 404]  # Do not save 404 page...
HTTPCACHE_STORAGE = 'neukolln.middlewares.CustomFilesystemCacheStorage'  # 'scrapy.extensions.httpcache.FilesystemCacheStorage'
HTTPCACHE_IGNORE_MISSING = False  # If enabled, requests not found in the cache will be ignored instead of downloaded.

# ??This policy has no awareness of any HTTP Cache-Control directives.
# Every request and its corresponding response are cached.
# When the same request is seen again, the response is returned without transferring anything from the Internet.
# ??The Dummy policy is useful for testing spiders faster
# (without having to wait for downloads every time) and for trying your spider offline,
# when an Internet connection is not available.
# The goal is to be able to ???replay??? a spider run exactly as it ran before.
# https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#dummy-policy-default
HTTPCACHE_POLICY = 'neukolln.middlewares.CustomPolicy'

LOG_STDOUT = True
### Patch - Build a custom logs folder to store all log files with timestamp
# https://github.com/scrapy/scrapy/blob/master/scrapy/utils/log.py
import time, os

path = "logs"
if not os.path.exists(path):
    os.makedirs(path)
now = time.strftime("%Y%m%d_%Hh-%Mmin-%Ss")
LOG_FILE = "%s/%s_%s.log" % (path, 'explorimmo', now)
###
LOG_ENABLED = True
LOG_LEVEL = 'DEBUG'

# Set job directory to pause/stop and resume crawls
# ??http://scrapy.readthedocs.io/en/latest/topics/jobs.html#job-directory
#??JOBDIR = 'jobs'

# Downloader middlewares
# Maximum number of times to retry, in addition to the first download.
RETRY_TIMES = 2  # Default: 2
RETRY_HTTP_CODES = [500, 503, 504, 400, 408, 404]  # Default: [500, 503, 504, 400, 408]
# Reminder:
# 400 Bad Request
# 401 Unauthorized
# 402 Payment Required
# 403 Forbidden
# 404 Not Found
# 405 Method Not Allowed
# 406 Not Acceptable
# 407 Proxy Authentication Required
# 408 Request Timeout
# 409 Conflict
# 410 Gone
# 411 Length Required
# 412 Precondition Failed
# 413 Request Entity Too Large
# 414 Request-URI Too Long
# 415 Unsupported Media Type
# 416 Requested Range Not Satisfiable
# 417 Expectation Failed
# 500 Internal Server Error
# 501 Not Implemented
# 502 Bad Gateway
# 503 Service Unavailable
# 504 Gateway Timeout
# 505 HTTP Version Not Supported

# https://doc.scrapy.org/en/latest/topics/feed-exports.html#feed-export-fields
# Use FEED_EXPORT_FIELDS option to define fields to export and their ORDER!!
FEED_EXPORT_FIELDS = [
    'ANNONCE_LINK',
    'FROM_SITE',
    'ID_CLIENT',
    'ANNONCE_DATE',
    'ACHAT_LOC',
    'SOLD',
    'MAISON_APT',
    'CATEGORIE',
    'NEUF_IND',
    'NOM',
    'ADRESSE',
    'CP',
    'VILLE',
    'QUARTIER',
    'DEPARTEMENT',
    'REGION',
    'PROVINCE',
    'ANNONCE_TEXT',
    'ETAGE',
    'NB_ETAGE',
    'LATITUDE',
    'LONGITUDE',
    'M2_TOTALE',
    'SURFACE_TERRAIN',
    'NB_GARAGE',
    'PHOTO',
    'PIECE',
    'PRIX',
    'PRIX_M2',
    'URL_PROMO',
    'STOCK_NEUF',
    'PAYS_AD',
    'PRO_IND',
    'SELLER_TYPE',
    'MINI_SITE_URL',
    'MINI_SITE_ID',
    'AGENCE_NOM',
    'AGENCE_ADRESSE',
    'AGENCE_CP',
    'AGENCE_VILLE',
    'AGENCE_DEPARTEMENT',
    'EMAIL',
    'WEBSITE',
    'AGENCE_TEL',
    'AGENCE_TEL_2',
    'AGENCE_TEL_3',
    'AGENCE_TEL_4',
    'AGENCE_FAX',
    'AGENCE_CONTACT',
    'PAYS_DEALER',

    'NEUKOLLN_FROM_LISTING_PAGE',

    'NEUKOLLN_ORIGINAL_PHONE_AGENCE_TEL',
    'NEUKOLLN_DEFAULT_CC_AGENCE_TEL',

    'NEUKOLLN_ORIGINAL_PHONE_AGENCE_FAX',
    'NEUKOLLN_DEFAULT_CC_AGENCE_FAX',
]


