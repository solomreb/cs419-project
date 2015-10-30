import curses
from dashboard import dashboard

screen = curses.initscr()
screen.keypad(1)

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


def exit():
	curses.endwin()


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