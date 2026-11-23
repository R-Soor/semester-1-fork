.headers on
.mode column

-- Write your sql for each task here - you can use comment (start with --) to add notes or number them. Remember your ; at the end of each query!
-- with multiple queries in the file, sql will run then one after the other and print them all out, so I recommend testing after each one.

-- To see all the tables in a database
.tables

-- To see the attributes belonging to each table
.schema customers

-- And to see a count of the total number of tuples
SELECT COUNT(*) as Cardinality FROM customers; 

SELECT COUNT(*) as Customers FROM customers;
SELECT COUNT(*) as Drivers FROM drivers;
SELECT COUNT(*) as Menu_items FROM menu_items;
SELECT COUNT(*) as Order_items FROM order_items;
SELECT COUNT(*) as Orders FROM orders;
SELECT COUNT(*) as Restaurants FROM restaurants;
SELECT COUNT(*) as Reviews FROM reviews;