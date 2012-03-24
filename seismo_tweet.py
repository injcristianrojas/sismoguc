#!/usr/bin/env python

import tweepy
import re
import datetime
import json
from isodate import datetime_isoformat

def get_api():
    return tweepy.API()

def get_tweets(num = 20):
    api = get_api()
    return api.user_timeline('sismoguc')

def parse_tweet(tweet):
	stripped = [t.strip() for t in tweet.text.split(',')]
	time_and_mag = stripped[0]
	m = re.match("Hora UTC: (?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+) (?P<hour>\d+):(?P<minute>\d+):(?P<second>\d+).(?P<decimal>\d+) UTC mag: (?P<mag>\d+.\d+)", time_and_mag)
	quake_time = datetime.datetime(
		int(m.group('year')),
		int(m.group('month')),
		int(m.group('day')),
		int(m.group('hour')),
		int(m.group('minute')),
		int(m.group('second')),
		int(m.group('decimal')) * 100000,
	)
	quake_time_iso = datetime_isoformat(quake_time) + 'Z'
	data = {
		'quake_time': quake_time_iso,
		'mag': float(m.group('mag')),
	}
	m = re.match("Lat: (?P<lat>-?\d+.\d+)", stripped[1])
	data['lat'] = float(m.group('lat'))
	m = re.match("Lon: (?P<lng>-?\d+.\d+)", stripped[2])
	data['lng'] = float(m.group('lng'))
	data['location'] = stripped[3][5:]
	data['publication_time'] = datetime_isoformat(tweet.created_at) + 'Z'
	return data

def get_data():
	tweet_list = get_tweets()
	return [parse_tweet(t) for t in tweet_list]

def jsonize_data():
	return json.dumps(get_data())

if __name__ == "__main__":
	tweets = get_tweets()
	j = jsonize_data()
	print j
