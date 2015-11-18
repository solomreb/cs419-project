import datetime
from peewee import CharField, DateTimeField
from model_base import PostgresqlModel, AdminModel


class TableModel(PostgresqlModel):
    class Meta:
        db_table = 'tables'

    user = CharField()
    name = CharField()
    created_date = DateTimeField(default=datetime.datetime.now)

class AdminTableModel(AdminModel):
    class Meta:
        db_table = 'tables'

    name = CharField()
    created_date = DateTimeField(default=datetime.datetime.now)