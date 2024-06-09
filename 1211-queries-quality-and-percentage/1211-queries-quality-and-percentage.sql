# Write your MySQL query statement below
WITH Percen AS (SELECT query_name, COUNT(query_name) AS ratingl
               FROM Queries
               WHERE rating < 3
               GROUP BY query_name)
SELECT q.query_name, ROUND(AVG(q.rating/q.position),2) AS quality, IFNULL(ROUND(p.ratingl*100/COUNT(q.query_name),2), 0.00) AS poor_query_percentage
FROM Queries AS q
LEFT JOIN Percen AS p
ON q.query_name = p.query_name
WHERE q.query_name IS NOT NULL
GROUP BY q.query_name;