from peewee import IntegrityError
from model_user import UserModel


def validate_user(username, password):
    """
    :param username:
    :param password:
    :return:
    """
    try:
        user = UserModel.get(UserModel.username == username)
    except UserModel.DoesNotExist:
        return None

    if user.password == password:
        return user

    return None


def add_user(username, password):
    """
    :param username:
    :param password:
    :return:
    """
    try:
        UserModel.create(username=username, password=password)
    except IntegrityError:
        return False

    return True


def display_users():
    for user in UserModel.select():
        print user.username, user.password
