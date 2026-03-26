-- Write your PostgreSQL query statement below
SELECT c.name as Customers
FROM Customers c
WHERE (
    SELECT COUNT(*)
    FROM Orders o
    WHERE c.id = o.customerId
) = 0;
