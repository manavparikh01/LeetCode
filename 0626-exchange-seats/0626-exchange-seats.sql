# Write your MySQL query statement below
# SELECT id, CASE WHEN id%2=0 THEN (SELECT student FROM Seat WHERE id = id-1)
# ELSE "HEHE" END AS student
# FROM Seat;
WITH RowCount AS (
    SELECT COUNT(*) AS cnt
    FROM Seat
),
LastRow AS (
    SELECT *
    FROM Seat
    ORDER BY id DESC -- Replace 'some_column' with the column you want to order by
    LIMIT 1
)
SELECT s2.id, s1.student
FROM Seat AS s1
JOIN Seat AS s2
ON CASE WHEN s1.id % 2 = 1
THEN s1.id = s2.id - 1
ELSE s1.id - 1 = s2.id
END

UNION

# SELECT id, student
# FROM Seat
# ORDER BY id DESC
# LIMIT 

# WITH RowCount AS (
#     SELECT COUNT(*) AS cnt
#     FROM Seat
# ),
# LastRow AS (
#     SELECT *
#     FROM Seat
#     ORDER BY id DESC -- Replace 'some_column' with the column you want to order by
#     LIMIT 1
# )
SELECT *
FROM LastRow
WHERE (SELECT cnt FROM RowCount) % 2 = 1;




# UNION

# SELECT s2.id, s1.student
# FROM Seat AS s1
# JOIN Seat AS s2
# ON s1.id - 1 = s2.id
# WHERE s2.id % 2 = 1;