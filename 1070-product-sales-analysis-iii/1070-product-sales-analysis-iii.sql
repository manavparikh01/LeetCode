# Write your MySQL query statement below
WITH product_first_year AS (SELECT product_id, MIN(year) AS first_year FROM 
Sales
GROUP BY product_id)
SELECT s.product_id, s.year AS first_year, s.quantity, s.price FROM Sales AS s
JOIN product_first_year p
ON s.product_id = p.product_id AND s.year = p.first_year
