# Write your MySQL query statement below
SELECT e1.reports_to AS employee_id, e2.name AS name, COUNT(e1.employee_id) AS reports_count, ROUND(AVG(e1.age)) AS average_age
FROM Employees AS e1
JOIN Employees AS e2
ON e1.reports_to = e2.employee_id
GROUP BY e1.reports_to
ORDER BY e1.reports_to;