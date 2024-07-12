# Write your MySQL query statement below
SELECT sell_date, COUNT(DISTINCT product) AS num_sold, GROUP_CONCAT(DISTINCT product) AS products
FROM Activities
GROUP BY sell_date
ORDER BY sell_date, product;

# SELECT product
# FROM Activities
# WHERE sell_date = '2020-05-30'
# ORDER BY product;