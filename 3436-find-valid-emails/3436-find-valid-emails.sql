SELECT user_id, email
FROM users
WHERE email REGEXP '^[a-zA-Z0-9]+@[a-zA-Z]+\\.com$'
order by user_id;
