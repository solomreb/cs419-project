import curses
#from databaseDashScreen import editSelectedDatabase
#from tablesOptions import tableOptions

#THIS DOES NOT FULLY WORK YET, BECAUSE OF CIRCULAR DEPENDENCY

#If user selects that they are sure they want to delete the selected table,
#Database query drops the table
#User is then sent back to the page that displays all the tables in the database
def deleteTable(username, database, tableName):
	"""ENTER database query here to delete the table 
	stored under 'tableName', associated with 'username'
	"""
	editSelectedDatabase(username, database, tableName)

#If user selects that they changed their mind to delete the selected table,
#User is sent back to the tables options page
def dont_deleteTable(username, database, tableName):
	tableOptions(username, database, tableName)


#If user has selected that they would like to drop a table
#This screen comes up, and asks if they are sure. The options are 
# Yes or No
def deleteTableMenu(username, database, tableName):
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
			deleteTable(username, database, tableName)
		elif selection == 1:
			dont_deleteTable(username, database, tableName)

