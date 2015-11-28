import curses
import dashboard_database


def table_menu(username, database, table):
    """
    User is sent here once they select a table to view/edit
    This displays the options they can do with the table they have selected:
    View / Query / Insert / Drop
    THE CORRECT PAGES NEED TO BE IMPORTED TO THIS PAGE
    RIGHT NOW, ONLY DELETETABLE WORKS
    :param username:
    :param database:
    :param table:
    :return:
    """
    screen = curses.initscr()
    screen.clear()
    screen.keypad(1)

    selection = -1
    option = 0
    while selection < 0:
        choices = [0] * 4
        choices[option] = curses.A_REVERSE
        screen.addstr(5, 5, 'What would you like to do with this table?', curses.A_BOLD | curses.A_UNDERLINE)
        screen.addstr(6, 5, table, curses.A_BOLD)
        screen.addstr(8, 5, 'View', choices[0])
        screen.addstr(11, 5, 'Query the Table', choices[1])
        screen.addstr(14, 5, 'Insert', choices[2])
        screen.addstr(17, 5, 'Drop', choices[3])

        screen.refresh()

        action = screen.getch()

        if action == curses.KEY_UP:
            option = (option - 1) % 4
        elif action == curses.KEY_DOWN:
            option = (option + 1) % 4
        elif action == ord('\n'):
            selection = option

        if selection == 0:
            view_table(username, database, table)
        elif selection == 1:
            query_table(username, database, table)
        elif selection == 2:
            insert_table(username, database, table)
        elif selection == 3:
            delete_table_menu(username, database, table)


def delete_table(username, database, table_name):
    """
    If user selects that they are sure they want to delete the selected table,
    Database query drops the table
    User is then sent back to the page that displays all the tables in the database
    ENTER database query here to delete the table
    stored under 'table_name', associated with 'username'
    :param username:
    :param database:
    :param table_name:
    :return:
    """
    dashboard_database.edit_selected_database_menu(None, username)


def dont_delete_table(username, database, table_name):
    """
    If user selects that they changed their mind to delete the selected table,
    User is sent back to the tables options page
    :param username:
    :param database:
    :param table_name:
    :return:
    """
    table_menu(username, database, table_name)


def delete_table_menu(username, database, table_name):
    """
    If user has selected that they would like to drop a table
    This screen comes up, and asks if they are sure. The options are
    Yes or No
    :param username:
    :param database:
    :param table_name:
    :return:
    """
    # FOR TESTING:
    table_name = 'table1'

    screen = curses.initscr()
    screen.clear()
    screen.keypad(1)

    selection = -1
    option = 0
    while selection < 0:
        choices = [0] * 2
        choices[option] = curses.A_REVERSE
        screen.addstr(5, 5, 'Are you sure you want to delete this table?', curses.A_BOLD | curses.A_UNDERLINE)
        screen.addstr(8, 5, table_name, curses.A_BOLD)
        screen.addstr(11, 5, 'Yes', choices[0])
        screen.addstr(14, 5, 'No', choices[1])

        screen.refresh()

        action = screen.getch()

        if action == curses.KEY_UP:
            option = (option - 1) % 2
        elif action == curses.KEY_DOWN:
            option = (option + 1) % 2
        elif action == ord('\n'):
            selection = option

        if selection == 0:
            delete_table(username, database, table_name)
        elif selection == 1:
            dont_delete_table(username, database, table_name)


def view_table(username, database, table):
    """
    :param username:
    :param database:
    :param table:
    :return:
    """
    screen = curses.initscr()
    screen.clear()
    screen.keypad(1)

    """RUN QUERY TO GET COUNT of how many rows are returned for the whole table: RIGHT NOW THIS IS HARD CODED"""
    count = 25

    #view paginated results of table, 7 rows per page
    view_table_pagination(table, 0, 6, count)


