#!/usr/bin/env python

import tweepy
import re
import datetime

def get_api():
    return tweepy.API()

def get_tweets(num = 20):
    api = get_api()
    return api.user_timeline('sismoguc')

def parse_tweet(tweet):
    m = re.match("Hora UTC: (?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+) (?P<hour>\d+):(?P<minute>\d+):(?P<second>\d+).(?P<decimal>\d+) mag: (?P<mag>\.+), Lat: (?P<lat>\.+), Lon: (?P<lng>\.+), Loc: (?P<loc>\.+)", tweet.text)
    data = {
        'time': datetime.datetime(
            int(m.group('year')),
            int(m.group('month')),
            int(m.group('day')),
            int(m.group('hour')),
            int(m.group('minute')),
            int(m.group('second')),
            None
        ),
        'mag': m.group('mag'),
        'lat': m.group('lat'),
        'lng': m.group('lng'),
        'loc': m.group('loc'),
    }
    return data

if __name__ == "__main__":
    tweets = get_tweets()
    print parse_tweet(tweets[0])
