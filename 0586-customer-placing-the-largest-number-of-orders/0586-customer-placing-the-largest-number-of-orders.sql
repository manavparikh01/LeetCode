# Write your MySQL query statement below
WITH cus_count AS (SELECT customer_number, COUNT(order_number) AS count_number
FROM Orders
GROUP BY customer_number)
SELECT c.customer_number
FROM cus_count c
WHERE c.count_number = (SELECT MAX(count_number) FROM cus_count)

-- SELECT customer_number
-- FROM Orders
-- WHERE
-- SELECT customer_number
-- FROM Orders
-- GROUP BY customer_number
-- ORDER BY COUNT(order_number) DESC
-- LIMIT 1