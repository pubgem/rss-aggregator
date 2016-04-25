#!/usr/bin/env python
# -*- coding: utf-8 -*-
# rss-aggregator (c) pubgem

from rss_aggregator.wsgi import app
app.run(port=app.config['PORT'])
