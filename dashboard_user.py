import curses
import dashboard_program
import dashboard_database
from utility_user import add_user, validate_user
import time

def existing_user_view():
    """
    User is directed here if they choose that they are an existing user
    In this function, user enters a password and user name
    And these are validated through calls to the database.
    If they are acceptable, they enter the database viewer, if they are not,
    They are returned to the main menu
    :return:
    """
    screen = curses.initscr()
    screen.clear()

    screen.addstr(5, 5, 'Enter Username:')
    screen.addstr(8, 5, 'Enter Password:')

    curses.echo()
    username = screen.getstr(6, 5, 15)
    curses.noecho()
    password = screen.getstr(9, 5, 15)

    """
    The code for checking the entered username and password against
    those stored in the database goes here. If it matches, send them
    to the database option menu (uncomment line below), otherwise,
    send them back to the main screen
    """

    user = validate_user(username, password)

    if user is not None:
        screen.addstr(11, 5, 'Logging you in...')
        screen.refresh()
        time.sleep(2)
        dashboard_database.database_menu(user)
    else:
        screen.addstr(11, 5, 'Invalid username/password. Try again...')
        screen.refresh()
        time.sleep(2)
        dashboard_program.main_menu()


def new_user_view():
    """
    User is directed here if they selected that they are a new user to this system
    Here, they enter a username and password
    Those are stored in the database
    User is then redirected back to the main login page to login as an existing user
    :return:
    """
    screen = curses.initscr()
    screen.clear()

    screen.addstr(5, 5, 'Enter Username:')
    screen.addstr(8, 5, 'Enter Password:')

    curses.echo()
    username = screen.getstr(6, 5, 15)
    curses.noecho()
    password = screen.getstr(9, 5, 15)

    user_added = add_user(username, password)

    if user_added is True:
        screen.addstr(11, 5, username + ' account created...')
        screen.refresh()
        time.sleep(2)
        dashboard_database.database_menu()
    else:
        # print "User already exists"
        screen.addstr(11, 5, 'Username ' + username + ' already exists...')
        screen.refresh()
        time.sleep(2)
        dashboard_program.main_menu()
