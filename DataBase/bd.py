import sqlite3
from DataBase.query_generator import QueryGenerator


class DB(object):
    PathDB = '/home/abi/AbiPy/Algorithm/DataBase/Abi.db'

    def __init__(self, table_name: str, data_base=None):
        self._conn = sqlite3.connect(self.PathDB if data_base is None else data_base)
        self._c = self._conn.cursor()
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
        self._c.execute(self._query.update_by_id(row=row_id, attribute=attribute, value=value))

        return

    def select(self, attributes: list, conditions: dict) -> list:
        self._c.execute(self._query.select(attributes=attributes, conditions=conditions))

        temp = list()
        for row in self._c.fetchall():
            val = dict()
            for i in range(len(attributes)):
                val[attributes[i]] = row[i]
            temp.append(val)

        return temp


if __name__ == '__main__':
    db = DB(table_name='date_dim')
    db.set_table_attributes(id='int', solar_yaer='int', solar_month='int')
    db.select(attributes=['solar_year', 'solar_month'], conditions={'id': {'value': 12, 'type': 'less'}})
