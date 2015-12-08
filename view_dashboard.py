#!/usr/bin/env python

import urwid
from lib_paginator import Paginator
from view_base import BaseView
from view_database import DatabaseView
from view_table import TableView


class DashboardView(BaseView):
    def __init__(self, database_info):
        super(DashboardView, self).__init__(database_info)
        self.paginator = Paginator()
        self.body_info = None
        self.table_listing = None
        self.table_name = None
        self.body_container = None
        self.error_box = None
        self.execute_query_text = None

    def create(self, frame, body):
        self.frame = frame
        self.body = body

        dashboard_body = [
            urwid.AttrWrap(urwid.Divider(), "topbar"),
            self.top_bar_widget(),
            urwid.AttrWrap(urwid.Divider(), "topbar"),
            self.main_body_info_widget()
        ]

        dashboard_body = urwid.ListBox(urwid.SimpleListWalker(dashboard_body))
        dashboard_body.set_focus(1)
        dashboard_body = urwid.AttrWrap(dashboard_body, "body")

        self.body.original_widget = dashboard_body

    def top_bar_widget(self):
        host_text = self.t.get_text("host_label")
        port_text = self.t.get_text("port_label")

        top_bar_1 = urwid.Text([
            host_text, self.database_info.host,
            u" / ",
            port_text, str(self.database_info.port)
        ])
        top_bar_1 = urwid.Padding(top_bar_1, left=2)
        top_bar_1 = urwid.AttrWrap(top_bar_1, "topbar")

        database_text = self.t.get_text("database_label")
        database = urwid.Text([database_text, self.database_info.database])
        database = urwid.Padding(database, left=2)
        database = urwid.AttrWrap(database, "topbar")

        display_database_info_text = self.t.get_text("display_database_info")
        display_database_info_size = len(display_database_info_text) + 6
        display_database_info_btn = urwid.Button(display_database_info_text, self.display_database_info_fn)
        display_database_info_btn = urwid.Padding(display_database_info_btn, right=2)
        display_database_info_btn = urwid.AttrWrap(display_database_info_btn, "b_text", "b_hover")

        create_table_text = self.t.get_text("create_table")
        create_table_size = len(create_table_text) + 6
        create_table_btn = urwid.Button(create_table_text, self.table_creation_fn)
        create_table_btn = urwid.Padding(create_table_btn, right=2)
        create_table_btn = urwid.AttrWrap(create_table_btn, "b_text", "b_hover")

        execute_query_text = self.t.get_text("execute_query")
        execute_query_size = len(execute_query_text) + 6
        execute_query_btn = urwid.Button(execute_query_text, self.execute_query_fn)
        execute_query_btn = urwid.Padding(execute_query_btn, right=2)
        execute_query_btn = urwid.AttrWrap(execute_query_btn, "b_text", "b_hover")

        top_bar_2 = urwid.Columns([
            database,
            ("fixed", display_database_info_size, display_database_info_btn),
            ("fixed", create_table_size, create_table_btn),
            ("fixed", execute_query_size, execute_query_btn)
        ])

        top_bar_widget = urwid.Pile([
            top_bar_1,
            top_bar_2
        ])

        return top_bar_widget

    def main_body_info_widget(self):
        self.body_info = self.database_info_widget()
        self.table_listing = self.table_listing_fn()

        columns = [
            urwid.AttrWrap(self.body_info, "body"),
            ("fixed", 17, self.table_listing)
        ]

        return urwid.Columns(columns)

    # handler for the display database info button
    def display_database_info_fn(self, button):
        self.body_info.original_widget = self.database_info_widget()

    def database_info_widget(self):
        return DatabaseView(self.database_info).database_info_widget()

    def table_creation_fn(self, button):
        frame = self.frame
        body = self.body
        body_info = self.body_info
        table_listing = self.table_listing
        table_listing_fn = self.table_listing_fn

        TableView(self.database_info).create_details(frame, body, body_info, table_listing, table_listing_fn)

    def execute_query_fn(self, button):
        query_header = urwid.Text(self.t.get_text("query_header"))
        query_note = urwid.Text(self.t.get_text("query_note"))

        error_text = urwid.Text(self.t.get_text("empty"), align="center")
        self.error_box = urwid.AttrWrap(error_text, "body")

        text_box_edit = urwid.Edit(multiline=True)
        urwid.connect_signal(text_box_edit, "change", self.text_box_edit_fn)
        text_box_edit = urwid.AttrWrap(text_box_edit, "b_text", "b_hover")

        execute_text = self.t.get_text("execute")
        execute_text_size = len(execute_text) + 4
        execute_btn = urwid.Button(execute_text, self.execute_btn_fn)
        execute_btn = urwid.AttrWrap(execute_btn, "m_text", "m_hover")

        execute_query_widget = urwid.WidgetPlaceholder(
            urwid.Pile([
                urwid.Divider(),
                urwid.Padding(query_header, left=5),
                urwid.Divider(),
                urwid.Padding(query_note, left=5),
                urwid.Divider(),
                urwid.Padding(text_box_edit, left=5, right=5),
                urwid.Divider(),
                urwid.Padding(execute_btn, left=5, width=execute_text_size),
                urwid.Divider(),
                urwid.Padding(self.error_box, left=5, right=5)
            ]))

        self.body_info.original_widget = execute_query_widget

    def text_box_edit_fn(self, widget, text):
        self.execute_query_text = text

    def execute_btn_fn(self, button):
        connection = self.database_info.connection
        response = self.db.execute_query(connection, self.execute_query_text)

        if response["success"]:
            self.execute_query_text = ""
            self.body_info.original_widget = self.database_info_widget()
            self.table_listing.original_widget = self.table_listing_fn()
        else:
            error_text = self.t.get_text("query_failed")
            error_text = "{0} {1}".format(error_text, response["data"])
            error_text = urwid.Text(error_text, align="center")
            error_text = urwid.AttrWrap(error_text, "error_bg")
            error_text = urwid.Padding(error_text, left=2)

            self.error_box.original_widget = error_text

    def table_listing_fn(self):
        table_listing_header_text = self.t.get_text("table_listing_header")
        table_listing_header = urwid.Text(table_listing_header_text, align="center")

        connection = self.database_info.connection
        tables = self.db.get_tables(connection)

        table_buttons_pile = list()

        for table in tables:
            table_button = urwid.Button(table, self.table_btn_fn)
            table_buttons_pile.append(urwid.AttrWrap(table_button, "b_hover", "b_text"))

        table_buttons = urwid.Pile(table_buttons_pile)

        table_list_widget = urwid.Pile([
            urwid.Divider(),
            table_listing_header,
            table_buttons,
            urwid.Divider()
        ])

        table_list_widget = urwid.Padding(table_list_widget, left=1, right=2)

        return urwid.AttrWrap(table_list_widget, "table_listing")

    def table_btn_fn(self, button):
        self.table_name = button.get_label()
        self.paginator.start = 0
        self.paginator.end = self.paginator.page_count

        table_selected_text = self.t.get_text("table_selected")
        table_selected = urwid.Text([table_selected_text, u" ", self.table_name])
        table_selected = urwid.Padding(table_selected, left=2)
        table_selected = urwid.Pile([
            urwid.Divider(),
            table_selected,
            urwid.Divider()
        ])
        table_selected = urwid.AttrWrap(table_selected, "body_topbar")

        structure_text = self.t.get_text("structure")
        structure_text_size = len(structure_text) + 6
        structure_btn = urwid.Button(structure_text, self.structure_btn_fn)
        structure_btn = urwid.Padding(structure_btn, left=2)
        structure_btn = urwid.AttrWrap(structure_btn, "a_text", "a_hover")

        content_text = self.t.get_text("content")
        content_text_size = len(content_text) + 6
        content_btn = urwid.Button(content_text, self.content_btn_fn)
        content_btn = urwid.Padding(content_btn, left=2)
        content_btn = urwid.AttrWrap(content_btn, "a_text", "a_hover")

        drop_text = self.t.get_text("drop")
        drop_text = u"{0} '{1}'".format(drop_text, self.table_name)
        drop_text_size = len(drop_text) + 6
        drop_btn = urwid.Button(drop_text, self.drop_btn_fn)
        drop_btn = urwid.Padding(drop_btn, left=2)
        drop_btn = urwid.AttrWrap(drop_btn, "a_text", "a_hover")

        truncate_text = self.t.get_text("truncate")
        truncate_text = u"{0} '{1}'".format(truncate_text, self.table_name)
        truncate_text_size = len(truncate_text) + 6
        truncate_btn = urwid.Button(truncate_text, self.truncate_btn_fn)
        truncate_btn = urwid.Padding(truncate_btn, left=2)
        truncate_btn = urwid.AttrWrap(truncate_btn, "a_text", "a_hover")

        body_top_action = urwid.Columns([
            ('fixed', structure_text_size, structure_btn),
            ('fixed', content_text_size, content_btn),
            ('fixed', drop_text_size, drop_btn),
            ('fixed', truncate_text_size, truncate_btn)
        ])

        body_top = urwid.Pile([
            urwid.Divider('-'),
            body_top_action,
            urwid.Divider('-')
        ])

        body_top = urwid.AttrWrap(body_top, "body_topaction")

        self.body_container = self.table_structure_widget()
        self.error_box = urwid.AttrWrap(urwid.Text(self.t.get_text("empty")), "body")

        body_info = urwid.Pile([
            table_selected,
            body_top,
            self.body_container,
            urwid.Divider(),
            self.error_box
        ])

        self.body_info.original_widget = body_info

    def structure_btn_fn(self, button):
        self.body_container.original_widget = self.table_structure_widget()

    def table_structure_widget(self):
        connection = self.database_info.connection
        table_info = self.db.get_table_info(connection, self.table_name)

        column_names = list()
        column_types = list()
        type_lengths = list()
        column_nulls = list()

        for row in table_info:
            column_name = row[0]
            column_names.append(urwid.Text(column_name, align="center"))

        for row in table_info:
            column_type = row[1]
            column_types.append(urwid.Text(column_type, align="center"))

        for row in table_info:
            type_length = row[2]

            if type_length:
                type_lengths.append(urwid.Text(str(type_length), align="center"))
            else:
                type_lengths.append(urwid.Text(self.t.get_text("empty")))

        for row in table_info:
            column_null = row[3]

            if column_null:
                column_nulls.append(urwid.Text(column_null, align="center"))
            else:
                column_nulls.append(urwid.Text(self.t.get_text("empty")))

        column_names_widget = urwid.LineBox(urwid.Pile(column_names), title="Name")
        column_types_widget = urwid.LineBox(urwid.Pile(column_types), title="Type")
        type_lengths_widget = urwid.LineBox(urwid.Pile(type_lengths), title="Length")
        column_nulls_widget = urwid.LineBox(urwid.Pile(column_nulls), title="Null")

        table_structure = urwid.Columns([
            column_names_widget,
            column_types_widget,
            type_lengths_widget,
            column_nulls_widget
        ])

        table_structure_widget = urwid.Pile([
            urwid.Divider(),
            table_structure
        ])

        table_structure_widget = urwid.Padding(table_structure_widget, left=2, right=2)

        return urwid.WidgetPlaceholder(table_structure_widget)

    def content_btn_fn(self, button):
        self.display_content()

    def display_content(self):
        connection = self.database_info.connection
        column_names = self.db.get_table_columns(connection, self.table_name)
        table_rows = self.db.fetch_all_rows(connection, self.table_name)
        table_rows_count = len(table_rows)

        if table_rows_count > 0:
            content_header_text = [
                self.t.get_text("viewing_rows"),
                self.t.get_text("empty_space"),
                str(self.paginator.start + 1),
                self.t.get_text("dash"),
                str(self.paginator.end),
                self.t.get_text("of"),
                str(table_rows_count),
                self.t.get_text("empty_space"),
                self.t.get_text("from_table")
            ]

            content_header = urwid.Text(content_header_text)

            table_widget = self.create_table_widget(column_names, table_rows)

            paging_btn_columns = list()

            if self.paginator.start >= self.paginator.page_count:
                previous_btn_text = self.t.get_text("previous")
                previous_btn_size = len(previous_btn_text) + 6
                previous_btn = urwid.Button(previous_btn_text, self.previous_btn_fn)
                previous_btn = urwid.AttrWrap(previous_btn, 'm_text', 'm_hover')
                previous_btn = urwid.Padding(previous_btn, left=2)

                paging_btn_columns.append(('fixed', previous_btn_size, previous_btn))

            if self.paginator.end <= table_rows_count:
                next_btn_text = self.t.get_text("next")
                next_btn_size = len(next_btn_text) + 6
                next_btn = urwid.Button(next_btn_text, self.next_btn_fn)
                next_btn = urwid.AttrWrap(next_btn, 'm_text', 'm_hover')
                next_btn = urwid.Padding(next_btn, left=2)

                paging_btn_columns.append(('fixed', next_btn_size, next_btn))

            content_widget_pile = [
                urwid.Divider(),
                content_header,
                urwid.Divider(),
                table_widget,
                urwid.Divider(),
                urwid.Columns(paging_btn_columns)
            ]
        else:
            content_header_text = [
                str(table_rows_count),
                self.t.get_text("empty_space"),
                self.t.get_text("rows_in_table")
            ]

            content_header = urwid.Text(content_header_text)
            content_header = urwid.AttrWrap(content_header, 'body')
            content_header = urwid.Padding(content_header, left=2)

            content_widget_pile = [
                urwid.Divider(),
                content_header
            ]

        content_widget_pile = urwid.Pile(content_widget_pile)
        content_widget = urwid.Padding(content_widget_pile, left=2, right=2)
        content_widget = urwid.WidgetPlaceholder(content_widget)

        self.body_info.original_widget = content_widget

    def create_table_widget(self, column_names, table_rows):
        linebox_columns = list()
        table_columns = {}

        for column_index, column_name in enumerate(column_names):
            table_columns[column_index] = list()

            column_name = str(column_name).translate(None, '(,)').upper()

            for table_index, table_row in enumerate(table_rows):
                if self.paginator.start <= table_index < self.paginator.end:
                    table_column_text = urwid.Text(str(table_row[column_index]), align="center")
                    table_columns[column_index].append(table_column_text)

            table_column_pile = urwid.Pile(table_columns[column_index])
            table_column_linebox = urwid.LineBox(table_column_pile, title=column_name)
            linebox_columns.append(table_column_linebox)

        return urwid.Columns(linebox_columns)

    def next_btn_fn(self, button):
        self.paginator.start += self.paginator.page_count
        self.paginator.end += self.paginator.page_count
        self.display_content()

    def previous_btn_fn(self, button):
        self.paginator.start -= self.paginator.page_count
        self.paginator.end -= self.paginator.page_count
        self.display_content()

    def drop_btn_fn(self, button):
        self.warning_fn("drop_warning", self.yes_drop_btn_fn)

    def truncate_btn_fn(self, button):
        self.warning_fn("truncate_warning", self.yes_truncate_btn_fn)

    def warning_fn(self, text, fn):
        warning_text = urwid.Text(self.t.get_text(text))
        warning_text = urwid.Padding(warning_text, left=2)
        warning_text = urwid.AttrWrap(warning_text, "body")

        yes_text_size, yes_btn = self.yes_btn_widget(fn, "m_text", "m_hover")
        no_text_size, no_btn = self.no_btn_widget(self.structure_btn_fn, "m_text", "m_hover")

        action_buttons = urwid.Columns([
            ('fixed', yes_text_size, yes_btn),
            ('fixed', no_text_size, no_btn)
        ])

        body_container = urwid.Pile([
            urwid.Divider(),
            warning_text,
            urwid.Divider(),
            action_buttons
        ])

        self.body_container.original_widget = body_container

    def yes_drop_btn_fn(self, button):
        query = "DROP TABLE {0};".format(self.table_name)
        self.yes_action_btn_fn(query)

    def yes_truncate_btn_fn(self, button):
        query = "TRUNCATE TABLE {0};".format(self.table_name)
        self.yes_action_btn_fn(query)

    def yes_action_btn_fn(self, query):
        connection = self.database_info.connection
        response = self.db.execute_query(connection, query)

        if response["success"]:
            self.table_name = None
            self.body_info.original_widget = DatabaseView(self.database_info).database_info_widget()
            self.table_listing.original_widget = self.table_listing_fn()
        else:
            error_text = self.t.get_text("query_failed")
            error_text = "{0} {1}".format(error_text, response["data"])
            error_text = urwid.Text(error_text, align="center")
            error_text = urwid.AttrWrap(error_text, "error_bg")
            error_text = urwid.Padding(error_text, left=2)

            self.error_box.original_widget = error_text

    def yes_btn_widget(self, fn, attr, focus_attr):
        yes_text = self.t.get_text("yes")
        yes_text_size = len(yes_text) + 8
        yes_btn = urwid.Button(yes_text, fn)
        yes_btn = urwid.Padding(yes_btn, left=2, right=2)
        return yes_text_size, urwid.AttrWrap(yes_btn, attr, focus_attr)

    def no_btn_widget(self, fn, attr, focus_attr):
        no_text = self.t.get_text("no")
        no_text_size = len(no_text) + 8
        no_btn = urwid.Button(no_text, fn)
        no_btn = urwid.Padding(no_btn, left=2, right=2)
        return no_text_size, urwid.AttrWrap(no_btn, attr, focus_attr)
