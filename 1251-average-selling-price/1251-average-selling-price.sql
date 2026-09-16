# Write your MySQL query statement below
select product_id,Coalesce(round(sum(total_price)/sum(units),2),0) as average_price from 
(select p.product_id,p.price,s.units,(price*units)as total_price from prices p
left Join UnitsSold s on
s.purchase_date>=p.start_date and s.purchase_date<=p.end_date and s.product_id=p.product_id
order by product_id) t
group by product_id;