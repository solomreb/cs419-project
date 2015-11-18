from model_column import ColumnModel
from model_table import TableModel
from model_user import UserModel
from peewee import PostgresqlDatabase

if __name__ == "__main__":
    database = PostgresqlDatabase('cs419', user='vagrant')

    tables = [
        ColumnModel,
        TableModel,
        UserModel
    ]

    database.drop_tables(tables, safe=True, cascade=True)
