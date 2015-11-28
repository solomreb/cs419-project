import datetime
from peewee import CharField, DateTimeField, ForeignKeyField
from model_base import PostgresqlModel, AdminModel
from model_user import UserModel, AdminUserModel


class DatabaseModel(PostgresqlModel):
    class Meta:
        db_table = 'databases'

    user = ForeignKeyField(UserModel, related_name='databases')
    name = CharField()
    created_date = DateTimeField(default=datetime.datetime.now)


class AdminDatabaseModel(AdminModel):
    class Meta:
        db_table = 'databases'

    user = ForeignKeyField(AdminUserModel, related_name='databases')
    name = CharField()
    created_date = DateTimeField(default=datetime.datetime.now)
