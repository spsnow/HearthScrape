import time
import praw
import re
import mechanize
import cookielib

# Setting up reddit script
r = praw.Reddit(user_agent='Hearthstone Subreddit Key Scraper')
keyRE = re.compile('\d{25}')
already_done = []

# Searching for keys
while True:
    subreddit = r.get_subreddit('hearthstone')
    for submission in subreddit.get_new(limit=20):
        if submission.id not in already_done:
            print 'Parsing new post: ' + submission.short_link
            key = keyRE.findall(submission.selftext.lower())
            for s in key:
                print 'FOUND A KEY: ' + s
            already_done.append(submission.id)
    time.sleep(10)

