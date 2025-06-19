-- Write your PostgreSQL query statement below
WITH one AS (SELECT u.name
FROM MovieRating m 
JOIN Users u
ON m.user_id = u.user_id
GROUP BY u.name
ORDER BY COUNT(m.movie_id) DESC, u.name ASC
LIMIT 1),
 
two AS (SELECT m.title
FROM MovieRating mr
JOIN Movies m
ON m.movie_id = mr.movie_id
WHERE mr.created_at < '2020-03-01' AND mr.created_at > '2020-01-31'
GROUP BY m.title
ORDER BY AVG(mr.rating) DESC, m.title ASC
LIMIT 1)

SELECT name AS results FROM one
UNION ALL
SELECT title AS results FROM two