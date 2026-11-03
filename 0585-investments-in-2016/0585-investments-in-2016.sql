# Write your MySQL query statement below
SELECT sum(tiv_2016) as tiv_2016
FROM Insurance i
WHERE NOT EXISTS (
    SELECT *
    FROM Insurance j
    WHERE j.lat = i.lat
      AND j.lon = i.lon
    GROUP BY j.lat, j.lon
    HAVING COUNT(*) > 1
);

