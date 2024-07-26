# Write your MySQL query statement below
# WITH Samelatlon AS (SELECT i1.pid
# FROM Insurance AS i1
# JOIN Insurance AS i2
# WHERE i1.pid != i2.pid AND i1.lat = i2.lat AND i1.lon = i2.lon)
SELECT COALESCE(ROUND(SUM(tiv_2016),2), null) AS tiv_2016
FROM Insurance
WHERE pid IN (SELECT DISTINCT i1.pid
            FROM Insurance AS i1
            JOIN Insurance AS i2
            WHERE i1.pid != i2.pid AND (i1.lat != i2.lat OR i1.lon != i2.lon) AND i1.tiv_2015 = i2.tiv_2015 AND i1.pid NOT IN (SELECT i1.pid
FROM Insurance AS i1
JOIN Insurance AS i2
WHERE i1.pid != i2.pid AND i1.lat = i2.lat AND i1.lon = i2.lon));


# SELECT DISTINCT i1.pid
# FROM Insurance AS i1
# JOIN Insurance AS i2
# WHERE i1.pid != i2.pid AND i1.lat != i2.lat AND i1.lon != i2.lon AND i1.tiv_2015 = i2.tiv_2015;