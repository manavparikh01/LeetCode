# Write your MySQL query statement below
WITH cust_first_order_date AS (SELECT customer_id, MIN(order_date) AS first_order_date FROM Delivery
GROUP BY customer_id),
c_f_emmediate AS (SELECT c.customer_id FROM cust_first_order_date c
JOIN Delivery d
ON c.customer_id = d.customer_id AND c.first_order_date = d.order_date
WHERE d.order_date = d.customer_pref_delivery_date)
SELECT ROUND(
    (SELECT COUNT(customer_id) FROM c_f_emmediate) /
    (SELECT COUNT(customer_id) FROM cust_first_order_date) * 100, 2
) AS immediate_percentage
