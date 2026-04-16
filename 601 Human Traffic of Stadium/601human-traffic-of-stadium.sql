-- Write your PostgreSQL query statement below
SELECT DISTINCT s1.id, s1.visit_date, s1.people
FROM (
    SELECT s.id, s.visit_date, s.people,
    LEAD(s.people, 1) OVER (ORDER BY s.id ASC) AS people_1,
    LEAD(s.people, 2) OVER (ORDER BY s.id ASC) AS people_2,
    LAG(s.people, 1) OVER (ORDER BY s.id ASC) AS people_m1,
    LAG(s.people, 2) OVER (ORDER BY s.id ASC) AS people_m2
    FROM Stadium s
) AS s1
WHERE s1.people >= 100 AND (
    s1.people_1 >= 100 AND s1.people_2 >= 100
    OR s1.people_m1 >= 100 AND s1.people_m2 >= 100
    OR s1.people_1 >= 100 AND s1.people_m1 >= 100
)
ORDER BY s1.visit_date ASC;