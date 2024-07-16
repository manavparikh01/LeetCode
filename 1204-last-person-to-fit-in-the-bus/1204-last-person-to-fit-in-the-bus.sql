# Write your MySQL query statement below
# SELECT turn, person_id, person_name, weight, (SELECT SUM(weight)
#                                              FROM Queue AS q1
#                                               JOIN Queue AS q2
#                                               ON q1.turn = q2.turn
#                                              WHERE q2.turn < q1.turn)
# FROM Queue
# ORDER BY turn;

# SELECT SUM(weight) AS total_weight
# FROM Queue
# WHERE turn = 1 or turn = 2
# ORDER BY turn;

WITH Cumulative AS (SELECT *, SUM(Weight) OVER (ORDER BY Turn) AS TotalWeight
  FROM Queue)
SELECT person_name
FROM Cumulative
WHERE TotalWeight <= 1000
ORDER BY turn DESC
LIMIT 1;