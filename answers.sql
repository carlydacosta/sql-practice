-- Problem 1
SELECT * from salespeople

-- Problem 2
SELECT * FROM salespeople WHERE region = 'Northwest'

-- Problem 3
SELECT email from salespeople where region = 'Southwest'

-- Problem 4
SELECT givenname, surname, email FROM salespeople WHERE region = 'Northwest'

-- Problem 5
SELECT common_name FROM melons where price > 5

-- Problem 6
SELECT melon_type, common_name FROM melons WHERE melon_type = 'Watermelon' AND price > 5

-- Problem 7
SELECT common_name FROM melons where common_name LIKE "C%"

-- Problem 8
SELECT common_name FROM melons WHERE common_name LIKE "%Golden%"

-- Problem 9
SELECT distinct region from salespeople

-- Problem 10
SELECT email FROM salespeople WHERE region = 'Northwest' OR region = 'Southwest';

-- Problem 11
SELECT email FROM salespeople WHERE region IN ('Northwest','Southwest')

-- Problem 12
SELECT email, givenname, surname FROM salespeople WHERE region IN ('Northwest', 'Southwest') AND surname LIKE 'M%'

-- Problem 13
SELECT melon_type, common_name, price, price*0.735693 AS Euros FROM melons

-- Problem 14
SELECT COUNT(*) FROM customers

-- Problem 15
SELECT COUNT(*) FROM orders WHERE shipto_state = 'CA'

-- Problem 16
SELECT SUM (order_total) from orders

-- Problem 17
SELECT AVG(order_total) FROM orders

-- Problem 18
SELECT MIN(order_total) FROM orders

-- Problem 19
SELECT id FROM customers WHERE email = 'phyllis@demizz.edu'

-- Problem 20
SELECT id, status, order_total from orders where customer_id= 100

-- Problem 21
SELECT orders.id, orders.status, orders.order_total FROM orders join customers ON (orders.customer_id=customers.id) where email='phyllis@demizz.edu'

-- Problem 22
SELECT orders.id, orders.status, orders.order_total FROM orders join customers ON (orders.customer_id=customers.id) where email='phyllis@demizz.edu'

-- Problem 23
SELECT* from order_items where order_id=2725

-- Problem 24
SELECT common_name, melon_type, quantity, unit_price, total_price FROM melons JOIN order_items ON (melons.id = order_items.melon_id) WHERE order_id = 2725

-- Problem 25
SELECT SUM(order_total) FROM orders where salesperson_id IS NULL

-- Problem 26
SELECT givenname, surname, SUM(order_total), SUM(order_total*0.15) FROM salespeople LEFT JOIN orders ON (orders.salesperson_id=salespeople.id) GROUP BY orders.salesperson_id

