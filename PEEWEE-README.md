# Overview

## Prerequisites (OSX)

* [python](https://www.python.org/downloads/)
* [peewee](http://docs.peewee-orm.com/en/latest/)
* [sqlite](https://www.sqlite.org/)

## Create and seed the database

```bash
$ python seed.py
```

## Connect to the sqlite database

```bash
$ sqlite3 cs419.db
```

### Running queries
```sql
sqlite> select * from user;
```