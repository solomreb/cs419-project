from peewee import Model, PostgresqlDatabase

psql_db = PostgresqlDatabase('cs419', user='vagrant')


def before_request_handler():
    database.connect()


def after_request_handler():
    database.close()


class PostgresqlModel(Model):
    class Meta:
        database = psql_db
