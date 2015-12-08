import datetime
from peewee import CharField, DateTimeField, ForeignKeyField
from model_base import *
from model_table import *


class ColumnModel(PostgresqlModel):
    class Meta:
        db_table = 'columns'

    table = ForeignKeyField(TableModel, related_name='columns')
    name = CharField()
    created_date = DateTimeField(default=datetime.datetime.now)


class AdminColumnModel(AdminModel):
    class Meta:
        db_table = 'columns'

    table = ForeignKeyField(AdminTableModel, related_name='columns')
    name = CharField()
    created_date = DateTimeField(default=datetime.datetime.now)
