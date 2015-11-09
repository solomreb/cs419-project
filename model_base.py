from peewee import Model, PostgresqlDatabase

database = PostgresqlDatabase('cs419', user='vagrant')


def before_request_handler():
    database.connect()


def after_request_handler():
    database.close()


class BaseModel(Model):
    class Meta:
        database = database
