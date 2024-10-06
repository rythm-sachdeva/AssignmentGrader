-- Write query to find the number of grade A's given by the teacher who has graded the most assignments
SELECT COUNT(id) AS number_of_A_grades
FROM assignments
WHERE teacher_id = (
    SELECT teacher_id
    FROM (
        SELECT teacher_id, COUNT(id) AS Assignment_count
        FROM assignments
        GROUP BY teacher_id
        ORDER BY Assignment_count DESC
        LIMIT 1
    ) AS top_teacher 
)  AND grade = 'A';
