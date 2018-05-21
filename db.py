from typing import Dict
import records



class Db(records.Database):
	pass

	def insert(self, table_name, params: Dict):
		sql = DB.insert_sql(table_name, params)
		
		self.query(sql, **params)

	def insert_sql(table_name, params: Dict):
		keys = list(params)
		field_sql = ', '.join(keys)
		values_sql = ',:'.join(keys)

		sql = "INSERT into {} ({}) VALUES (:{})".format(table_name, field_sql, values_sql)

		return sql

