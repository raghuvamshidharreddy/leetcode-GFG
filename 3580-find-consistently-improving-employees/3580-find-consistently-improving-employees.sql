# Write your MySQL query statement below
with t as(select 
    e.employee_id,
    e.name,
    p.review_date,
    p.rating,
    row_number() over(partition by employee_id order by review_date desc) rn
From employees e
Join performance_reviews p on
e.employee_id=p.employee_id)
,t1 as(select 
* from t where rn=1 )
,t2 as(select * from t where rn=2 )
,t3 as(select * from t where rn=3)
    
select t3.employee_id,t3.name,t1.rating-t3.rating improvement_score
from t1 join t2 on
t1.employee_id=t2.employee_id and t1.rating>t2.rating
join t3 on
t2.employee_id=t3.employee_id  and t2.rating>t3.rating
where t1.rating-t2.rating
order by improvement_score desc,t1.name
;