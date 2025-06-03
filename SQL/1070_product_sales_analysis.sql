WITH FirstSales AS (
    SELECT product_id, MIN(year) AS first_year
    FROM Sales
    GROUP BY product_id
)

SELECT s.product_id, s.year AS first_year, s.quantity, s.price
FROM Sales s
JOIN FirstSales ms
ON s.product_id = ms.product_id AND s.year = ms.first_year