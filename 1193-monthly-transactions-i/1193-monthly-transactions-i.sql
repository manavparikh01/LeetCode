# Write your MySQL query statement below
WITH Approve AS (SELECT DATE_FORMAT(trans_date, '%Y-%m') as month, IFNULL(country, null) AS country, COUNT(state) AS approved_count, SUM(amount) AS approved_total_amount
                FROM Transactions
                WHERE state = 'approved'
                GROUP BY month, country),
      Total AS (SELECT DATE_FORMAT(trans_date, '%Y-%m') as month, IFNULL(country, null) AS country, COUNT(state) AS trans_count, SUM(amount) AS trans_total_amount
                FROM Transactions
                GROUP BY month, country)
SELECT t.month, t.country, t.trans_count, IFNULL(a.approved_count, 0) AS approved_count, t.trans_total_amount, IFNULL(a.approved_total_amount, 0) AS approved_total_amount
FROM Total AS t
LEFT OUTER JOIN Approve AS a
ON t.month = a.month AND COALESCE(t.country, '') = COALESCE(a.country, '');
