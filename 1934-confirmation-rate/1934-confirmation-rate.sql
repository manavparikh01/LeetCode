# Write your MySQL query statement below
# WITH TotalMe AS (SELECT user_id, COUNT(action) AS totalme
# FROM Confirmations
# GROUP BY user_id),
# TotalConf AS (SELECT user_id, COUNT(action) AS totalcon
# FROM Confirmations
# WHERE action = 'confirmed'
# GROUP BY user_id, action),


WITH Con AS (SELECT s.user_id, c.action
FROM Signups AS s
LEFT JOIN Confirmations AS c
ON s.user_id = c.user_id),
TotalMe AS (SELECT user_id, COUNT(action) AS totalme
FROM Con
GROUP BY user_id),
TotalCon AS (SELECT user_id, COUNT(action) AS totalcon
FROM Con
WHERE action = 'confirmed'
GROUP BY user_id, action)
SELECT tm.user_id, ROUND(IFNULL(tc.totalcon, 0.00) * 1.00/IF(tm.totalme = 0, 1.00, tm.totalme), 2) AS confirmation_rate
FROM TotalMe AS tm
LEFT JOIN TotalCon AS tc
ON tm.user_id = tc.user_id