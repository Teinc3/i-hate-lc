-- Write your PostgreSQL query statement below
SELECT student_id, subject, first_score, latest_score
FROM (
    SELECT DISTINCT ON (s1.student_id, s1.subject)
        s1.student_id, s1.subject, 
        s1.score AS first_score, s2.score as latest_score,
        s1.exam_date AS first_date, s2.exam_date AS latest_date
    FROM Scores s1
    INNER JOIN Scores s2
    ON s1.student_id = s2.student_id AND s2.subject = s1.subject AND s2.exam_date > s1.exam_date
    ORDER BY s1.student_id ASC, s1.subject ASC, s2.exam_date DESC, s1.exam_date ASC
)
WHERE first_score < latest_score
ORDER BY student_id, subject;