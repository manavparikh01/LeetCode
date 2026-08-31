# Write your MySQL query statement below
SELECT p1.name AS Employee FROM Employee p1
JOIN Employee p2
ON p1.managerId = p2.id
WHERE p1.salary > p2.salary