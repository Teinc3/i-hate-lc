-- Write your PostgreSQL query statement below
SELECT t.request_at AS Day,
ROUND(1.00 * COUNT(CASE t.status WHEN 'completed' then null else 1 END) / COUNT(*), 2) AS "Cancellation Rate"
FROM Trips t
INNER JOIN Users u1
ON t.client_id = u1.users_id
INNER JOIN Users u2
ON t.driver_id = u2.users_id
WHERE u1.banned = 'No' AND u2.banned = 'No'
AND t.request_at IN ('2013-10-01', '2013-10-02', '2013-10-03')
GROUP BY t.request_at;
