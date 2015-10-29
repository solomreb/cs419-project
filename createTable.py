import curses

screen = curses.initscr()
screen.keypad(1)

def initCurses(title):
	screen.clear()
	screen.keypad(1)
	#curses.cbreak()


	#Top Title Bar
	screen.addstr("DATABASE VIEWER", curses.A_BOLD)
	screen.addstr(0, curses.COLS - len(title), title, curses.A_BOLD)


	#Bottom Info Bar
	screen.addstr(curses.LINES-1, 0, "Use up and down arrow keys to navigate. 'Enter' to select. 'Q' to quit")

	#Window title
	
	#Create window
	window = curses.newwin(curses.LINES-2, curses.COLS, 1, 0)

	return window

def choice1():
	win = initCurses("Choice 1")

def choice2():
	win = initCurses("Choice 2")

def exit():
	#Restore the terminal settings
	curses.nocbreak()
	curses.echo()

	curses.endwin()

def menu():

#	win = initCurses("CREATE TABLE")

	screen.refresh()
	selection = -1
	option = 0
	while selection < 0:
		choices = [0]*3
		choices[option] = curses.A_REVERSE

		screen.addstr(8,5, 'Choice 1', choices[0])
		screen.addstr(11,5, 'Choice 2', choices[1])
		screen.addstr(14,5, 'Exit', choices[2])
		
		screen.refresh()

		action = screen.getch()
		
		if action == curses.KEY_UP:
			option = (option -1) % 4
		elif action == curses.KEY_DOWN:
			option = (option +1) % 4
		elif action == ord('\n'):
			selection = option
		elif action == ord('q') or action == ord('Q'):
			exit()
		
		if selection == 0:
			choice1()
		elif selection == 1:
			choice2()
		elif selection == 2:
			exit()

menu()