# Write your MySQL query statement below
WITH MinDate AS (SELECT p.product_id, MIN(s.year) AS first_year
FROM Product AS p
JOIN Sales AS s
ON p.product_id = s.product_id
GROUP BY s.product_id)
SELECT m.product_id, m.first_year, s.quantity, s.price
FROM MinDate AS m
JOIN Sales AS s
ON m.product_id = s.product_id AND m.first_year = s.year;
