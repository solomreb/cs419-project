Schemas.txt

-User 'admin' owns only one database: the database of Users/Passwords
-All other users can own zero to many databases, each with multiple tables if desired.


For User 'admin':

Database: 'psql-admin'
	-Used for logging user in, out, veryifying login credentials
	
	-User table
		class User(BaseModel):
	    	username = CharField(max_length=100, unique=True)
	    	password = CharField(max_length=100)


For UserA:

Database: <userA created nameA>

	class Table(BaseModel):
	    user = ForeignKeyField(User)
	    field1 = <user created>
	    field2 = <user created>
	    ...

Database: <userA created nameB >

	class Table(BaseModel):
	    user = ForeignKeyField(User)
	    field1 = <user created>
	    field2 = <user created>
	    ...

