# Write your MySQL query statement below
WITH highest_salary AS (SELECT e.departmentId, MAX(e.salary) as max_salary, d.name
FROM Employee e
JOIN Department d
ON e.departmentId = D.id
GROUP BY e.departmentId)
SELECT h.name AS Department, e.name AS Employee, e.salary AS Salary
FROM highest_salary h
JOIN Employee e
ON h.departmentId = e.departmentId AND h.max_salary = e.salary