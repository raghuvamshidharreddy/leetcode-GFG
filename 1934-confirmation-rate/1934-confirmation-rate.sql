# Write your MySQL query statement below
select user_id,0 as confirmation_rate from signups  
where user_id not in (select distinct user_id from confirmations)
union
select 
    s.user_id,
    round(coalesce(count(case when action='confirmed' then s.user_id end),0)/coalesce(count(s.user_id),1),2) as confirmation_rate
from signups s
join confirmations c on
s.user_id=c.user_id
group by s.user_id;