-- Write your MySQL query statement below
WITH cod AS (
    SELECT 
        customer_id, 
        MIN(order_date) AS od,
        MIN(customer_pref_delivery_date) AS dd
    FROM delivery
    GROUP BY customer_id
)
SELECT 
    ROUND(AVG(dd = od) * 100, 2) AS immediate_percentage
FROM cod;
