from model_column import ColumnModel
from model_database import DatabaseModel
from model_table import TableModel
from model_user import UserModel
from peewee import OperationalError

if __name__ == "__main__":
    try:
        UserModel.create_table()
    except OperationalError:
        print "User's table already exists!"

    try:
        DatabaseModel.create_table()
    except OperationalError:
        print "Database's table already exists!"

    try:
        TableModel.create_table()
    except OperationalError:
        print "Table's table already exists!"

    try:
        ColumnModel.create_table()
    except OperationalError:
        print "Column's table already exists!"
