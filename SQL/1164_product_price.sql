-- Write your PostgreSQL query statement below
WITH recent_date AS (SELECT DISTINCT product_id, MAX(change_date) change_date
FROM Products
WHERE change_date <= '2019-08-16'
GROUP BY product_id)

SELECT DISTINCT product_id, 10 as price
FROM products
GROUP BY product_id
HAVING min(change_date) > '2019-08-16'

UNION ALL

SELECT p.product_id, p.new_price
FROM Products p 
JOIN recent_date rd
ON p.product_id = rd.product_id AND p.change_date = rd.change_date

