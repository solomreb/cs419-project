from peewee import IntegrityError
from model_database import DatabaseModel
import psycopg2
import psycopg2.extensions

def connect_default_db():

    conn = psycopg2.connect(dbname='postgres', user='postgres')
    conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    return conn

def add_database(user, database_name):

    conn = connect_default_db()
    cursor = conn.cursor()

    """
    find_query = "SELECT 1 FROM pg_database WHERE datname = \'%s\'" % (database_name)
    result = cursor.execute(find_query)
    if result.rowcount > 0:
        print 'Database already exists.'
        return False
    else:
    """
    create_query = "CREATE DATABASE " + database_name
    cursor.execute(create_query)
    conn.commit()
    conn.close()
    return True
