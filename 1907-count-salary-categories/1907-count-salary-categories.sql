# Write your MySQL query statement below
select 'Low Salary' as category,count(account_id) as accounts_count from  accounts where income<20000
Union 
Select 'Average Salary',count(account_id) from accounts where income between 20000 and 50000
Union
Select 'High Salary',count(account_id) from accounts where income >50000; 