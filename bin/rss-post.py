#!/usr/bin/env python

import Feedbot

rss_map = {
#    "Journal of Personality and Social Psychology": {
#        "schema": "apa",
#        "subreddit": "jpsp",
#        "url": "http://content.apa.org/journals/psp.rss",
#    },
#    "Personality and Social Psychology Bulletin": {
#        "schema": "sage",
#        "subreddit": "pspb",
#        "url": "http://psp.sagepub.com/rss/current.xml",
#    },
#    "Journal of Experimental Social Psychology": {
#        "schema": "sciencedirect",
#        "subreddit": "jesp",
#        "url": "http://rss.sciencedirect.com/publication/science/00221031",
#    },
#    "Social Psychology and Personality Science": {
#        "schema": "sage",
#        "subreddit": "spps",
#        "url": "http://spp.sagepub.com/rss/current.xml",
#    },
#    "Journal of Language and Social Psychology": {
#        "schema": "sage",
#        "subreddit": "jlsp",
#        "url": "http://jls.sagepub.com/rss/current.xml",
#    },
#    "Journal of Personality": {
#        "schema": "wiley",
#        "subreddit": "jp",
#        "url": "http://onlinelibrary.wiley.com/rss/journal/10.1111/(ISSN)1467-6494",
#    },
#    "Journal of Research in Personality": {
#        "schema": "sciencedirect",
#        "subreddit": "jrp",
#        "url": "http://rss.sciencedirect.com/publication/science/00926566",
#    },
#   "Journal of Experimental Psychology": {
#       "schema": "apa",
#       "subreddit": "jep",
#       "url": "http://content.apa.org/journals/xge.rss",
#   },
#    "Psychological Science": {
#        "schema": "sage",
#        "subreddit": "psychscience",
#        "url": "http://pss.sagepub.com/rss/current.xml",
#    },
    "Psychological Bulletin": {
        "schema": "apa",
        "subreddit": "psychbull",
        "url": "http://content.apa.org/journals/bul.rss",
    },
#    "Cyberpsychology, Behavior, and Social Networking": {
#        "schema": "liebert",
#        "subreddit": "cyberbsn",
#        "url": "http://online.liebertpub.com/action/showFeed?ui=0&mi=3zlocj&ai=1q8j&jc=cyber&type=etoc&feed=rss",
#    },
#    "Computers in Human Behavior": {
#        "schema": "sciencedirect",
#        "subreddit": "computersinhumanbehavior",
#        "url": "http://rss.sciencedirect.com/publication/science/07475632",
#    },
#    "Social Cognition": {
#        "schema": "rss",
#        "subreddit": "socialcognition",
#        "url": "http://guilfordjournals.com/action/showFeed?type=etoc&feed=rss&jc=soco",
#    },
#    "International Journal of Human-Computer Interaction": {
#        "schema": "tandf",
#        "subreddit": "",
#        "url": "http://www.tandfonline.com/action/showFeed?ui=0&mi=78dcn5&ai=xy&jc=hihc20&type=etoc&feed=rss",
#    },
#    "Human-Computer Interaction": {
#        "schema": "rss",
#        "subreddit": "",
#        "url": "http://www.tandfonline.com/action/showFeed?ui=0&mi=78dak6&ai=2h5&jc=hhci20&type=etoc&feed=rss",
#    },
#    "Information Systems Frontiers": {
#        "schema": "springer",
#        "subreddit": "",
#        "url": "http://link.springer.com/search.rss?facet-content-type=Article&facet-journal-id=10796&channel-name=Information%20Systems%20Frontiers",
#    },
#    "Journal of Broadcasting & Electronic Media": {
#        "schema": "tandf",
#        "subreddit": "",
#        "url": "http://www.tandfonline.com/action/showFeed?ui=0&mi=78dcn5&ai=2gr&jc=hbem20&type=etoc&feed=rss",
#    },
    "New Media \& Society": {
        "schema": "sage",
        "subreddit": "nms",
        "url": "http://nms.sagepub.com/rss/current.xml",
    },
#    "Communication Theory": {
#        "schema": "wiley",
#        "subreddit": "",
#        "url": "http://onlinelibrary.wiley.com/rss/journal/10.1111/(ISSN)1468-2885",
#    },
#    "Human Communication Research": {
#        "schema": "wiley",
#        "subreddit": "",
#        "url": "http://onlinelibrary.wiley.com/rss/journal/10.1111/(ISSN)1468-2958",
#    },
#    "Journal of Computer-Mediated Communication": {
#        "schema": "wiley",
#        "subreddit": "",
#        "url": "http://onlinelibrary.wiley.com/rss/journal/10.1111/(ISSN)1083-6101",
#    },
    "Sociological Methods \& Research": {
        "schema": "sage",
        "subreddit": "smr",
        "url": "http://smr.sagepub.com/rss/current.xml",
    },
#    "Journal of Information Technology & Politics": {
#        "schema": "rss",
#        "subreddit": "",
#        "url": "http://www.tandfonline.com/action/showFeed?ui=0&mi=78dcn5&ai=1cl&jc=witp20&type=etoc&feed=rss",
#    },
    "Bulletin of Science, Technology, \& Society": {
        "schema": "sage",
        "subreddit": "bsts",
        "url": "http://bst.sagepub.com/rss/current.xml",
    },
#    "Psychology & Marketing": {
#        "schema": "rss",
#        "subreddit": "",
#        "url": "http://onlinelibrary.wiley.com/rss/journal/10.1002/(ISSN)1520-6793",
#    },
#    "Journal of Interactive Advertising": {
#        "schema": "rss",
#        "subreddit": "",
#        "url": "http://www.tandfonline.com/action/showFeed?ui=0&mi=78dcn5&ai=15h5v&jc=ujia20&type=etoc&feed=rss",
#    },
#    "Journal of Management Information Systems": {
#        "schema": "rss",
#        "subreddit": "",
#        "url": "http://rss.ebscohost.com/AlertSyndicationService/Syndication.asmx/GetFeed?guid=3785656",
#    },
#    "": {
#        "schema": "rss",
#        "subreddit": "",
#        "url": "",
#    },
}

def main(rss_map):
    reddit_api = Feedbot.login()
    for title, feed in rss_map.items():
        Feedbot.submit_feed(title, feed, reddit_api)

main(rss_map)
