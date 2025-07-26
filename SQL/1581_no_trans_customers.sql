-- Write your PostgreSQL query statement below
WITH Customers AS (
    SELECT v.customer_id, t.transaction_id 
    FROM Visits v
    LEFT JOIN Transactions t
    ON v.visit_id = t.visit_id    
)

SELECT customer_id, COUNT(customer_id) count_no_trans
FROM Customers
WHERE transaction_id IS NULL
GROUP BY customer_id