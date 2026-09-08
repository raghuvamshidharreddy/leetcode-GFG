# Write your MySQL query statement below
with reqcount as(
select requester_id,count(requester_id) as a
from RequestAccepted
group by requester_id
), acccount as(
select accepter_id,count(accepter_id) as b
from RequestAccepted
group by accepter_id
), temp as(
select accepter_id,b as num from acccount
union all
select requester_id,a  from reqcount)
select accepter_id as id,sum(num) as num from temp
group by id order by num desc limit 1;