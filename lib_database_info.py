#!/usr/bin/env python


class DatabaseInfo:
    def __init__(self):
        self.host = "localhost"
        self.port = 5432
        self.username = ""
        self.password = ""
        self.database = ""
        self.connection = None
