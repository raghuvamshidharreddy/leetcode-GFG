# Write your MySQL query statement below
with AMS as(select visited_on,sum(amount) as a
from customer 
group by visited_on)
select visited_on, sum(a) over (order by visited_on rows between 6 preceding and current row) as amount, 
round(avg(a)Over(
        Order by visited_on
        Rows Between 6 preceding and current row ),2) as average_amount
from AMs limit 999 offset 6;