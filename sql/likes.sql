CREATE TABLE likes (
	id numeric,
	source varchar(80),
	created_at timestamp,
	inserted_at timestamp,
	updated_at timestamp,
	data jsonb
);

create unique index on likes (id);

-- insert into likes (id, source, created_at, inserted_at, data)
-- values 
-- ('966744545936453632', 'tweet', 'Thu Feb 22 18:40:35 +0000 2018', now())

CREATE TABLE likes (
	id numeric,
	source varchar(80),
	created_at timestamp,
	inserted_at timestamp,
	updated_at timestamp,
	tweet text,
	author text,
	urls text,
	data text
);