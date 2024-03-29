from peewee import IntegrityError
from model_base import *
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT, AsIs


def connect_to_db(db_name, username):
    conn = psycopg2.connect(dbname=db_name, user=username)
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    return conn


def add_database(username, database_name):

    # connect to default postgres db to start creating new db
    conn = connect_to_db('postgres', 'postgres')
    cursor = conn.cursor()

    # check for duplicate database name
    find_query = "SELECT 1 FROM pg_database WHERE datname = (%s);"
    data = (database_name,)
    cursor.execute(find_query, data)

    if cursor.rowcount > 0:
        #print 'Database already exists.'
        return False

    else:
        #create database
        create_query = 'CREATE DATABASE %s' % (database_name)
        cursor.execute(create_query)

        #change owner to user
        change_owner = "ALTER DATABASE %s OWNER TO %s"
        data = (AsIs(database_name), AsIs(username))
        cursor.execute(change_owner, data)
        conn.close()

        #initialize psql_db
        psql_db.init(database_name, user=username)
    return True

def display_databases(username):
    # connect to default postgres db to search dbs
    conn = connect_to_db('postgres', 'postgres')
    cursor = conn.cursor()

    # check for duplicate database name
    find_query = "SELECT datname FROM pg_catalog.pg_database d WHERE pg_catalog.pg_get_userbyid(d.datdba) = %s;"

    cursor.execute(find_query, (username,))
    result = cursor.fetchall()
    return result