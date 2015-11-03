import datetime
from peewee import CharField, DateTimeField, ForeignKeyField
from model_base import BaseModel
from model_user import UserModel


class DatabaseModel(BaseModel):
    class Meta:
        db_table = 'databases'

    user = ForeignKeyField(UserModel, related_name='databases')
    name = CharField()
    created_date = DateTimeField(default=datetime.datetime.now)
