# Write your MySQL query statement below
WITH MoviesRated AS (SELECT u.name, m.user_id, COUNT(m.movie_id) AS movies
                    FROM MovieRating AS m
                    LEFT JOIN Users AS u
                    ON m.user_id = u.user_id
                    GROUP BY m.user_id
                    ORDER BY movies DESC, u.name
                    LIMIT 1),
UsersRated AS (SELECT m.title, r.movie_id, AVG(r.rating) AS ratingavg
              FROM MovieRating AS r
              LEFT JOIN Movies AS m
              ON r.movie_id = m.movie_id
              WHERE MONTH(r.created_At) = 2 AND YEAR(r.created_at) = 2020
              GROUP BY r.movie_id
              ORDER BY ratingavg DESC, m.title
              LIMIT 1)
SELECT name AS results
FROM MoviesRated
UNION ALL
SELECT title AS results
FROM UsersRated;

# SELECT m.title, r.movie_id, AVG(m.rating)
