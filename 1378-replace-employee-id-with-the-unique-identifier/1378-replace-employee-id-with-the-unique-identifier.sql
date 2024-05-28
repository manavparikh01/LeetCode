# Write your MySQL query statement below
SELECT en.unique_id, E.name 
FROM Employees AS e
LEFT JOIN EmployeeUNI AS en
ON e.id = en.id
