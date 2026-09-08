WITH temp AS (
    SELECT product_id, new_price, change_date
    FROM products
    WHERE change_date <= '2019-08-16'
),
idn AS (
    SELECT product_id
    FROM products
    WHERE product_id NOT IN (
        SELECT product_id
        FROM temp
    )
),
t AS (
    SELECT product_id,
           new_price AS price
    FROM (
        SELECT product_id,
               new_price,
               change_date,
               ROW_NUMBER() OVER (PARTITION BY product_id ORDER BY change_date DESC) AS rn
        FROM temp
    ) x
    WHERE rn = 1
)
SELECT product_id, price
FROM t
UNION
SELECT product_id, 10
FROM idn
ORDER BY price DESC;
