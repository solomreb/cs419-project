from peewee import *

database = SqliteDatabase("cs419.db")


def before_request_handler():
    database.connect()


def after_request_handler():
    database.close()


class BaseModel(Model):
    class Meta:
        database = database


class User(BaseModel):
    username = CharField(max_length=100, unique=True)
    password = CharField(max_length=100)


if __name__ == "__main__":
    try:
        User.create_table()
    except OperationalError:
        print "User table already exists!"

    users = [
        {
            'username': 'allie',
            'password': 'test1'
        },
        {
            'username': 'becky',
            'password': 'test2'
        },
        {
            'username': 'lynda',
            'password': 'test3'
        },
        {
            'username': 'test',
            'password': 'test'
        },
    ]

    for user in users:
        try:
            User.create(username=user['username'], password=user['password'])
        except IntegrityError:
            print "User already exists!"
