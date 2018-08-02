import sqlite3
import json
from typing import Dict
from datetime import datetime

__DB__ = None 

def store_tweet(tweet):
	db = __connection__();
	row = __prepare_twitter_row(tweet)
	sql = __insert_sql('likes', row)
	db.execute(sql, row)
	db.commit()

def __prepare_twitter_row(tweet):
	insert = {
		'id': tweet['id'],
		'source': 'twitter',
		'created_at': __tweet_date_to_iso(tweet['created_at']),
		'inserted_at': None,   # "DATETIME('NOW')",
		'tweet': tweet.get('full_text') if tweet.get('full_text') else tweet.get('text'),

		'author': '; '.join((tweet['user']['name'], tweet['user']['screen_name'])),
		'data': json.dumps(tweet)
	}

	if tweet['entities']['urls']:
		insert['urls'] = ' '.join(url['expanded_url'] for url in tweet['entities']['urls'])

	return insert

def __tweet_date_to_iso(date_str):
	return datetime.strptime(date_str, '%a %b %d %X %z %Y').isoformat()

def __insert_sql(table_name, params: Dict):
	# data = params['data']
	# del(params['data'])

	keys = list(params)
	field_sql = ', '.join(keys)

	values = []
	for key in keys:
		if key in ['inserted_at']:
			values.append("DATETIME('NOW')")
		else:
			values.append(":{}".format(key))

	values_sql = ','.join(values)

	sql = "INSERT OR IGNORE into {} ({}) VALUES ({})".format(table_name, field_sql, values_sql)
	#print(sql)
	return sql

def __connection__():
	global __DB__
	if not __DB__:
		__DB__ = conn = sqlite3.connect('likes.db')

	return __DB__