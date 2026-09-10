# Write your MySQL query statement below
with b as(select stock_name,
 sum(price) as p
from stocks
where operation='Buy'
group by stock_name),
s as(
    select stock_name,
 sum(price) as p
from stocks
where operation='Sell'
group by stock_name
)
select s.stock_name,
s.p-b.p as capital_gain_loss
from b join s on
b.stock_name=s.stock_name
;