from DataBase.bd import DB
import unittest
import datetime


class SolarDate(object):
	def __init__(self, year=None, month=None, day=None):
		# TODO: gregorian parameters
		self._date = self.set_gregorian_date(year=year, month=month, day=day)

	def get_solar_year(self):
		return self._date.get('solar_year')

	def get_solar_month(self):
		return self._date.get('solar_month')

	def get_solar_day(self):
		return self._date.get('solar_day')

	def get_solar_date(self):
		year = str(self.get_solar_year())
		month = str(self.get_solar_month()).zfill(2)
		day = str(self.get_solar_day()).zfill(2)

		return '{0}/{1}/{2}'.format(year, month, day)

	def get_solar_week_day(self):
		return self._date.get('week_day')

	def set_gregorian_date(self, year, month, day):
		now = datetime.datetime.now()
		y = now.year if year is None else year
		m = now.month if month is None else month
		d = now.day if day is None else day

		# get solar date from db
		return self._get_solar_date_inf(year=y, month=m, day=d)

	@staticmethod
	def _get_solar_date_inf(year, month, day) -> dict:
		# TODO: connect to date_dime table in db for get solar information
		db = DB(table_name='date_dim')
		db.set_table_attributes(
			id='int', solar_year='int', solar_month='int', solar_day='int', week_day='str',
			gregorian_year='int', gregorian_month='int', gregorian_day='int')

		attributes = ['solar_year', 'solar_month', 'solar_day', 'week_day']
		conditions = {
			'gregorian_year': {'value': year, 'type': 'equal'},
			'gregorian_month': {'value': month, 'type': 'equal'},
			'gregorian_day': {'value': day, 'type': 'equal'}}

		temp = db.select(attributes=attributes, conditions=conditions)
		db.db_close()

		return temp[0] if len(temp) > 0 else dict()


class TestCase(unittest.TestCase):
	def test_get_solar_date(self):
		# 1399 mehr 26 == 17 oct 2020
		# H0: '1399/07/26  H1: convert 17 oct 2020 to solar date
		sld = SolarDate(year=2020, month=10, day=17)
		self.assertEqual(first='1399/07/26', second=sld.get_solar_date())

		return


if __name__ == '__main__':
	unittest.main()
