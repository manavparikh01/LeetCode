# Write your MySQL query statement below
SELECT w2.id
FROM Weather AS w2
WHERE w2.temperature > (SELECT w1.temperature 
                    FROM Weather AS w1
                       WHERE w1.recordDate = DATE_SUB(w2.recordDate, INTERVAL 1 DAY));