#!/usr/bin/env python

import requests

username = "ian"
password = "ian"
UP = {'user': username, 'passwd': password, 'api_type': 'json'}
url_prefix = "https://ssl.lexitrax.com/api"

def do_auth_function(username, password):

def submit_link(sr, title, url, uh):
	new_link = {
		"sr": sr,
		"r": sr,
		"uh": modhash,
		"kind": "link",
		"title": title,
		"url": url,
		'api_type': 'json'
		}
	r = client.post(url_prefix + '/submit', data=new_link, verify=False)
	return r

# Login
with requests.session() as client:
	r = client.post(url_prefix + '/login', data=UP, verify=False)
	if r.ok:
		modhash = r.json()['json']['data']['modhash']
		print modhash
		r = submit_link(sr="lazypost", title="lazy2", url="http://lexitrax.com/6", uh=modhash)
		print r.status_code
		print r.text
		print r.json()

	else:
		print "NOT OK"
