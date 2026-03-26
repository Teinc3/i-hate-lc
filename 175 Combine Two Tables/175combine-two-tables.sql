-- Write your PostgreSQL query statement below
SELECT p.firstName as firstName, p.lastName as lastName, a.city, a.state
FROM Person AS p
LEFT JOIN Address AS a
ON p.personId = a.personId