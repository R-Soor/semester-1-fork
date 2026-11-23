.headers on
.mode column

-- Write your sql for each task here - you can use comment (start with --) to add notes or number them. Remember your ; at the end of each query!
-- with multiple queries in the file, sql will run then one after the other and print them all out, so I recommend testing after each one.


SELECT name, price FROM menu_items 
WHERE is_vegetarian=TRUE AND price<8 
ORDER BY price LIMIT 10;

SELECT name, postcode, order_time FROM orders, customers
WHERE orders.customer_id=customers.customer_id AND status='placed' AND order_time LIKE '%-10-%';