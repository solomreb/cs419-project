import curses
from dashboard import dashboard

screen = curses.initscr()
screen.keypad(1)

#User is directed here if they choose that they are an existing user
#In this function, user enters a password and user name
#And these are validated through calls to the database.
#If they are acceptable, they enter the database viewer, if they are not,
#They are returned to the main menu
def existingUser():
	screen.clear()

	screen.addstr(5,5, 'Enter Username:')
	screen.addstr(8,5, 'Enter Password:')

	curses.echo()
	username = screen.getstr(6,5,15)
	curses.noecho()
	password = screen.getstr(9,5,15)

	"""
	
	The code for checking the entered username and password
	against those stored in the database goes here. If it matches, send 
	them to the database option menu (uncomment line below), otherwise, send them back to the 
	main screen

	"""
	dashboard(username)

	#DELETE THIS NEXT LINE, ONCE CODE ABOVE IS WRITTEN TO DIRECT THEM FROM THIS PAGE:
	#curses.endwin()

#User is directed here if they selected that they are a new user to this system
#Here, they enter a username and password
#Those are stored in the database
#User is then redirected back to the main login page to login as an existing user
def newUser():
	screen.clear()

	screen.addstr(5,5, 'Enter Username:')
	screen.addstr(8,5, 'Enter Password:')

	curses.echo()
	username = screen.getstr(6,5,15)
	curses.noecho()
	password = screen.getstr(9,5,15)

	"""
	
	The code for storing the entered username and password
	into the database goes here. 

	"""

	menu()

#If user chooses to exit the program, this is called, and it closes the program
#And returns user to the terminal
def exit():
	curses.endwin()

#This is the first thing that is displayed to the user
#The options that the user can choose are in regards to logging in
#The are: existing user, new user, and exit
def menu():
	screen.clear()
	selection = -1
	option = 0
	while selection < 0:
		choices = [0]*3
		choices[option] = curses.A_REVERSE
		screen.addstr(5,5, 'DATABASE VIEWER', curses.A_BOLD|curses.A_UNDERLINE)
		screen.addstr(8,5, 'Existing User', choices[0])
		screen.addstr(11,5, 'New User', choices[1])
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
			existingUser()
		elif selection == 1:
			newUser()
		elif selection == 2:
			exit()

menu()