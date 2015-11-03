import curses
import dashboard_program
from utility_database import add_database


def database_menu(user):
    """
    Once a user is logged in, they are shown this screen
    It displays the options for them to do in regards to databases.
    create a new database or edit/view existing databases (or exit)
    :param username:
    :return:
    """
    screen = curses.initscr()
    screen.clear()
    screen.keypad(1)

    selection = -1
    option = 0

    while selection < 0:
        choices = [0] * 3
        choices[option] = curses.A_REVERSE
        screen.addstr(5, 5, 'WELCOME! WHAT WOULD YOU LIKE TO DO?', curses.A_BOLD | curses.A_UNDERLINE)
        screen.addstr(8, 5, 'Create New Database', choices[0])
        screen.addstr(11, 5, 'Edit/View Existing Database', choices[1])
        screen.addstr(14, 5, 'Exit', choices[2])

        screen.refresh()
        action = screen.getch()

        if action == curses.KEY_UP:
            option = (option - 1) % 3
        elif action == curses.KEY_DOWN:
            option = (option + 1) % 3
        elif action == ord('\n'):
            selection = option

        if selection == 0:
            new_database_view(user)
        elif selection == 1:
            edit_database(user)
        elif selection == 2:
            dashboard_program.end_program()


def new_database_view(user):
    """
    User is taken here if they would like to create a new database
    It is passed the username, so that the database can be associated
    with the particular user
    THIS STILL NEEDS TO BE WRITTEN
    User will be taken from here to a screen that displays the screens
    to create a database
    :param user:
    :return:
    """
    screen = curses.initscr()
    screen.clear()
    screen.addstr(5, 5, 'Enter Database Name:')

    curses.echo()
    database_name = screen.getstr(6, 5, 15)

    database = add_database(user, database_name)

    edit_selected_database_menu(database)


def edit_selected_database_menu(database):
    screen = curses.initscr()
    screen.clear()
    screen.keypad(1)

    selection = -1
    option = 0

    while selection < 0:
        choices = [0] * 2
        choices[option] = curses.A_REVERSE
        screen.addstr(5, 5, 'What would you like to do in this database?', curses.A_BOLD | curses.A_UNDERLINE)
        screen.addstr(8, 5, 'Edit/View an Existing Table', choices[0])
        screen.addstr(11, 5, 'Create a New Table', choices[1])

        screen.refresh()

        action = screen.getch()

        if action == curses.KEY_UP:
            option = (option - 1) % 2
        elif action == curses.KEY_DOWN:
            option = (option + 1) % 2
        elif action == ord('\n'):
            selection = option

        if selection == 0:
            edit_table_view_selected_database(database)
        elif selection == 1:
            create_new_table(database)


def edit_table_view_selected_database(database):
    """
    This is a poorly named function
    User is brought here if they selected that they wanted to edit an existing database
    It pulls all the tables that are in that database and that are associated the
    username
    User then selected a table from that list
    This table, the username, and database is sent to tableOptions.py tableOptions()
    :param username:
    :param selected_database:
    :return:
    """
    screen = curses.initscr()
    screen.clear()
    screen.keypad(1)

    """
    Here we query all the tables associated with this user and this database
    And put all the names as elements of 'tables' variable (instead of the hardcoded testing elements)
    Also, query the count of tables and save that as 'tables_count'
    """
    tables = ['name1', 'name2', 'name3', 'name4']
    tables_count = 4
    selection = -1
    option = 0

    screen.addstr(3, 5, 'Choose a table to edit/view', curses.A_BOLD | curses.A_UNDERLINE)

    selected_table = None

    while selection < 0:
        y = 5
        i = 0
        choices = [0] * tables_count
        choices[option] = curses.A_REVERSE

        for name in tables:
            screen.addstr(y, 5, name, choices[i])
            i += 1
            y += 3

        screen.refresh()

        action = screen.getch()

        if action == curses.KEY_UP:
            option = (option - 1) % tables_count
        elif action == curses.KEY_DOWN:
            option = (option + 1) % tables_count
        elif action == ord('\n'):
            selection = option

        selected_table = tables[selection]

    table_dashboard(username, selected_database, selected_table)


def edit_database(user):
    """
    User is taken here if they would like to edit an existing database
    All of the databases that are associated with the user's username
    Are displayed, and the user can scroll through the pick the database
    they would like to edit
    The database that they select is sent to edit_selected_database_menu()
    the username and database name are sent
    :param user:
    :return:
    """
    screen = curses.initscr()
    screen.clear()
    screen.keypad(1)

    screen.addstr(3, 5, 'Choose a database to edit/view', curses.A_BOLD | curses.A_UNDERLINE)

    """
    Here we query all the databases associated with this user
    And put all the names as elements of 'databases' variable
    Also, query the count of databases and save that as 'databases_count'
    """
    databases = ['name1', 'name2', 'name3', 'name4']
    databases_count = 4
    selection = -1
    option = 0

    selected_database = None

    while selection < 0:
        y = 5
        i = 0
        choices = [0] * databases_count
        choices[option] = curses.A_REVERSE

        # LINE 37 BELOW KEEPS THROWING ERROR
        for name in databases:
            screen.addstr(y, 5, name, choices[i])
            i += 1
            y += 3

        screen.refresh()

        action = screen.getch()

        if action == curses.KEY_UP:
            option = (option - 1) % 5
        elif action == curses.KEY_DOWN:
            option = (option + 1) % 5
        elif action == ord('\n'):
            selection = option

        selected_database = databases[selection]

    edit_selected_database_menu(database)


def create_new_table(username, selected_database):
    screen = curses.initscr()
    screen.clear()
    screen.keypad(1)

    screen.addstr(5, 5, 'Enter Table Name:')
    curses.echo()
    table_name = screen.getstr(6, 5, 15)

    """
    HERE RUN THE CREATE TABLE COMMAND FOR DATABASE WITH THE FOLLOWING TABLE NAME:
    table_name
    """

    create_columns(username, selected_database, table_name)


def create_columns(username, selected_database, table):
    screen = curses.initscr()
    screen.clear()
    screen.keypad(1)

    curses.echo()
    screen.addstr(5, 5, 'Enter Field Name:')
    screen.addstr(8, 5, 'Enter Type (provide the necessary lengths and decimals):')
    field_name = screen.getstr(6, 5, 15)
    field_type = screen.getstr(9, 5, 15)

    screen.addstr(11, 5, 'Is this a primary key? Enter Y or N: ')
    field_primary_key = screen.getch()

    screen.addstr(14, 5, 'Can this value be NULL? Enter Y or N: ')
    field_null = screen.getch()

    if field_primary_key == ord('y') and field_null == ord('y'):
        field_option = 'PRIMARY KEY'

    if field_primary_key == ord('y') and field_null == ord('n'):
        field_option = 'PRIMARY KEY, NOT NULL'

    if field_primary_key == ord('n') and field_null == ord('n'):
        field_option = 'NOT NULL'

    if field_primary_key == ord('n') and field_null == ord('y'):
        field_option = ''

    # for testing
    # screen.addstr(15, 5, field_option)
    # screen.refresh()

    """
    HERE RUN THE ALTER TABLE COMMAND FOR THE DATABASE, WITH THE FOLLOWING FIELDS:
    field_name, field_type, field_option
    """

    screen.addstr(17, 5, 'Do you have more columns to add? Enter Y or N: ')
    response = screen.getch()

    if response == ord('y'):
        create_columns(username, selected_database, table)
    if response == ord('n'):
        table_menu(username, selected_database, table)