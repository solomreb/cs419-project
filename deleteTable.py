import curses
from dashboard import dashboard

def deleteTable(username, tableName):
	"""ENTER database query here to delete the table 
	stored under 'tableName', associated with 'username'
	"""

	#Return User to DatabaseDashboard Screen ??????
	return

def dont_deleteTable(username, tableName):
	#Return User to DatabaseDashboard Screen ??????
	return


def deleteTableMenu(username, tableName):
	#FOR TESTING:
	tableName = 'table1'

	screen = curses.initscr()
	screen.clear()
	screen.keypad(1)

	selection = -1
	option = 0
	while selection < 0:
		choices = [0]*2
		choices[option] = curses.A_REVERSE
		screen.addstr(5,5, 'Are you sure you want to delete this table?', curses.A_BOLD|curses.A_UNDERLINE)
		screen.addstr(8,5, tableName, curses.A_BOLD)
		screen.addstr(11,5, 'Yes', choices[0])
		screen.addstr(14,5, 'No', choices[1])

		screen.refresh()
		
		action = screen.getch()
		
		if action == curses.KEY_UP:
			option = (option -1) % 5
		elif action == curses.KEY_DOWN:
			option = (option +1) % 5
		elif action == ord('\n'):
			selection = option
		
		if selection == 0:
			deleteTable(username, tableName)
		elif selection == 1:
			dont_deleteTable(username, tableName)

deleteTableMenu('allie', 'table')
