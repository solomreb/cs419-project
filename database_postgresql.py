#!/usr/bin/env python

import psycopg2
import logging

logging.basicConfig(filename="cs419.log", level=logging.DEBUG)


class PostgreSQL:
    def connect(self, host, port, database, username, password):
        logging.debug(
            "pgsql:host={0};port={1};dbname={2};user={3};password={4}".format(host, port, database, username, password))

        try:
            logging.debug("db connect success")
            return psycopg2.connect(host=host, port=port, user=username, password=password, database=database)
        except psycopg2.OperationalError:
            logging.debug("db connect error")
            return -1

    def get_tables(self, conn):
        cursor = conn.cursor()

        query = """
                  SELECT DISTINCT table_name
                    FROM information_schema.tables
                   WHERE table_schema='public'
                     AND table_type='BASE TABLE'
                ORDER BY table_name;
            """

        logging.debug("db get_tables: {0}".format(query))

        names = -1

        try:
            cursor.execute(query)
            data = cursor.fetchall()

            names = []

            for table in data:
                names.append(table[0])
        except psycopg2.Error as e:
            logging.debug(e)
            pass

        cursor.close()

        return names

    def get_database_stats(self, conn, database_name):
        cursor = conn.cursor()

        query = """
            SELECT pg_size_pretty(pg_database_size(datname)) AS "Size",
                   pg_catalog.pg_encoding_to_char(encoding) AS "Encoding",
                   datcollate AS "Collate"
              FROM pg_catalog.pg_database
             WHERE datname=(%s);
        """

        logging.debug("db get_database_stats: {0}".format(query))

        data = -1

        try:
            cursor.execute(query, [database_name])
            data = cursor.fetchall()[0]
        except psycopg2.Error as e:
            logging.debug(e)
            pass

        cursor.close()

        return data

    def get_database_table_info_list(self, conn):
        cursor = conn.cursor()

        query = """
              SELECT relname AS "Table",
                     pg_size_pretty(pg_total_relation_size(relid)) AS "Size"
                FROM pg_catalog.pg_statio_user_tables
            ORDER BY pg_total_relation_size(relid) DESC;
        """

        logging.debug("db get_database_table_info_list: {0}".format(query))

        data = -1

        try:
            cursor.execute(query)
            data = cursor.fetchall()
        except psycopg2.Error as e:
            logging.debug(e)
            pass

        cursor.close()

        return data

    def get_table_info(self, conn, table_name):
        cursor = conn.cursor()

        query = """
            SELECT column_name,
                   data_type,
                   character_maximum_length,
                   is_nullable
              FROM information_schema.columns
             WHERE table_name=(%s);
        """

        logging.debug("db get_table_info: {0}".format(query))

        data = -1

        try:
            cursor.execute(query, [table_name])
            data = cursor.fetchall()
        except psycopg2.Error as e:
            logging.debug(e)
            pass

        cursor.close()

        return data

    def get_table_columns(self, conn, table_name):
        cursor = conn.cursor()

        query = """
            SELECT column_name
              FROM information_schema.columns
             WHERE table_name=(%s);
        """

        logging.debug("db get_table_columns: {0}".format(query))

        data = -1

        try:
            cursor.execute(query, [table_name])
            data = cursor.fetchall()
        except psycopg2.Error as e:
            logging.debug(e)
            pass

        cursor.close()

        return data

    def execute_query(self, conn, query, fetch=False):
        cursor = conn.cursor()

        success = True
        data = ""

        logging.debug("db execute_query: {0}".format(query))

        try:
            cursor.execute(query)
            conn.commit()

            if fetch:
                data = cursor.fetchall()

        except psycopg2.Error as e:
            logging.debug(e)
            success = False
            data = e.pgerror
            conn.rollback()

        cursor.close()

        return {"success": success, "data": data}

    def fetch_all_rows(self, conn, table_name):
        cursor = conn.cursor()

        query = """
            SELECT *
              FROM {0}
        """

        logging.debug("db fetch_all_rows: {0}".format(query))

        data = -1

        try:
            cursor.execute(query.format(table_name))
            data = cursor.fetchall()
        except psycopg2.Error as e:
            logging.debug(e)
            pass

        cursor.close()

        return data
