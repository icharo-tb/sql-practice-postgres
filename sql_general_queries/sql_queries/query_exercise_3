SELECT
	c.region,
	ROUND(SUM(o.revenue)::numeric,2) total_revenue
FROM customers c
	INNER JOIN orders o ON c.customer_id = o.customer_id
	INNER JOIN products p ON o.product_id = p.product_id
WHERE p.category LIKE 'Electro%'
GROUP BY c.region
ORDER BY total_revenue DESC;