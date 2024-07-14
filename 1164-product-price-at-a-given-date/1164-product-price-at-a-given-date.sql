# Write your MySQL query statement below
WITH Changed AS (SELECT p.product_id, p.new_price AS price
FROM Products AS p
WHERE p.change_date = (
  SELECT MAX(change_date)
  FROM Products AS p2
  WHERE p2.product_id = p.product_id
  AND p2.change_date <= '2019-08-16'
))
SELECT DISTINCT p.product_id, IFNULL(c.price, 10) AS price
FROM Products AS p
LEFT JOIN Changed AS c
ON p.product_id = c.product_id;
