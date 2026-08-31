# Write your MySQL query statement below
WITH combined AS (SELECT d.name AS Department, e.name AS Employee, e.salary AS Salary, DENSE_RANK() OVER (PARTITION BY e.departmentId ORDER BY e.salary DESC) as dense_salary_rank FROM Employee AS e
JOIN Department AS d ON e.departmentId = d.id)
SELECT Department, Employee, Salary
FROM combined
WHERE dense_salary_rank <= 3
