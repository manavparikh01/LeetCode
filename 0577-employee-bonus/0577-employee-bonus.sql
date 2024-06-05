# Write your MySQL query statement below
SELECT e.name, b.bonus
FROM Employee AS e
LEFT JOIN Bonus AS b
ON e.empId = b.empId
WHERE e.empId not in (SELECT empId FROM Bonus WHERE bonus >= 1000)