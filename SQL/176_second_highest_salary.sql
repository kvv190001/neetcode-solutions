-- Write your PostgreSQL query statement below
-- SELECT MAX(salary) SecondHighestSalary
-- FROM Employee
-- WHERE salary < (SELECT MAX(salary) FROM Employee)

-- Write your PostgreSQL query statement below
SELECT (SELECT DISTINCT salary 
FROM Employee 
ORDER BY salary DESC 
OFFSET 1 
LIMIT 1) AS SecondHighestSalary 