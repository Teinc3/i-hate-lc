-- Write your PostgreSQL query statement below
SELECT session_id,
    user_id,
    EXTRACT(EPOCH FROM last_timestamp - first_timestamp) / 60 AS session_duration_minutes, 
    scroll_count
FROM (
    SELECT session_id, user_id, 
        MIN(event_timestamp) AS first_timestamp,
        MAX(event_timestamp) AS last_timestamp,
        COUNT(CASE WHEN event_type = 'scroll' THEN 1 END) AS scroll_count,
        COUNT(CASE WHEN event_type = 'click' THEN 1 END) AS click_count,
        COUNT(CASE WHEN event_type = 'purchase' THEN 1 END) AS purchase_count
    FROM app_events
    GROUP BY session_id, user_id
)
WHERE last_timestamp - first_timestamp > INTERVAL '30 minutes'
    AND scroll_count >= 5
    AND 5 * click_count < scroll_count
    AND purchase_count = 0
ORDER BY scroll_count DESC, session_id ASC;