# Write your MySQL query statement below
WITH cumulative AS (SELECT *, SUM(weight) OVER (ORDER BY turn) AS cum_sum
FROM Queue
ORDER BY turn)
-- SELECT * FROM cumulative
SELECT person_name FROM cumulative
WHERE cum_sum <= 1000
ORDER BY cum_sum DESC
LIMIT 1
