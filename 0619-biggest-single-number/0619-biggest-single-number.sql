# Write your MySQL query statement below
# WITH SumNumber AS (SELECT num, COUNT(num) as countn
#                   FROM MyNumbers
#                   GROUP BY num
#                   ORDER BY num DESC)
SELECT MAX(num) AS num
FROM MyNumbers
WHERE num NOT IN (SELECT num
                 FROM MyNumbers
                 GROUP BY num
                 HAVING COUNT(num) > 1);