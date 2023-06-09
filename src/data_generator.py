import json
from datetime import datetime

import psycopg2

from dotenv import load_dotenv
load_dotenv()

import os

customer_data = [
	{
		'name': "Tamara Hyde",
		'postalZip': "76486",
		'region': "Goias",
		'country': "Vietnam"
	},
	{
		'name': "Phillip Blevins",
		'postalZip': "79425",
		'region': "Queensland",
		'country': "Canada"
	},
	{
		'name': "Claudia Zamora",
		'postalZip': "18210",
		'region': "Zamboanga Peninsula",
		'country': "Vietnam"
	},
	{
		'name': "Patricia Dyer",
		'postalZip': "16986",
		'region': "Antalya",
		'country': "Peru"
	},
	{
		'name': "Amal Schroeder",
		'postalZip': "187333",
		'region': "Niger",
		'country': "Vietnam"
	},
	{

		'name': "Keaton Franks",
		'postalZip': "233160",
		'region': "Huabei",
		'country': "Sweden"
	},
	{
		'name': "Brittany Delgado",
		'postalZip': "04564",
		'region': "Victoria",
		'country': "Vietnam"
	},
	{
		'name': "Griffin Gaines",
		'postalZip': "415445",
		'region': "Nam Dinh",
		'country': "Canada"
	},
	{
		'name': "Kylan Melendez",
		'postalZip': "77803",
		'region': "South Kalimantan",
		'country': "Norway"
	},
	{
		'name': "Cheryl Alexander",
		'postalZip': "13677",
		'region': "Izmir",
		'country': "South Africa"
	}
]


def postgres_connect(load_data=False):

	conn = None
    
	try:
		
		print('Connecting to PostgreSQL customers_practice')
		conn = psycopg2.connect(
		host='localhost',
		database='customers_pratice',
		user='postgres',
		password=os.getenv('POSTGRES_PASS')
		)

		cur = conn.cursor()

		print(f"Postgres Database Version:\n {cur.execute('SELECT version()')}")

		db_version = cur.fetchone()
		print(db_version)

		if load_data == True:

			try:
				# customer data
				with open('./Assets/customers.json') as cj:
					customer_data = json.load(cj)
					for customer in customer_data:
						customer_query = f"INSERT INTO customers(name, postal_code, city, region) \
									VALUES('{customer.get('name')}',{customer.get('postalZip')},'{customer.get('region')}','{customer.get('country')}');"
					
						cur.execute(customer_query)
						conn.commit()
					
					print('Customer data inserted.')

				# product data
				with open('./Assets/products.json') as pj:
					product_data = json.load(pj)
					for product in product_data:
						product_query = f"INSERT INTO products(brand, category, subcategory) \
									VALUES('{product.get('name')}','{product.get('category')}','{product.get('subcategory')}');"
						
						cur.execute(product_query)
						conn.commit()

					print('Product data inserted.')

				# order data
				with open('./Assets/orders.json') as oj:
					order_data = json.load(oj)
					for order in order_data['order_details']:

						product_id = order.get('products',{}).get('product_id')
						customer_id = order.get('customers',{}).get('customer_id')

						order_qty = order.get('orders',{}).get('quantity')
						order_price = order.get('orders',{}).get('list_price')
						order_revenue = order.get('orders',{}).get('revenue')

						order_query = f"INSERT INTO orders(product_id, customer_id, quantity, list_price, revenue, order_date) \
							VALUES({product_id},{customer_id},{order_qty},{order_price},{order_revenue},'{order.get('order_date')}');"
						
						cur.execute(order_query)
						conn.commit()

					print('Order data inserted.')
			except Exception as e:
				print(e)
		
		cur.close()
	except Exception as e:
		print(e)
	finally:
		if conn is not None:
			conn.close()
			print('Connection closed.')

if __name__=='__main__':
	postgres_connect(load_data=True)