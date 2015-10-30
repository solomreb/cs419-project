import curses
from tablesOptions import tablesOptions

def editSelectedDatabase(username, selected_database):
	screen = curses.initscr()
	screen.clear()
	screen.keypad(1)

	"""
	Here we query all the tables associated with this user and this database
	And put all the names as elements of 'tables' variable (instead of the hardcoded testing elements)
	Also, query the count of tables and save that as 'tables_count'
	"""
	tables = ['name1','name2','name3','name4']
	tables_count = 4
	selection = -1
	option = 0

	screen.addstr(3, 5, 'Choose a table to edit/view',curses.A_BOLD|curses.A_UNDERLINE)


	while selection < 0:
		y = 5 
		i = 0
		choices = [0] * tables_count
		choices[option] = curses.A_REVERSE
		
		#LINE 35 BELOW KEEPS THROWING ERROR 
		for name in tables:
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
		
		selected_table = tables[selection]


	tablesOptions(username, selected_database, selected_table)





