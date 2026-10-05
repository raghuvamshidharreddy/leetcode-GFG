# Write your MySQL query statement below
select person_name
from 
(select person_name,
SUM(weight) OVER (ORDER BY turn) AS t
from queue) t
where t<=1000
order by t desc limit 1;