def view_table_pagination(table, beg, end, count):

    #Set if there will be a previous button and/or next button
    if beg == 0:
        previous_button = False
    else:
        previous_button = True

    if end >= count - 1:
        next_button = False
    else:
        next_button = True


    #Get a variable called 'safe_end'... is the variable you want to use in the
    #query to ensure that it only calls rows that exist
    safe_end = min(end, count)

    """gather all the rows from the view table query (USE THE QUERY THAT YOU CAN 
        PASS IN STARTING AND ENDING ROW,... we found it while in a meeting one time...
        and use the beg variable as start value, and safe_end as last value)
    """

    # for testing, the results are hardcoded
    rows = [['Bob', '9123 4567', 'home', 'A'], ['Janet', '3453 8828', 'cell', 'B'],
        ['Joe', '1234 0982', 'home', 'A'], ['Kate', '0298 5233', 'cell', 'B'],
        ['Susan', '2345 2340', 'home', 'A'], ['Carrie', '2350 3463', 'cell', 'B'],
        ['Jose', '9123 4567', 'home', 'A']]


    screen = curses.initscr()
    screen.clear()
    screen.keypad(1)

    selection = -1
    option = 0

    while selection < 0:
        choices = [0] * 3
        choices[option] = curses.A_REVERSE
        screen.addstr(1, 5, 'Go back to table menu', choices[0])
        screen.addstr(3, 5, table, curses.A_BOLD | curses.A_UNDERLINE)

        y = 4  # starting y
        x = 2  # starting x

        for row in rows:
            for result in row:
                screen.addstr(y, x, result)
                x += 15
            y += 1  # move to next line
            x = 2  # reset x

        #Display previous and next buttons
        y += 2
        x = 2

        if previous_button:
            screen.addstr(y, x, 'Previous', choices[1])
        if next_button:
            screen.addstr(y+1, x, 'Next', choices[2])

        screen.refresh()

        action = screen.getch()

        if action == curses.KEY_UP:
            option = (option - 1) % 3
        elif action == curses.KEY_DOWN:
            option = (option + 1) % 3
        elif action == ord('\n'):
            selection = option

        if selection == 0:
            #user has selected to return to the menu
            table_menu(username, database, table)
        elif selection == 1:
            #user has selected 'Previous'
            view_table_pagination(table, beg-7, end-7, count)
        elif selection == 2:
            #user has selected 'Next'
            if end < count:
                new_beg = end + 1
            else:
                break
            if (end + 7) < count:
                new_end = end + 7
            else:
                new_end = count

            view_table_pagination(table, new_beg, new_end, count)

def insert_table(username, database, table):
    """
    :param username:
    :param database:
    :param table:
    :return:
    """
    screen = curses.initscr()
    screen.clear()
    screen.addstr(1, 5, "Insert Values For New Row:", curses.A_BOLD | curses.A_UNDERLINE)
    screen.refresh()

    new_row_data = {}  # going to hold the new row data user enters

    """Here we run a query against the table listed in the parameter
    to find all the column names, See TO-DO file for information
    on these database queries"""
    # for testing, this is hard-coded
    columns = ['col1', 'col2', 'col3', 'col4']

    y = 3  # starting x value

    for name in columns:
        screen.addstr(y, 3, name + ":", curses.A_BOLD)
        # Get response
        curses.echo()
        response = screen.getstr(y + 1, 3, 15)
        # Put response in dictionary
        new_row_data[name] = response
        y += 2
    screen.refresh()

    # for testing: passed
    # screen.clear()
    # x=1
    # y=1
    # for key, val in new_row_data.items():
    #    screen.addstr(y,x, key+": ")
    #    screen.addstr(y, x+10, val)
    #    x=1
    #    y+=2

    """Here run the query to enter the key, val, into the table
    specified in the parameter if query is successful, display
    success window, else, display fail
    http://stackoverflow.com/questions/11918797/how-to-check-if-a-mysql-query-was-successful"""

    """Here is what the python will look like once a variable has been set to
        the returned success of the query:
    if (success):
        screen.clear()
        screen.addstr(5,5, "Insert successful")
        screen.addstr(7,5, "Press any button to return to the table menu")
        screen.getch()
        table_menu(username, database,table)
    else:
        screen.clear()
        screen.addstr(5,5, "Insert unsuccessful")
        screen.addstr(7,5, "Press any button to try again")
        screen.getch()
        insert_table(username, database,table)
    """

    screen.refresh()


