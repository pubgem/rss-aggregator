import feedparser, sys, praw

def login():
    user_agent = ("lexitrax feedbot 1.0 by /u/ian 127.0.0.1")
    r = praw.Reddit(site_name="lexitrax", user_agent=user_agent, log_requests=1)
    r.config._ssl_url = None
    r.login()
    return r

def shorten_authors(authors, delim=";"):
    authors_list = authors.split(delim)
    lastnames = list()
    for name in authors_list:
        lastnames.append(name.split(",")[0])
    author_str = ", ".join(lastnames[0:3])
    if len(lastnames) > 3:
        author_str += "..."
    else:
        author_str += "."
    return author_str

def parse_apa(feed, entry):
    author_str = shorten_authors(entry["author"], delim="; ")
    url_str = "http://dx.doi.org/" + entry["dc_identifier"]
    title_str = author_str + " " + entry["title"]
    if len(title_str) > 300:
        title_str = title_str[0:296] + "..."
    return {"title": title_str, "url": url_str}

def parse_sage(feed, entry):
    author_str = shorten_authors(entry["author"], delim="., ")
    url_str = "http://dx.doi.org/10.1177/" + entry["dc_identifier"].split(";")[1]
    title_str = author_str + " " + entry["title"]
    if len(title_str) > 300:
        title_str = title_str[0:296] + "..."
    return {"title": title_str, "url": url_str}

def submit_feed(title, feed, reddit_api):
    subreddit = feed["subreddit"]
    d = feedparser.parse(feed["url"])
    print d['feed']['title']

    for entry in d.entries:
        if feed["schema"] == "apa":
            parsed = parse_apa(feed, entry)
        elif feed["schema"] == "sage":
            parsed = parse_sage(feed, entry)
        else:
            parsed = { "url": entry["link"], "title": entry["title"] }

        print parsed

        try:
            reddit_api.submit(subreddit=subreddit, url=parsed["url"], title=parsed["title"])
        except praw.errors.AlreadySubmitted:
            print "already submitted..."
        except AttributeError:
            print "submitted successfully; no comments yet"
