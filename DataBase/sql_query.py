
class DB(object):
    def __init__(self):
        self.tbl = str()
        self._cond = list()

    def set_table_name(self, table: str, schema='dbo', database=None):
        if database is None:
            self.tbl = table

        else:
            self.tbl = '[{0}].[{1}].[{2}]'.format(database, schema, table)

    @staticmethod
    def conv_value(value, is_string) -> str:
        if is_string:
            return 'N\'{0}\''.format(value)

        else:
            return '{0}'.format(value)

    def set_condition(self, attribute: str, value, is_string=False, equation='='):
        equation.upper()
        if equation == 'IN':
            tmp = str()
            for val in value:
                tmp += '{0}, '.format(val)

            self._cond.append('[{0}] IN ({1})'.format(attribute, tmp[:-2]))

        elif equation == 'BETWEEN':
            val = list(value)
            val.sort()
            v1 = self.conv_value(value=val[0], is_string=is_string)
            v2 = self.conv_value(value=val[-1], is_string=is_string)
            self._cond.append('[{0}] BETWEEN {1} AND {2}'.format(attribute, v1, v2))

        else:
            val = self.conv_value(value=value, is_string=is_string)
            self._cond.append('[{0}] {1} {2}'.format(attribute, equation, val))

        return

    def where_str(self):
        if len(self._cond) == 0:
            return ' '

        else:
            tmp = 'WHERE '
            for cnd in self._cond:
                tmp += '{0} AND '.format(cnd)

            return tmp[:-4]

    def get_query(self) -> str:
        pass


class Insert(DB):
    def __init__(self):
        DB.__init__(self)
        self._ats = str()
        self._vls = str()

    def set_attribute(self, attribute: str, value, is_string=False):
        self._ats += '[{0}], '.format(attribute)
        self._vls += self.conv_value(value=value, is_string=is_string)

    def get_query(self):
        return 'INSERT INTO {0} ({1}) VALUES ({2});'.format(self.tbl, self._ats[:-2], self._vls[:-2])


class Update(DB):
    def __init__(self):
        DB.__init__(self)
        self._val = str()

    def set_value(self, attribute: str, value, is_string=False):
        val = self.conv_value(value=value, is_string=is_string)
        self._val = '[{0}] = {1},'.format(attribute, val)

        return

    def get_query(self):
        return 'UPDATE {0} SET {1} {2} ;'.format(self.tbl, self._val[:-2], self.where_str())


class Select(DB):
    def __init__(self):
        DB.__init__(self)
        self.columns = tuple()

    def set_columns(self, *args):
        self.columns = args

    def _get_column(self) -> str:
        tmp = str()
        for clm in self.columns:
            tmp += '[{0}], '.format(clm)

        return tmp[:-2]

    def get_query(self) -> str:
        return 'SELECT {0} FROM {1} {2} ;'.format(self._get_column(), self.tbl, self.where_str())


class Delete(DB):
    def __init__(self):
        DB.__init__(self)

    def get_query(self) -> str:
        return 'DELETE FROM {0} {1} ;'.format(self.tbl, self.where_str())
