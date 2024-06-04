# Write your MySQL query statement below
WITH Processing AS (SELECT a1.machine_id, a1.process_id, (a2.timestamp - a1.timestamp) AS processing_time
FROM Activity AS a2, Activity AS a1
WHERE a1.activity_type = "start" AND a2.activity_type = "end"
AND a1.machine_id = a2.machine_id AND a1.process_id = a2.process_id)
SELECT p.machine_id, ROUND(AVG(p.processing_time),3) AS processing_time
FROM Processing AS p
GROUP BY p.machine_id;
