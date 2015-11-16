import datetime
from peewee import CharField, DateTimeField, ForeignKeyField
from model_base import PostgresqlModel
from model_database import DatabaseModel


class TableModel(PostgresqlModel):
    class Meta:
        db_table = 'tables'

    database = ForeignKeyField(DatabaseModel, related_name='tables')
    name = CharField()
    created_date = DateTimeField(default=datetime.datetime.now)