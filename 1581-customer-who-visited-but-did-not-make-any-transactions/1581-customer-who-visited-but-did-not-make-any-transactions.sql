# Write your MySQL query statement below
select c.customer_id, count(c.customer_id) as count_no_trans from visits c
left join Transactions t 
on c.visit_id=t.visit_id
where t.visit_id is Null
group by c.customer_id;