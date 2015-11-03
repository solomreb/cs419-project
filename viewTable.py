import curses

def viewTable(username, database, table):
	screen = curses.initscr()
	screen.clear()
	
	screen.addstr(6,5, "THIS NEEDS TO BE DONE", curses.A_BOLD)

	screen.refresh()