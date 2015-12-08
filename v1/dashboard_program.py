import curses
import dashboard_user


def main_menu():
    """
    This is the first thing that is displayed to the user
    The options that the user can choose are in regards to logging in
    They are: existing user, new user, and end_program
    :return:
    """
    screen = curses.initscr()
    screen.keypad(1)
    screen.clear()
    selection = -1
    option = 0

    while selection < 0:
        choices = [0] * 3
        choices[option] = curses.A_REVERSE
        screen.addstr(5, 5, 'DATABASE VIEWER', curses.A_BOLD | curses.A_UNDERLINE)
        screen.addstr(8, 5, 'Existing User', choices[0])
        screen.addstr(11, 5, 'New User', choices[1])
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
            dashboard_user.existing_user_view()
        elif selection == 1:
            dashboard_user.new_user_view()
        elif selection == 2:
            end_program()


def end_program():
    """
    If user chooses to exit the program, this is called, and it closes the program
    And returns user to the terminal
    :return:
    """
    curses.endwin()
