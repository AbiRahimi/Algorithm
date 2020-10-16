import sqlite3
from DataBase.query_generator import QueryGenerator


class DB(object):
    def __init__(self, table_name: str, data_base='Abi.db'):
        self._conn = sqlite3.connect(data_base)
        self._query = QueryGenerator(table_name=table_name)

    def set_table_attributes(self, **kwargs):
        self._query.tbl_attributes = kwargs

        return

    def db_commit(self):
        self._conn.commit()

        return

    def db_close(self):
        self._conn.commit()
        self._conn.close()

        return

    def insert(self, **kwargs):
        # TODO: create insert query and insert to db
        pass

    def update(self, row_id: int, attribute: str, value):

        pass

    def select(self, *args) -> list:
        pass
