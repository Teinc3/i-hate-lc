-- Write your PostgreSQL query statement below
SELECT results FROM (
    SELECT u.name AS results, COUNT(*) AS metric
    FROM MovieRating r
    INNER JOIN Users u
    ON r.user_id = u.user_id
    GROUP BY results
    ORDER BY metric DESC, results ASC
    LIMIT 1
) UNION ALL SELECT results FROM (
    SELECT m.title AS results, AVG(rating) AS metric
    FROM MovieRating r
    INNER JOIN Movies m
    ON r.movie_id = m.movie_id
    WHERE r.created_at BETWEEN '2020-02-01' AND '2020-02-29'
    GROUP BY results
    ORDER BY metric DESC, results ASC
    LIMIT 1
);