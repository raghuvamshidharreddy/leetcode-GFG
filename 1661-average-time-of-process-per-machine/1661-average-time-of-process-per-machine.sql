WITH st AS (
    SELECT 
        machine_id,
        process_id,
        MIN(timestamp) AS start_time
    FROM activity
    WHERE activity_type = 'start'
    GROUP BY machine_id, process_id
),
en AS (
    SELECT
        machine_id,
        process_id,
        MAX(timestamp) AS end_time
    FROM activity
    WHERE activity_type = 'end'
    GROUP BY machine_id, process_id
)
SELECT 
    e.machine_id,
    round(avg(e.end_time-s.start_time),3)as Processing_time
FROM en e
JOIN st s 
    ON e.machine_id = s.machine_id
   AND e.process_id = s.process_id
group by e.machine_id;
