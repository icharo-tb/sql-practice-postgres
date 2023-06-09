DROP TABLE IF EXISTS products CASCADE;
DROP TABLE IF EXISTS customers CASCADE;
DROP TABLE IF EXISTS orders CASCADE;

CREATE TABLE products(
	product_id INT GENERATED ALWAYS AS IDENTITY,
	brand TEXT,
	category VARCHAR(255),
	subcategory VARCHAR(255),
	created_at TIMESTAMPTZ DEFAULT Now(),
	PRIMARY KEY(product_id)
);

CREATE TABLE customers(
	customer_id INT GENERATED ALWAYS AS IDENTITY,
	name TEXT,
	postal_code INT,
	city VARCHAR(255),
	region VARCHAR(255),
	created_at TIMESTAMPTZ DEFAULT Now(),
	PRIMARY KEY(customer_id)
);

CREATE TABLE orders(
	order_id INT GENERATED ALWAYS AS IDENTITY,
	product_id INT,
	customer_id INT,
	quantity INT,
	list_price FLOAT,
	revenue FLOAT,
	order_date VARCHAR(255),
	created_at TIMESTAMPTZ DEFAULT Now(),
	PRIMARY KEY(order_id),
	CONSTRAINT fk_product
		FOREIGN KEY(product_id)
			REFERENCES products(product_id)
			ON DELETE SET NULL,
	CONSTRAINT fk_customer
		FOREIGN KEY(customer_id)
			REFERENCES customers(customer_id)
			ON DELETE SET NULL
);