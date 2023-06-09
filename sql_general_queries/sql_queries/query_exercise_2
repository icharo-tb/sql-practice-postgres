SELECT
	p.brand,
	ROUND(SUM(o.revenue)::numeric,2) total_revenue
FROM products p
INNER JOIN orders o ON p.product_id = o.product_id
WHERE p.category = 'Beauty'
GROUP BY p.brand
ORDER BY total_revenue ASC;