# Write your MySQL query statement below
select * from (select 
    u.name,
    sum(t.amount) as balance
From Users as u
Join transactions t on 
u.account=t.account
group by t.account) t
where balance>10000;