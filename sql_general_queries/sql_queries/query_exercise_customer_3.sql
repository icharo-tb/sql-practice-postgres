SELECT
	CASE
		WHEN TO_DATE(o.order_date, 'MM-DD-YYYY') >= DATE_TRUNC('month', CURRENT_DATE) - INTERVAL '1 year'
		THEN SUM(o.revenue)
	END annualized_customer_value
FROM orders o
INNER JOIN customers c ON o.customer_id = c.customer_id
GROUP BY o.order_date;