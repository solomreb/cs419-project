import curses
from databaseDashScreen import editSelectedDatabase

def newDatabase(username):
	"""
	Here we put a function call to a different file
	that will have all the fields needed for making a new database
	"""
	#DELETE THE LINE BELOW ONCE THE ABOVE CODE IS WRITTEN AND USER IS CORRECTLY REDIRECTED
	curses.endwin()

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

def exit():
	curses.endwin()

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
			option = (option -1) % 5
		elif action == curses.KEY_DOWN:
			option = (option +1) % 5
		elif action == ord('\n'):
			selection = option
		
		if selection == 0:
			newDatabase(username)
		elif selection == 1:
			editDatabase(username)
		elif selection == 2:
			exit()


