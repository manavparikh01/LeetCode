# Write your MySQL query statement below
# WITH TotalUnits AS (SELECT product_id, SUM(units) AS sumunits
#                    FROM UnitsDold
#                    GROUP BY product_id)
SELECT p.product_id, IFNULL(ROUND(SUM(p.price*u.units)/SUM(u.units), 2), 0.00) AS average_price
FROM Prices AS p
LEFT JOIN UnitsSold AS u
ON p.product_id = u.product_id AND u.purchase_date >= p.start_date AND u.purchase_date <= p.end_date
GROUP BY p.product_id