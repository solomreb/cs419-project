import curses
from databaseDashScreen import editSelectedDatabase

"""
THIS PAGE JUST NEEDS THE DATABASE FUNCTIONALITY
"""

#User is taken here if they would like to create a new database
#It is passed the username, so that the database can be associated
#with the particular user
#THIS STILL NEEDS TO BE WRITTEN
#User will be taken from here to a screen that displays the screens
#to create a database
def newDatabase(username):
	
	screen = curses.initscr()

	screen.clear()
	screen.addstr(5,5, 'Enter Database Name:')

	curses.echo()
	newDatabaseName = screen.getstr(6,5,15)

	"""
	Here we enter the new database name into the database
	and ensure that it is tied to the user
	"""

	editSelectedDatabase(username, newDatabaseName)	

#User is taken here if they would like to edit an existing database
#All of the databases that are associated with the user's username
#Are displayed, and the user can scroll through the pick the database
#they would like to edit
#The database that they select is sent to databaseDashScreen.py editSelectedDatabase()
#the username and database name are sent
def editDatabase(username):
	screen = curses.initscr()
	screen.clear()
	screen.keypad(1)

	screen.addstr(3, 5, 'Choose a database to edit/view',curses.A_BOLD|curses.A_UNDERLINE)

	"""
	Here we query all the databases associated with this user 
	And put all the names as elements of 'databases' variable
	Also, query the count of databases and save that as 'databases_count'
	"""
	databases = ['name1','name2','name3','name4']
	databases_count = 4
	selection = -1
	option = 0

	while selection < 0:
		y = 5 
		i = 0
		choices = [0] * databases_count
		choices[option] = curses.A_REVERSE
		
		#LINE 37 BELOW KEEPS THROWING ERROR 
		for name in databases:
			screen.addstr(y,5, name, choices[i])
			i = i + 1
			y = y + 3
		
		screen.refresh()

		action = screen.getch()
		
		if action == curses.KEY_UP:
			option = (option -1) % 5
		elif action == curses.KEY_DOWN:
			option = (option +1) % 5
		elif action == ord('\n'):
			selection = option
		
		selected_database = databases[selection]

	editSelectedDatabase(username, selected_database)

#If a user chooses to exit, the program is terminated
def exit():
	curses.endwin()

#Once a user is logged in, they are shown this screen
#It displays the options for them to do in regards to databases:
#create a new database or edit/view existing databases (or exit)
def dashboard(username):
	screen = curses.initscr()
	screen.clear()
	screen.keypad(1)

	selection = -1
	option = 0
	while selection < 0:
		choices = [0]*3
		choices[option] = curses.A_REVERSE
		screen.addstr(5,5, 'WELCOME! WHAT WOULD YOU LIKE TO DO?', curses.A_BOLD|curses.A_UNDERLINE)
		screen.addstr(8,5, 'Create New Database', choices[0])
		screen.addstr(11,5, 'Edit/View Existing Database', choices[1])
		screen.addstr(14,5, 'Exit', choices[2])

		screen.refresh()
		
		action = screen.getch()
		
		if action == curses.KEY_UP:
			option = (option -1) % 3
		elif action == curses.KEY_DOWN:
			option = (option +1) % 3
		elif action == ord('\n'):
			selection = option
		
		if selection == 0:
			newDatabase(username)
		elif selection == 1:
			editDatabase(username)
		elif selection == 2:
			exit()


