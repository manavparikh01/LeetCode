# Write your MySQL query statement below
# WITH Updated AS (SELECT p2.id AS id
#             FROM Person AS p1
#             CROSS JOIN Person AS p2
#             WHERE p1.email = p2.email AND p1.id < p2.id)
# DELETE FROM Person
# WHERE id LIKE Updated;

# SELECT p2.id AS id
#             FROM Person AS p1
#             CROSS JOIN Person AS p2
#             WHERE p1.email = p2.email AND p1.id < p2.id

DELETE p1 FROM Person p1
INNER JOIN Person p2
ON p1.email = p2.email
WHERE p1.id > p2.id;