import json
import socket
import praw
import csv
from datetime import datetime, timedelta
import time

with open("config.json", "r") as jsonfile:
    # reading the config file
    data = json.load(jsonfile) 
    print("Config data read successful",data)

# creating csv file to store comments data 
filename = 'reddit_comments.csv'
columns = ['author', 'id', 'submission', 'body', 'subreddit', 'created_utc', 'collected_utc']
with open(filename, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(columns)

reddit = praw.Reddit(
        client_id = data["client_id"],
        client_secret = data["client_secret"],
        user_agent="COM3021 Reddit Listener")

# record start time
start_time = datetime.now()

# stream comments and save data
stream = reddit.subreddit("AskUK+AskAnAmerican").stream
for comments in stream.comments(skip_existing=True):
    # check if its been 4 hours 
    if datetime.now() - start_time > timedelta(hours=4):
        break
    # extract data from each comment
    comment_data = [
        comments.author.name if comments.author else 'Deleted', # author
        comments.id, # id
        comments.submission.id, # submission
        comments.body.replace('\n', ''), # body
        comments.subreddit.display_name, # subreddit
        datetime.fromtimestamp(comments.created_utc).isoformat(), # created utc
        datetime.now().isoformat() # collected utc
    ]

    # write comment data to csv
    with open(filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(comment_data)

