from twitter import *
from tweet_store import sqlite3 as tweet_store
from config import *
import sqlalchemy.exc
import time

def debug_cursor(resp):
	if len(resp) > 0:
		print("start {}".format(resp[0]['id']))
	else:
		print("empty response")
		exit()

	if len(resp) > 1:
		print("end {}".format(resp[len(resp)-1]))
	else:
		print("one record, hmmmm?")

def write_file(resp):
	pass

if __name__ == '__main__':
	twitter_api = Twitter(
		auth=OAuth(TWITTER_TOKEN, TWITTER_TOKEN_SECRET, TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET))


	resp = twitter_api.favorites.list(count=200, tweet_mode='extended')

	#foo = resp.headers.get('X-Rate-Limit-Remaining')
	#print(foo)

	debug_cursor(resp)

	while len(resp) > 0:
		for tweet in resp:
			max_id = tweet['id']
			try:
				tweet_store.store_tweet(tweet);
				print('.')
			except sqlalchemy.exc.IntegrityError as err:
				#print(err)
				pass

		print ('sleeping');
	
		time.sleep(10) 
		resp = twitter_api.favorites.list(count=200, max_id=max_id)
		debug_cursor(resp)
