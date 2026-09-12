# Write your MySQL query statement below
with report as (select 
    reports_to,
    count(reports_to)reports_count,
    round(avg(age))as average_age
from employees
where reports_to is not Null
group by reports_to)
-- 
select r.reports_to as employee_id, 
    e.name,
    r.reports_count,
    r.average_age
From report as r
Join employees e on
r.reports_to=e.employee_id
order by e.employee_id;