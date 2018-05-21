import db;
import sqlalchemy.exc
from psycopg2.extras import Json

__DB__ = None 

def store_tweet(tweet):
	db = __connection__();
	row = __prepare_twitter_row__(tweet)
	db.insert('likes', row)


def __prepare_twitter_row__(tweet):
	insert = {
		'id': tweet['id'],
		'source': 'twitter',
		'created_at': tweet['created_at'],
		'inserted_at': 'now()',
		'data': Json(tweet)
	}

	return insert

def __connection__():
	global __DB__
	if not __DB__:
		__DB__ = db.Db('postgres://localhost/likes')

	return __DB__