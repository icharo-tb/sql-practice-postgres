SELECT
	p.category,
	ROUND(AVG(o.quantity),2) avg_orders
FROM products p
INNER JOIN orders o ON p.product_id = o.product_id
WHERE EXTRACT('Year' FROM TO_DATE(o.order_date, 'MM-DD-YYYY')) = '2022'
GROUP BY p.category
ORDER BY avg_orders DESC;