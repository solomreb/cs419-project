import curses
from tablesOptions import tablesOptions

"""
THIS PAGE JUST NEEDS THE DATABASE FUNCTIONALITY
"""

def createColumns(username, selected_database, table):
	screen = curses.initscr()
	screen.clear()
	screen.keypad(1)

	curses.echo()
	screen.addstr(5,5, 'Enter Field Name:')
	screen.addstr(8,5, 'Enter Type (provide the necessary lengths and decimals):')
	fieldName = screen.getstr(6,5,15)
	fieldType = screen.getstr(9,5,15)

	screen.addstr(11,5, 'Is this a primary key? Enter Y or N: ')
	fieldPK = screen.getch()

	screen.addstr(14,5, 'Can this value be NULL? Enter Y or N: ')
	fieldNULL = screen.getch()

	if fieldPK == ord('y') and fieldNULL == ord('y'):
		fieldOptions = 'PRIMARY KEY'
	if fieldPK == ord('y') and fieldNULL == ord('n'):
		fieldOptions = 'PRIMARY KEY, NOT NULL'
	if fieldPK == ord('n') and fieldNULL == ord('n'):
		fieldOptions = 'NOT NULL'
	if fieldPK == ord('n') and fieldNULL == ord('y'):
		fieldOptions=''

	#for testing
	#screen.addstr(15,5, fieldOptions)
	#screen.refresh()

	"""
	HERE RUN THE ALTER TABLE COMMAND FOR THE DATABASE, WITH THE FOLLOWING FIELDS:
	fieldName, fieldType, fieldOptions
	"""

	screen.addstr(17,5, 'Do you have more columns to add? Enter Y or N: ')
	response = screen.getch()

	if response == ord('y'):
		createColumns(username, selected_database, table)
	if response == ord('n'):
		tablesOptions(username, selected_database, table)




def createNewTable(username, selected_database):
	screen = curses.initscr()
	screen.clear()
	screen.keypad(1)

	screen.addstr(5,5, 'Enter Table Name:')
	curses.echo()
	tableName = screen.getstr(6,5,15)

	"""
	HERE RUN THE CREATE TABLE COMMAND FOR DATABASE WITH THE FOLLOWING TABLE NAME:
	tableName
	"""

	createColumns(username, selected_database, tableName)