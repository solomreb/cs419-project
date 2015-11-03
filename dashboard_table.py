import curses
import dashboard_database


def table_menu(username, database, table):
    """
    User is sent here once they select a table to view/edit
    This displays the options they can do with the table they have selected:
    View / Edit Structure / Insert / Drop
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
        screen.addstr(11, 5, 'Edit Structure', choices[1])
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
            edit_table(username, database, table)
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
    dashboard_database.edit_selected_database_menu(username, database, table_name)


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
    screen.addstr(6, 5, "THIS NEEDS TO BE DONE", curses.A_BOLD)
    screen.refresh()


def insert_table(username, database, table):
    """
    :param username:
    :param database:
    :param table:
    :return:
    """
    screen = curses.initscr()
    screen.clear()
    screen.addstr(6, 5, "THIS NEEDS TO BE DONE", curses.A_BOLD)
    screen.refresh()


def edit_table(username, database, table):
    """
    :param username:
    :param database:
    :param table:
    :return:
    """
    screen = curses.initscr()
    screen.clear()
    screen.addstr(6, 5, "THIS NEEDS TO BE DONE", curses.A_BOLD)
    screen.refresh()
