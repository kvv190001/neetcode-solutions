# Write your MySQL query statement below
SELECT DISTINCT a.num AS ConsecutiveNums
FROM Logs a
JOIN Logs b
JOIN Logs c
ON a.num = b.num AND b.num = c.num
WHERE a.id = b.id + 1 and b.id = c.id + 1