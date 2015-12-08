#!/usr/bin/env python

import urwid
import urwid.curses_display
from lib_database_info import DatabaseInfo
from view_login import LoginView


def main():
    db_info = DatabaseInfo()
    login_view = LoginView(db_info).create()

    '''
    Foreground Colors:
        'black'
        'dark red'
        'dark green'
        'brown'
        'dark blue'
        'dark magenta'
        'dark cyan'
        'light gray'
        'dark gray'
        'light red'
        'light green'
        'yellow'
        'light blue'
        'light magenta'
        'light cyan'
        'white'

    Background Colors:
        'black'
        'dark red'
        'dark green'
        'brown'
        'dark blue'
        'dark magenta'
        'dark cyan'
        'light gray'
    '''

    palette = [
        ('header', 'black', 'dark green'),
        ('footer', 'light gray', 'dark red'),
        ('topbar', 'light gray', 'dark blue'),
        ('table_listing', 'black', 'dark cyan'),
        ('body_topbar', 'black', 'dark cyan'),
        ('body_topaction', 'white', 'dark magenta'),
        ('body', 'black', 'light gray'),
        ('a_hover', 'black', 'dark cyan'),
        ('a_text', 'white', 'dark magenta'),
        ('b_hover', 'black', 'dark cyan'),
        ('b_text', 'light gray', 'dark blue'),
        ('m_hover', 'light gray', 'black'),
        ('m_text', 'black', 'light gray'),
        ('selected', 'light gray', 'dark red'),
        ('error', 'dark red', 'light gray'),
        ('error_bg', 'light gray', 'dark red')
    ]

    def show_or_exit(key):
        if key in ('q', 'Q'):
            raise urwid.ExitMainLoop()

    urwid_screen = urwid.curses_display.Screen()

    loop = urwid.MainLoop(login_view, palette, unhandled_input=show_or_exit, screen=urwid_screen)
    loop.run()


if __name__ == '__main__':
    main()
