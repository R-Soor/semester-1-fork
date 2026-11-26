.headers on
.mode column

-- add tasks below
-- sqlite3 database_file.db to open the database
-- .read sql_file.sql to run the queries
BEGIN;
INSERT INTO orders (order_id, customer_id, restaurant_id)
VALUES (5001, 12, 3);
INSERT INTO order_items (order_id, item_id, quantity)
VALUES (5001, 87, 2);
COMMIT;