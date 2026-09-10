# Write your MySQL query statement below
select 
    u.name,
    Coalesce(sum(distance),0) as travelled_distance
from users u
Left Join Rides r on
    u.id=r.user_id
group by u.id
order by travelled_distance desc,name;
