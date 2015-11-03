from peewee import Model, SqliteDatabase

database = SqliteDatabase("cs419.db")


def before_request_handler():
    database.connect()


def after_request_handler():
    database.close()


class BaseModel(Model):
    class Meta:
        database = database
