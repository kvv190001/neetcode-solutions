-- Write your PostgreSQL query statement below
SELECT r.contest_id, ROUND(COUNT(r.user_id)::numeric * 100 / (SELECT COUNT(user_id) FROM Users),2) percentage
FROM Register r
GROUP BY contest_id
ORDER BY percentage DESC, contest_id
