# Write your MySQL query statement below
select 
id,visit_date,people
from
(select 
    id,
    visit_date,
    people,
    id-rn,
    count(*) over(partition by id-rn) as ans
from
(select *,row_number() over() as rn from 
stadium where people>=100) t) t1
where ans>=3
order by visit_date;
