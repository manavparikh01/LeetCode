# Write your MySQL query statement below
SELECT e.name, b.bonus FROM Employee e
LEFT JOIN Bonus b
ON e.empId = b.empId
WHERE e.empId NOT IN (SELECT empId FROM Bonus WHERE bonus >= 1000)