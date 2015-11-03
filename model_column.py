import datetime
from peewee import CharField, DateTimeField, ForeignKeyField
from model_base import BaseModel
from model_table import TableModel


class ColumnModel(BaseModel):
    class Meta:
        db_table = 'columns'

    table = ForeignKeyField(TableModel, related_name='columns')
    name = CharField()
    created_date = DateTimeField(default=datetime.datetime.now)
