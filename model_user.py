import datetime
from peewee import CharField, DateTimeField
from model_base import BaseModel


class UserModel(BaseModel):
    class Meta:
        db_table = 'users'

    username = CharField(unique=True)
    password = CharField()
    created_date = DateTimeField(default=datetime.datetime.now)