def query_table(username, database, table):
    """
    :param username:
    :param database:
    :param table:
    :return:
    """

    # Get the query
    screen = curses.initscr()
    screen.clear()
    screen.addstr(5, 5, "Enter your query line:", curses.A_BOLD)
    screen.refresh()

    # IS 50 CHARS LONG ENOUGH FOR A QUERY???????????????????????????????
    query = screen.getstr(6, 5, 50)

    # run the query 
    """RUN THIS QUERY TO THE TABLE"""


    cursor = database.connect()

    """
    cursor.execute(query)
        results = cursor.fetchall()
        """

    # Display results
    screen.clear()
    screen.addstr(1, 1, "Results:", curses.A_BOLD)

    """Here we run a query against the table listed in the parameter
    to find all the column names, See TO-DO file for information
    on these database queries"""
    # for testing, this is hard-coded
    columns = ['col1', 'col2', 'col3', 'col4']

    """Here we run the query that the user entered, stored in the
    variable 'query', and store the results of the query into 'rows'"""
    # run the query
    # for testing, the results are hardcoded
    rows = [['Bob', '9123 4567', 'home', 'A'], ['Janet', '8888 8888', 'cell', 'B']]
    """Get the number of rows returned in the next line"""
    #count = rows.length()
    y = 5  # starting y
    x = 1  # starting x


    """
    for row in table.select().paginate(1, 10):
        print tweet.message
        """

    for row in rows:
        for result in row:
            screen.addstr(y, x, result)
            x += 10
        y += 1  # move to next line
        x = 1  # reset x

    """THIS PAGE JUST NEEDS TO ALLOW PAGINATION"""


    screen.refresh()

def query_table_pagination(columns, rows, beg, end, count):
    #this will be similar to pagination for view Table, except it is with 'rows', so no querying needed

    #screen set up
    screen = curses.initscr()
    screen.clear()
    screen.keypad(1)

    #are next/previous buttons needed?
    if beg == 0:
        previous_button = False
    else:
        previous_button = True

    if end >= count - 1:
        next_button = False
    else:
        next_button = True

    #Get a variable called 'safe_end'... is the variable you want to use in the
    #index to ensure that it only calls rows that exist
    safe_end = min(end, count)

    #print columns (titles)
    x = 1  # starting x value

    for name in columns:
        screen.addstr(3, x, name)
        x += 10

    screen.refresh()

    x=2
    y=4

    #print rows from beg - end
    i = beg
    while i <= safe_end:
        for result in row[i]:
            screen.addstr(y, x, result)
            x += 15
        y += 1  # move to next line
        x = 2  # reset x
        i += 1

    #print previous and next buttons
    selection = -1
    option = 0

    while selection < 0:
        choices = [0] * 2
        choices[option] = curses.A_REVERSE
        if previous_button:
            screen.addstr(13, x, 'Previous', choices[0])
        if next_button:
            screen.addstr(14, x, 'Next', choices[1])

        screen.refresh()

        action = screen.getch()

        if action == curses.KEY_UP:
            option = (option - 1) % 2
        elif action == curses.KEY_DOWN:
            option = (option + 1) % 2
        elif action == ord('\n'):
            selection = option

        if selection == 0:
            #user has selected 'Previous'
            query_table_pagination(columns, rows, beg-7, end-7, count)
        elif selection == 1:
            #user has selected 'Next'
            if end < count:
                new_beg = end + 1
            else:
                break
            if (end + 7) < count:
                new_end = end + 7
            else:
                new_end = count

            query_table_pagination(table, new_beg, new_end, count)


