# Write your MySQL query statement below
WITH logged_date AS (SELECT player_id, MIN(event_date) as min_event_date FROM Activity
GROUP BY player_id),
not_loggin_date AS (SELECT a1.player_id, MIN(a1.event_date) as sec_event_date FROM Activity a1
JOIN logged_date l1 ON l1.player_id = a1.player_id AND l1.min_event_date != a1.event_date
GROUP BY a1.player_id),
logged_again AS (SELECT l1.player_id FROM logged_date l1
JOIN not_loggin_date as l2 ON l1.player_id = l2.player_id
WHERE DATEDIFF(l2.sec_event_date, l1.min_event_date) = 1)
-- SELECT COUNT(DISTINCT player_id) FROM Activity
SELECT ROUND((SELECT COUNT(player_id) from logged_again) / (SELECT COUNT(DISTINCT player_id) FROM Activity), 2) AS fraction