import curses
import curses.textpad

screen = curses.initscr()
screen.keypad(1)

def get_input(prompt):
	screen.clear()
	screen.border(0)
	screen.addstr(2, 2, prompt)
	screen.refresh()
	input = screen.getstr(10, 10, 60)
	return input

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
	win = curses.newwin(1, 6, 6, 5)
	win.box()
	#win.addstr(8,5, 'Table Name', choices[0])
	win.refresh()
		

menu()