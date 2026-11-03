# Write your MySQL query statement below
select
    user_id,
    Concat(Upper(Substring(name,1,1)),Lower(Substring(name,2))) as name
from Users 
order by user_id;