# Write your MySQL query statement below
with t as(select 
id,
student,
lag(student) over(order by id) as Lag1,
lead(student) over(order by id) as Lead1,
max(id) over() as m
from Seat)
select id,(case when id%2=0 then Lag1 when id%2!=0 and id=m then student else Lead1 end) as student from t;