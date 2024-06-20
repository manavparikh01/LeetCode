# Write your MySQL query statement below
WITH DateActivity AS (SELECT player_id, MIN(event_date) AS event_date
FROM Activity
GROUP BY player_id),
NotThatDate AS (SELECT a.player_id, MIN(a.event_date) AS event_date
FROM Activity AS a
JOIN DateActivity AS d
ON a.player_id = d.player_id AND a.event_date != d.event_date
GROUP BY a.player_id),
ConsecutiveDate AS (SELECT f.player_id
FROM NotThatDate AS f
JOIN DateActivity AS d
ON f.player_id = d.player_id
WHERE f.event_date > d.event_date AND DATEDIFF(f.event_date, d.event_date) = 1)
SELECT ROUND((SELECT COUNT(player_id) FROM ConsecutiveDate) / COUNT(DISTINCT player_id), 2) AS fraction
FROM Activity;
