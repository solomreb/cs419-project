import curses

def newDatabase():
	"""
	Here we put a function call to a different file
	that will have all the fields needed for making a new database
	"""
	#DELETE THE LINE BELOW ONCE THE ABOVE CODE IS WRITTEN AND USER IS CORRECTLY REDIRECTED
	curses.endwin()

def editDatabase():

	"""
	Here we query all the databases associated with this user 
	And put all the names as options to edit
	When a user selects the database, redirect them to a different file
	for editing
	"""

	#DELETE THE LINE BELOW ONCE THE ABOVE CODE IS WRITTEN AND USER IS CORRECTLY REDIRECTED
	curses.endwin()

def exit():
	curses.endwin()

def dashboard():
	screen = curses.initscr()
	screen.keypad(1)

	selection = -1
	option = 0
	while selection < 0:
		choices = [0]*3
		choices[option] = curses.A_REVERSE
		screen.addstr(5,5, 'WELCOME! WHAT WOULD YOU LIKE TO DO?', curses.A_BOLD|curses.A_UNDERLINE)
		screen.addstr(8,5, 'Create New Database', choices[0])
		screen.addstr(11,5, 'Edit Existing Database', choices[1])
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
			newDatabase()
		elif selection == 1:
			editDatabase()
		elif selection == 2:
			exit()

