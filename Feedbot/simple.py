#!/usr/bin/env python

import sys, praw
user_agent = ("lexitrax Feedbot 1.0 by /u/ian 127.0.0.1")
r = praw.Reddit(site_name="lexitrax", user_agent=user_agent, log_requests=1)
r.config._ssl_url = None

r.login()

resp = r.submit(subreddit="lazypost", url="http://lexitrax.com/10", title="simple")
#print resp
