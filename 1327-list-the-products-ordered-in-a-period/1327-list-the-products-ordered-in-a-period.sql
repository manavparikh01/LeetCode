# Write your MySQL query statement below
SELECT p.product_name, SUM(o.unit) AS unit
FROM Orders AS o
JOIN Products AS p
ON o.product_id = p.product_id
WHERE YEAR(o.order_date) = 2020 AND MONTH(o.order_date) = 2
GROUP BY p.product_id
HAVING unit >= 100;