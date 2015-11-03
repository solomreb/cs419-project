import datetime
from peewee import CharField, DateTimeField, ForeignKeyField
from model_base import BaseModel
from model_database import DatabaseModel


class TableModel(BaseModel):
    class Meta:
        db_table = 'tables'

    database = ForeignKeyField(DatabaseModel, related_name='tables')
    name = CharField()
    created_date = DateTimeField(default=datetime.datetime.now)
