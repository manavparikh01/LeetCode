# Write your MySQL query statement below
WITH Firstdeliv AS (SELECT customer_id, MIN(order_date) AS firstdate
FROM Delivery
GROUP BY customer_id)
SELECT ROUND(SUM(IF(f.firstdate = d.customer_pref_delivery_date, 1, 0)*100/(SELECT COUNT(*)
FROM Firstdeliv)), 2) AS immediate_percentage
FROM Delivery AS d
JOIN Firstdeliv AS f
ON d.customer_id = f.customer_id AND d.order_date = f.firstdate



