# Write your MySQL query statement below
SELECT 
CASE WHEN COUNT(id) = 0 THEN NULL
ELSE MAX(salary)
END AS SecondHighestSalary
FROM Employee
WHERE salary NOT IN (SELECT MAX(salary) FROM Employee)


