-- Write your PostgreSQL query statement below
DELETE FROM Person p1
WHERE EXISTS (
    SELECT 1
    FROM Person p2
    WHERE p1.id > p2.id and p1.email = p2.email
)
