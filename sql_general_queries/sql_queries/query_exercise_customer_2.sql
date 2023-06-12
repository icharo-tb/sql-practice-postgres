SELECT
	p.category,
	p.subcategory,
	SUM(o.quantity) total_orders
FROM products p
INNER JOIN orders o ON p.product_id = o.product_id
WHERE p.category = 'Beauty'
GROUP BY p.subcategory, p.category;