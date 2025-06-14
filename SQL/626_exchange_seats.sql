-- Write your PostgreSQL query statement below
SELECT CASE WHEN id % 2 = 1 AND id + 1 IN (SELECT id FROM SEAT) THEN id + 1
            WHEN id % 2 = 0 THEN id - 1
            ELSE id
        END AS id,
        student
FROM SEAT
ORDER BY id ASC