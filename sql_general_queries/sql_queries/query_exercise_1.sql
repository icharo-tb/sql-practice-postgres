SELECT
	p.category,
	ROUND(SUM(o.revenue)::numeric,2) AS total_revenue
FROM products p
INNER JOIN orders o ON p.product_id = o.product_id
WHERE TO_DATE(o.order_date, 'MM-DD-YYYY') >= DATE_TRUNC('month', CURRENT_DATE) - INTERVAL '1 year'
GROUP BY p.category
ORDER BY total_revenue DESC;