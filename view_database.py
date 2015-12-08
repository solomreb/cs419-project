#!/usr/bin/env python

import urwid
from view_base import BaseView


class DatabaseView(BaseView):
    def database_info_widget(self):
        database_info_text = self.t.get_text("database_info")
        database_info = urwid.Text(database_info_text)
        database_info = urwid.AttrWrap(database_info, "body")

        database_tables_text = self.t.get_text("database_tables")
        database_tables = urwid.Text(database_tables_text)
        database_tables = urwid.AttrWrap(database_tables, "body")

        structure_view = urwid.Padding(urwid.Pile([
            urwid.Divider(),
            database_info,
            self.database_stats_widget(),
            urwid.Divider(),
            database_tables,
            self.database_table_info_list_widget()
        ]), left=2, right=2)

        structure_view = urwid.WidgetPlaceholder(structure_view)

        return structure_view

    def database_stats_widget(self):
        connection = self.database_info.connection
        database = self.database_info.database
        database_stats = self.db.get_database_stats(connection, database)

        size = database_stats[0]
        encoding = database_stats[1]
        collation = database_stats[2]

        database_size_text = urwid.Text(size, align="center")
        database_size_col = urwid.LineBox(database_size_text, title="Size")

        database_encoding_text = urwid.Text(encoding, align="center")
        database_encoding_col = urwid.LineBox(database_encoding_text, title="Encoding")

        database_collation_text = urwid.Text(collation, align="center")
        database_collation_col = urwid.LineBox(database_collation_text, title="Collation")

        database_stats_widget = urwid.Columns([
            database_size_col,
            database_encoding_col,
            database_collation_col
        ])

        return database_stats_widget

    def database_table_info_list_widget(self):
        connection = self.database_info.connection
        database_table_info_list = self.db.get_database_table_info_list(connection)

        table_names_list = []
        table_sizes_list = []

        for database_table_info in database_table_info_list:
            table_names_list.append(urwid.Text(database_table_info[0], align="center"))
            table_sizes_list.append(urwid.Text(database_table_info[1], align="center"))

        table_names_col = urwid.LineBox(urwid.Pile(table_names_list), title="Name")
        table_sizes_col = urwid.LineBox(urwid.Pile(table_sizes_list), title="Size")

        database_table_info_list_widget = urwid.Columns([
            table_names_col,
            table_sizes_col
        ])

        return database_table_info_list_widget
