from model_column import AdminColumnModel
from model_table import AdminTableModel
from model_user import AdminUserModel
from peewee import PostgresqlDatabase

if __name__ == "__main__":
    database = PostgresqlDatabase('cs419', user='vagrant')

    tables = [
        AdminColumnModel,
        AdminTableModel,
        AdminUserModel
    ]

    database.drop_tables(tables, safe=True, cascade=True)
