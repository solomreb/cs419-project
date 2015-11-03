from model_user import UserModel
from model_database import DatabaseModel
from peewee import IntegrityError

if __name__ == "__main__":
    users = [
        {
            'username': 'allie',
            'password': 'test1',
            'database_name': 'allie db',
            'tables': [

            ]
        },
        {
            'username': 'becky',
            'password': 'test2',
            'database_name': 'becky db',
            'tables': [

            ]
        },
        {
            'username': 'lynda',
            'password': 'test3',
            'database_name': 'lynda db',
            'tables': [

            ]
        },
        {
            'username': 'test',
            'password': 'test',
            'database_name': 'test db',
            'tables': [

            ]
        },
    ]

    for user in users:
        try:
            user_created = UserModel.create(username=user['username'], password=user['password'])
            database = DatabaseModel.create(user=user_created, name=user['database_name'])
        except IntegrityError:
            print "User already exists!"
