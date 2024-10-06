-- Write query to get number of graded assignments for each student:
SELECT student_id, COUNT(grade) AS Graded_assignment_numbers
FROM assignments
GROUP BY student_id;