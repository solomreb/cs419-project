#!/usr/bin/env python

import urwid
from view_base import BaseView
from view_dashboard import DashboardView


class LoginView(BaseView):
    def __init__(self, database_info):
        super(LoginView, self).__init__(database_info)
        self.error_box = None

    def create(self):
        database_select = self.create_database_select()
        conn_details = self.create_conn_details()
        connect_btn = self.create_connect_btn()
        self.error_box = self.create_error_box()

        body = urwid.Pile([
            urwid.Text(self.t.get_text("login_header_1")),
            urwid.Divider(),
            database_select,
            urwid.Divider(),
            urwid.Divider(),
            urwid.Text(self.t.get_text("login_header_2")),
            urwid.Divider(),
            conn_details,
            urwid.Divider(),
            connect_btn,
            urwid.Divider(),
            self.error_box
        ])

        body = urwid.Padding(body, left=self.h_padding, right=self.h_padding)
        body = urwid.WidgetPlaceholder(urwid.Filler(body, valign="top", top=self.v_padding))

        self.body = urwid.AttrWrap(body, "body")

        header_widget_text = urwid.Text(self.t.get_text("header"))
        header_widget = urwid.Padding(header_widget_text, left=2, right=2)
        header_widget = urwid.AttrWrap(header_widget, "header")

        footer_widget_text = urwid.Text(self.t.get_text("footer"))
        footer_widget = urwid.Padding(footer_widget_text, left=2, right=2)
        footer_widget = urwid.AttrWrap(footer_widget, "footer")

        self.frame = urwid.Frame(body=self.body, header=header_widget, footer=footer_widget)

        return self.frame

    def create_database_select(self):
        radio_list = []

        psql_radio_text = self.t.get_text("postgresql")
        psql_radio_btn_size = len(psql_radio_text) + 4
        psql_radio_btn = urwid.RadioButton(radio_list, psql_radio_text)
        psql_radio_widget = urwid.AttrWrap(psql_radio_btn, "m_text", "m_hover")

        database_select = urwid.Pile([psql_radio_widget])

        return urwid.Padding(database_select, width=psql_radio_btn_size, left=self.h_padding)

    def create_edit_widget(self, text, attr, focus_attr, mask="", int_edit=False, default_text=""):
        if mask:
            edit = urwid.Edit(self.t.get_text(text), "", mask=mask)
        else:
            if int_edit:
                edit = urwid.IntEdit(self.t.get_text(text), default_text)
            else:
                edit = urwid.Edit(self.t.get_text(text), default_text)

        urwid.connect_signal(edit, "change", self.conn_details_fn)

        return urwid.AttrWrap(edit, attr, focus_attr)

    def create_conn_details(self):
        host_input = self.create_edit_widget("host_label", "m_text", "m_hover", default_text=self.database_info.host)
        port_input = self.create_edit_widget("port_label", "m_text", "m_hover", int_edit=True, default_text=self.database_info.port)
        username_input = self.create_edit_widget("username_label", "m_text", "m_hover")
        password_input = self.create_edit_widget("password_label", "m_text", "m_hover", self.t.get_text("mask"))
        database_input = self.create_edit_widget("database_label", "m_text", "m_hover")
        conn_details = urwid.Pile([host_input, port_input, username_input, password_input, database_input])
        return urwid.Padding(conn_details, left=self.h_padding, width=45)

    def create_connect_btn(self):
        text = self.t.get_text("connect")
        size = len(text) + 4
        connect_btn = urwid.AttrWrap(urwid.Button(text, self.connect_fn), "m_text", "m_hover")
        return urwid.Padding(connect_btn, left=self.h_padding, width=size)

    def create_error_box(self):
        text = self.t.get_text("connection_error")
        size = len(text) + 4
        error_box = urwid.AttrMap(urwid.Text(u""), "m_text")
        return urwid.Padding(error_box, left=self.h_padding, width=size)

    # handler for the connect button
    def connect_fn(self, button):
        error_text = self.t.get_text("connection_error")

        host = self.database_info.host
        port = self.database_info.port
        username = self.database_info.username
        password = self.database_info.password
        database = self.database_info.database

        if host and port and username and database:
            self.database_info.connection = self.db.connect(host, port, database, username, password)

            if self.database_info.connection == -1:
                self.error_box.original_widget = urwid.AttrMap(urwid.Text(error_text), "error")
            else:
                self.error_box.original_widget = urwid.AttrMap(urwid.Text(u"success"), "m_text")
                DashboardView(self.database_info).create(self.frame, self.body)
        else:
            self.error_box.original_widget = urwid.AttrMap(urwid.Text(error_text), "error")

    # handler to store input from user
    def conn_details_fn(self, widget, text):
        if widget.caption == self.t.get_text("host_label"):
            self.database_info.host = text
        elif widget.caption == self.t.get_text("port_label"):
            self.database_info.port = text
        elif widget.caption == self.t.get_text("username_label"):
            self.database_info.username = text
        elif widget.caption == self.t.get_text("password_label"):
            self.database_info.password = text
        elif widget.caption == self.t.get_text("database_label"):
            self.database_info.database = text
