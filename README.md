# tweet-faves-py

download your twitter likes (nee favorites) and stick them into a sqlite db

## setup config

`cp config.py.SAMPLE config.py`

add your twitter api key and token info to config.py

## initialize sqlite database

`sqlite3 likes.db < sql/likes.sql`

## run it

python twitter-faves.py

## bonus

datasette likes.db see also [datasette](https://github.com/simonw/datasette)
