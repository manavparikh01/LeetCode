# Write your MySQL query statement below
# SELECT class
# FROM Courses
# WHERE 
# GROUP BY class
# HAVING COUNT(student) >= 5;

WITH StudentCount AS (SELECT class, COUNT(student) as counts
                     FROM Courses
                     GROUP BY class)
SELECT class
FROM StudentCount
WHERE counts >= 5;