from peewee import Model, PostgresqlDatabase

psql_db = PostgresqlDatabase('cs419', user='vagrant')



class PostgresqlModel(Model):
    class Meta:
        database = psql_db
