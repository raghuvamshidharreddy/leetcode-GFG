# Write your MySQL query statement below
SELECT p.product_name,s.Year,s.price from 
Sales s
Join Product p
on s.product_id=p.product_id;