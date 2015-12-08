from model_column import *
from model_table import *
from model_user import *
from peewee import OperationalError

if __name__ == "__main__":
    try:
        AdminUserModel.create_table()
    except OperationalError:
        print "User's table already exists!"

    try:
        AdminTableModel.create_table()
    except OperationalError:
        print "Table's table already exists!"

    try:
        AdminColumnModel.create_table()
    except OperationalError:
        print "Column's table already exists!"
