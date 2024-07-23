# Write your MySQL query statement below
WITH Allsum AS (SELECT visited_on, SUM(amount) AS amount
               FROM Customer
               GROUP BY visited_on
               ORDER BY visited_on),
Avgsum AS (SELECT visited_on, 
SUM(amount) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS amount, 
AVG(amount) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS average_amount
FROM Allsum
ORDER BY visited_on)
SELECT visited_on, ROUND(amount,2) AS amount, ROUND(average_amount,2) AS average_amount
FROM Avgsum
WHERE DATEDIFF(visited_on, (SELECT MIN(visited_on) FROM Avgsum)) >= 6;
