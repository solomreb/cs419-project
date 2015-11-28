from peewee import Model, PostgresqlDatabase

admin_db = PostgresqlDatabase('cs419', user='vagrant')

psql_db = PostgresqlDatabase(None) #To be initialized at runtime


class PostgresqlModel(Model):
    class Meta:
        database = psql_db


class AdminModel(Model):
    class Meta:
        database = admin_db
