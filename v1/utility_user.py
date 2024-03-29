from peewee import IntegrityError
from model_user import AdminUserModel
from utility_database import connect_to_db
from psycopg2.extensions import AsIs

def validate_user(username, password):
    """
    :param username:
    :param password:
    :return:
    """
    try:
        user = AdminUserModel.get(AdminUserModel.username == username)

    except AdminUserModel.DoesNotExist:
        return None

    if user.password == password:
        return user

    return None


def add_user(user, password):
    """
    :param username:
    :param password:
    :return:
    """
    try:
        #add user to admin user table
        #AdminUserModel.create(username=user, password=password)

        # add user to psql
        conn = connect_to_db('postgres', 'postgres')
        cursor = conn.cursor()
        add_query = "CREATE ROLE %s WITH CREATEDB LOGIN PASSWORD %s"
        add_data = (AsIs(user), password)
        cursor.execute(add_query, add_data)

    except IntegrityError:
        return False

    return True


def display_users():
    for user in AdminUserModel.select():
        print user.username, user.password
