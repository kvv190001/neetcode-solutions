-- Write your PostgreSQL query statement below
WITH first_delivery AS (
    SELECT DISTINCT customer_id, MIN(order_date) AS order_date
    FROM Delivery
    GROUP BY customer_id
)

SELECT ROUND(AVG(CASE WHEN d.order_date = d.customer_pref_delivery_date THEN 1 ELSE 0 END)::NUMERIC * 100,2) AS immediate_percentage
FROM first_delivery fd
JOIN Delivery d
ON fd.customer_id = d.customer_id AND fd.order_date = d.order_date