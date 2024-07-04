# Write your MySQL query statement below
WITH Temp1 AS (SELECT employee_id, department_id
              FROM Employee
              GROUP BY employee_id
              HAVING COUNT(department_id) = 1),
Temp2 AS (SELECT employee_id, department_id
         FROM Employee
         WHERE primary_flag = 'Y')
SELECT employee_id, department_id
FROM Temp1
UNION
SELECT employee_id, department_id
FROM Temp2;

# SELECT employee_id, department_id
# FROM Employee
# GROUP BY employee_id
# HAVING COUNT(department_id) = 1;
