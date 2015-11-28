import datetime
from peewee import CharField, DateTimeField
from model_base import AdminModel, PostgresqlModel


class UserModel(PostgresqlModel):
    class Meta:
        db_table = 'users'

    username = CharField(unique=True)
    password = CharField()
    created_date = DateTimeField(default=datetime.datetime.now)


class AdminUserModel(AdminModel):
    class Meta:
        db_table = 'users'

    username = CharField(unique=True)
    password = CharField()
    created_date = DateTimeField(default=datetime.datetime.now)
