-- Write your PostgreSQL query statement below
SELECT s1.id,
(CASE WHEN  s2.student IS NULL THEN s1.student ELSE s2.student END)
FROM Seat s1
LEFT JOIN Seat s2
ON (
    s1.id % 2 = 1 AND s1.id + 1 = s2.id
    OR s1.id % 2 = 0 AND s1.id - 1 = s2.id
)