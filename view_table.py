#!/usr/bin/env python

import urwid
from lib_table_info import Table, TableField
from view_base import BaseView
from view_database import DatabaseView
import logging

logging.basicConfig(filename="cs419.log", level=logging.DEBUG)


class TableView(BaseView):
    def __init__(self, database_info):
        super(TableView, self).__init__(database_info)
        self.body_info = None
        self.table_listing = None
        self.table_listing_fn = None
        self.table = Table()
        self.table_field = None
        self.table_create_error_text = None
        self.fields_error_text = None
        self.forward_btn = None

    def create_details(self, frame, body, body_info, table_listing, table_listing_fn):
        self.frame = frame
        self.body = body
        self.body_info = body_info
        self.table_listing = table_listing
        self.table_listing_fn = table_listing_fn

        table_create_header_1 = self.t.get_text("table_create_header_1")
        table_create_warning = self.t.get_text("table_create_warning")
        table_create_name_label = self.t.get_text("table_create_name_label")
        table_create_columns_label = self.t.get_text("table_create_columns_label")

        table_create_header_text = urwid.Text(table_create_header_1)
        table_create_warning_text = urwid.Text(table_create_warning)

        self.table_create_error_text = self.empty_text()

        table_create_name_edit = urwid.Edit(table_create_name_label)
        urwid.connect_signal(table_create_name_edit, "change", self.table_name_edit_fn)
        table_create_name_edit = urwid.AttrWrap(table_create_name_edit, "body")

        number_of_fields_edit = urwid.IntEdit(table_create_columns_label)
        urwid.connect_signal(number_of_fields_edit, "change", self.number_of_fields_edit_fn)
        number_of_fields_edit = urwid.AttrWrap(number_of_fields_edit, "body")

        table_create_fields = urwid.Pile([table_create_name_edit, number_of_fields_edit])
        table_create_fields = urwid.Padding(table_create_fields, left=5, width=45)

        table_create_next_text = self.t.get_text("next")
        table_create_next_text_size = len(table_create_next_text) + 4
        table_create_next_btn = urwid.Button(table_create_next_text, self.create_table_next_fn)
        table_create_next_btn = urwid.AttrWrap(table_create_next_btn, "b_hover", "b_text")
        table_create_next_btn = urwid.Padding(table_create_next_btn, left=5, width=table_create_next_text_size)

        create_table_widget = urwid.WidgetPlaceholder(urwid.Padding(
            urwid.Pile([
                urwid.Divider(),
                table_create_header_text,
                urwid.Divider(),
                table_create_fields,
                urwid.Divider(),
                table_create_warning_text,
                urwid.Divider(),
                table_create_next_btn,
                urwid.Divider(),
                self.table_create_error_text
            ]), left=5, right=5))

        self.body_info.original_widget = create_table_widget

    # signal handler for table name edit
    def table_name_edit_fn(self, widget, text):
        self.table.table_name = text.strip()

    # signal handler for number of fields int edit
    def number_of_fields_edit_fn(self, widget, number):
        if number:
            self.table.number_of_fields = int(number)
        else:
            self.table.number_of_fields = 0

        self.table.fields_edited = 0

    # signal handler for the create button
    def create_table_next_fn(self, button):
        table_name = self.table.table_name
        table_fields = self.table.number_of_fields

        logging.debug("table_name: {0}, fields: {1}".format(table_name, table_fields))

        # Validate inputs
        if not table_name:
            error_text = self.t.get_text("table_create_error_1")
            self.table_create_error_text.original_widget = urwid.AttrWrap(urwid.Text(error_text), "error")
        elif table_fields <= 0:
            error_text = self.t.get_text("table_create_error_2")
            self.table_create_error_text.original_widget = urwid.AttrWrap(urwid.Text(error_text), "error")
        elif table_fields > 15:
            error_text = self.t.get_text("table_create_error_3")
            self.table_create_error_text.original_widget = urwid.AttrWrap(urwid.Text(error_text), "error")
        else:
            self.create_table_fields()

    def empty_text(self):
        empty_text = urwid.Text(self.t.get_text("empty"))
        return urwid.AttrWrap(empty_text, "body")

    def create_table_fields(self, button_type=""):
        table_name = self.table.table_name
        number_of_fields = self.table.number_of_fields
        fields_edited = self.table.fields_edited

        fields_header_text = self.t.get_text("table_fields_name_header")
        fields_header = urwid.Text([fields_header_text, table_name])

        fields_number_text = self.t.get_text("table_fields_number_header")
        fields_of_text = self.t.get_text("of")
        fields_text = [fields_number_text, str(fields_edited + 1), fields_of_text, str(number_of_fields)]
        fields_number = urwid.Text(fields_text)

        self.fields_error_text = self.empty_text()

        self.table_field = TableField()

        table_fields_name_label = self.t.get_text("table_fields_name_label")
        table_fields_name_edit = urwid.Edit(table_fields_name_label)
        urwid.connect_signal(table_fields_name_edit, "change", self.fields_edit_fn)
        table_fields_name_edit = urwid.AttrWrap(table_fields_name_edit, "body")

        table_fields_type_label = self.t.get_text("table_fields_type_label")
        table_fields_type_edit = urwid.Edit(table_fields_type_label)
        urwid.connect_signal(table_fields_type_edit, "change", self.fields_edit_fn)
        table_fields_type_edit = urwid.AttrWrap(table_fields_type_edit, "body")

        not_null_text = self.t.get_text("not_null")
        not_null_checkbox = urwid.CheckBox(not_null_text, state=False, on_state_change=self.field_null_change_fn)
        not_null_checkbox = urwid.AttrWrap(not_null_checkbox, "body")

        r_list = []

        primary_key_text = self.t.get_text("primary_key")
        primary_key_radio = urwid.RadioButton(r_list, primary_key_text, False,
                                              on_state_change=self.field_attr_change_fn)
        primary_key_radio = urwid.AttrWrap(primary_key_radio, "body")

        unique_text = self.t.get_text("unique")
        unique_radio = urwid.RadioButton(r_list, unique_text, False, on_state_change=self.field_attr_change_fn)
        unique_radio = urwid.AttrWrap(unique_radio, "body")

        none_text = self.t.get_text("none")
        none_radio = urwid.RadioButton(r_list, none_text, True, on_state_change=self.field_attr_change_fn)
        none_radio = urwid.AttrWrap(none_radio, "body")

        if button_type == "create" or fields_edited == number_of_fields - 1:
            forward_btn_text = self.t.get_text("create")
        elif button_type == "try_again":
            forward_btn_text = self.t.get_text("try_again")
        else:
            forward_btn_text = self.t.get_text("next")

        forward_btn_size = len(forward_btn_text) + 7
        forward_btn = urwid.Button(forward_btn_text, self.table_fields_next_fn)
        forward_btn = urwid.AttrWrap(forward_btn, "b_hover", "b_text")
        forward_btn = urwid.Padding(forward_btn, left=2, width=forward_btn_size)

        self.forward_btn = forward_btn

        table_field_box = urwid.Pile([
            urwid.Divider(),
            table_fields_name_edit,
            urwid.Divider(),
            table_fields_type_edit,
            urwid.Divider(),
            not_null_checkbox,
            urwid.Divider(),
            primary_key_radio,
            unique_radio,
            none_radio,
            urwid.Divider(),
            self.fields_error_text,
            urwid.Divider(),
            self.forward_btn
        ])

        table_fields_widget = urwid.WidgetPlaceholder(urwid.Padding(
            urwid.Pile([
                urwid.Divider(),
                fields_header,
                urwid.Divider(),
                fields_number,
                urwid.Divider(),
                urwid.LineBox(table_field_box),
            ]), left=5, right=5))

        self.body_info.original_widget = table_fields_widget

    # signal handler for edit field events
    def fields_edit_fn(self, widget, text):
        field_name_label = self.t.get_text("table_fields_name_label")
        field_type_label = self.t.get_text("table_fields_type_label")

        if widget.caption == field_name_label:
            self.table_field.field_name = text.strip()
        elif widget.caption == field_type_label:
            self.table_field.field_type = text.strip()

    # signal handler for checkbox
    def field_null_change_fn(self, widget, state):
        if state:
            self.table_field.not_null = True
        else:
            self.table_field.not_null = False

    # signal handler for radio buttons
    def field_attr_change_fn(self, widget, state):
        if state:
            if widget.label == "Primary Key":
                self.table_field.primary_key = True
                self.table_field.unique = False
                self.table_field.none = False
            elif widget.label == "Unique":
                self.table_field.primary_key = False
                self.table_field.unique = True
                self.table_field.none = False
            elif widget.label == "None":
                self.table_field.primary_key = False
                self.table_field.unique = False
                self.table_field.none = True

    # signal handler for the next attribute button
    def table_fields_next_fn(self, button):
        fields_error_text = self.t.get_text("fields_create_error")

        field_name = self.table_field.field_name
        field_type = self.table_field.field_type

        logging.debug("field_name: {0}, type: {1}".format(field_name, field_type))

        if field_name == "" or field_type == "":
            self.fields_error_text.original_widget = urwid.AttrWrap(urwid.Text(fields_error_text), "error")

        else:
            self.fields_error_text.original_widget = self.empty_text()

            # add table field to table and increment number of fields edited
            self.table.table_fields.append(self.table_field)
            self.table.fields_edited += 1

            # reset table field
            self.table_field = None

        fields_edited = self.table.fields_edited
        number_of_fields = self.table.number_of_fields

        if fields_edited < number_of_fields:
            self.create_table_fields()
        else:
            self.create_table()

    # signal handler for create button
    def create_table(self):
        query = ""

        query += "CREATE TABLE {0} (\n".format(self.table.table_name)

        table_fields = self.table.table_fields

        last = len(table_fields) - 1

        for index, table_field in enumerate(table_fields):
            query += "{0} {1}".format(table_field.field_name, table_field.field_type)

            if table_field.not_null:
                query += " NOT NULL"

            if table_field.primary_key:
                query += " PRIMARY KEY"

            if table_field.unique:
                query += " UNIQUE"

            if index != last:
                query += ",\n"

        query += "\n);"

        logging.debug("query: {0}".format(query))

        connection = self.database_info.connection
        response = self.db.execute_query(connection, query)

        if response["success"]:
            footer_text = self.t.get_text("table_created_successfully")
            footer_text = urwid.Text(footer_text, align="center")
            footer_widget = urwid.AttrWrap(footer_text, "footer")
            self.frame.footer = footer_widget

            self.body_info.original_widget = DatabaseView(self.database_info).database_info_widget()
            self.table_listing.original_widget = self.table_listing_fn()
        else:
            error_text = self.t.get_text("table_create_query_failed")
            error_text = "{0} {1}".format(error_text, response["data"])
            error_text_size = len(error_text)
            error_text = urwid.Text(error_text, align="center")
            error_text = urwid.AttrWrap(error_text, "error")
            error_text = urwid.Padding(error_text, width=error_text_size)
            self.fields_error_text.original_widget = error_text

            try_again_text = self.t.get_text("try_again")
            try_again_btn_size = len(try_again_text) + 10
            try_again_btn = urwid.Button(try_again_text, self.try_again_fn)
            try_again_btn = urwid.AttrWrap(try_again_btn, "b_hover", "b_text")
            try_again_btn = urwid.Padding(try_again_btn, left=2, width=try_again_btn_size)

            self.forward_btn.original_widget = try_again_btn

    # signal handler for try again button
    def try_again_fn(self, button):
        self.table.table_fields = []
        self.table.fields_edited = 0
        self.create_table_fields()
