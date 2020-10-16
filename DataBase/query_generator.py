import unittest


class QueryGenerator(object):
    def __init__(self, table_name: str):
        self._table = table_name
        self.tbl_attributes = dict()
        self._string_format = ['s', 'str', 'string']

    def select(self, attributes: list, conditions: dict) -> str:
        att, cond = str(), str()
        for ats in attributes:
            att += '[{0}], '.format(ats)

        for key in conditions:
            cond += '{0} and '.format(self._get_condition_structure(attribute=key, information=conditions.get(key)))

        return 'SELECT {0} FROM {1} WHERE {2}'.format(att[:-2], self._table, cond[:-4])

    def update_by_id(self, row: int, attribute: str, value) -> str:
        val = self._get_string(value) if self.tbl_attributes.get(attribute) in self._string_format else value

        return 'UPDATE {0} SET {1} = {2} WHERE id = {3}'.format(self._table, attribute, val, row)

    @staticmethod
    def _get_string(data) -> str:
        return '\'{0}\''.format(data)

    def _get_condition_structure(self, attribute: str, information: dict) -> str:
        temp = '[{0}]'.format(attribute)

        # set type
        if information.get('type', '').lower() in ['g', 'greater', 'great']:
            temp += ' > '
        elif information.get('type', '').lower() in ['l', 'less', 'lesser']:
            temp += ' < '
        else:
            temp += ' = '

        # set value
        if self.tbl_attributes.get(attribute).lower() in self._string_format:
            temp += str(self._get_string(information.get('value')))
        else:
            temp += str(information.get('value'))

        return temp


class TestCase(unittest.TestCase):
    def test_query_generator(self):
        # H0
        h0 = 'SELECT [id], [c1], [c2], [c3] FROM test WHERE [c1] < \'first val\' and [c2] = 123 '

        # H1
        qg = QueryGenerator(table_name='test')
        qg.tbl_attributes = {'id': 'int', 'c1': 'string', 'c2': 'int', 'c3': 'float'}
        h1 = qg.select(attributes=['id', 'c1', 'c2', 'c3'],
                       conditions={'c1': {'type': 'l', 'value': 'first val'}, 'c2': {'value': 123}})

        self.assertEqual(first=h0, second=h1)
        return


if __name__ == '__main__':
    unittest.main()

