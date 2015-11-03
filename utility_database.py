from peewee import IntegrityError
from model_database import DatabaseModel


def add_database(user, database_name):
    """
    :param user:
    :param database_name:
    :return:
    """
    try:
        database = DatabaseModel.create(user=user, name=database_name)
    except IntegrityError:
        return False

    return database
