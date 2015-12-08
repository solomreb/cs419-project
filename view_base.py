#!/usr/bin/env python

import urwid
from lib_translator import Translator
from database_postgresql import PostgreSQL


class BaseView(object):
    def __init__(self, database_info):
        self.database_info = database_info
        self.t = Translator()
        self.db = PostgreSQL()
        self.v_padding = 1
        self.h_padding = 5
        self.frame = None
        self.body = None
