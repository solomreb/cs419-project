import curses
from deleteTable import deleteTableMenu

#User is sent here once they select a table to view/edit
#This displays the options they can do with the table they have selected:
#View / Edit Structure / Insert / Drop
#THE CORRECT PAGES NEED TO BE IMPORTED TO THIS PAGE
#RIGHT NOW, ONLY DELETETABLE WORKS
def tablesOptions(username, database, table):
	screen = curses.initscr()
	screen.clear()
	screen.keypad(1)

	selection = -1
	option = 0
	while selection < 0:
		choices = [0]*4
		choices[option] = curses.A_REVERSE
		screen.addstr(5,5, 'What would you like to do with this table?', curses.A_BOLD|curses.A_UNDERLINE)
		screen.addstr(6,5, table, curses.A_BOLD)
		screen.addstr(8,5, 'View', choices[0])
		screen.addstr(11,5, 'Edit Structure', choices[1])
		screen.addstr(14,5, 'Insert', choices[2])
		screen.addstr(17,5, 'Drop', choices[3])
		
		screen.refresh()
		
		action = screen.getch()
		
		if action == curses.KEY_UP:
			option = (option -1) % 5
		elif action == curses.KEY_DOWN:
			option = (option +1) % 5
		elif action == ord('\n'):
			selection = option
		
		if selection == 0:
			viewTable(username, database, table)
		elif selection == 1:
			editTable(username, database, table)
		elif selection == 2:
			insertTable(username, database, table)
		elif selection == 3:
			deleteTableMenu(username,database, table)
