from model_user import UserModel
from model_database import DatabaseModel
from peewee import OperationalError

if __name__ == "__main__":
    try:
        UserModel.create_table()
    except OperationalError:
        print "User table already exists!"

    try:
        DatabaseModel.create_table()
    except OperationalError:
        print "Database table already exists!"
