# Write your MySQL query statement below
WITH Requester As (SELECT requester_id AS id, COUNT(accepter_id) AS accept
FROM RequestAccepted
GROUP BY requester_id),
Accepter AS (SELECT accepter_id AS id, COUNT(requester_id) AS request
FROM RequestAccepted
GROUP BY accepter_id),
Allinone AS (SELECT id, accept AS num FROM Requester
            UNION ALL
            SELECT id, request AS num FROM Accepter)
SELECT id, SUM(num) AS num
FROM Allinone
GROUP BY id
ORDER BY num DESC
LIMIT 1;
            

# SELECT r.id, (r.accept + q.request) AS num
# FROM Requester AS r
# CROSS JOIN Accepter AS q
# ON r.id = q.id
# ORDER BY num DESC
# LIMIT 1;
