# Write your MySQL query statement below
SELECT DISTINCT l1.num AS ConsecutiveNums
FROM Logs AS l1
JOIN Logs AS l2 ON l1.num = l2.num
JOIN Logs AS l3 ON l2.num = l3.num
WHERE l1.id + 1 = l2.id AND l2.id + 1 = l3.id;