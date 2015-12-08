#!/usr/bin/env python


class TableField:
    def __init__(self):
        self.field_name = ""
        self.field_type = None
        self.not_null = False
        self.primary_key = False
        self.unique = False
        self.none = True


class Table:
    def __init__(self):
        self.table_name = ""
        self.table_fields = []
        self.number_of_fields = 0
        self.fields_edited = 0
