# # Write your MySQL query statement below
WITH Categories AS (
    SELECT 'Low Salary' AS category
    UNION ALL
    SELECT 'Average Salary'
    UNION ALL
    SELECT 'High Salary'
),
Updated AS (SELECT account_id, income, 
                CASE WHEN income < 20000
                THEN 'Low Salary'
                WHEN income >= 20000 and income <= 50000
                THEN 'Average Salary'
                ELSE 'High Salary'
                END AS category
                FROM Accounts),
CategoryCounts AS (
    SELECT category, COUNT(income) AS accounts_count
    FROM Updated
    GROUP BY category
)
SELECT c.category, COALESCE(c1.accounts_count, 0) AS accounts_count
FROM Categories AS c
LEFT JOIN CategoryCounts AS c1
ON c.category = c1.category
ORDER BY c1.accounts_count DESC;

# WITH Updated AS (
#   SELECT account_id, income,
#     CASE WHEN income > 20000 THEN 'Low Salary'
#          WHEN income >= 20000 AND income <= 50000 THEN 'Average Salary'
#          ELSE 'High Salary'
#     END AS category
#   FROM Accounts
# )
# SELECT *
# FROM (
#   SELECT category, COUNT(income) AS accounts_count
#   FROM Updated
#   GROUP BY category
# ) AS PivotTable
# PIVOT (
#   SUM(accounts_count) FOR category IN ('Low Salary', 'Average Salary', 'High Salary')
# ) AS PivotResult;