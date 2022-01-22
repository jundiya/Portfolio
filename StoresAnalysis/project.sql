-- Low stock
SELECT a.productCode, ROUND(SUM(a.quantityOrdered)*1.0/b.quantityInStock,2) AS low_stock
  FROM orderdetails AS a
  JOIN products AS b
    ON a.productCode = b.productCode
 GROUP BY a.productCode
 ORDER BY low_stock
 LIMIT 10
 
-- Product performance
SELECT productCode AS product_code, SUM(quantityOrdered * priceEach) AS performance
  FROM orderdetails
 GROUP BY productCode
 ORDER BY performance DESC
 LIMIT 10
 
-- Product prioritize using CTE
WITH
product_low_stock AS (
SELECT a.productCode, ROUND(SUM(a.quantityOrdered)*1.0/b.quantityInStock,2) AS low_stock
  FROM orderdetails AS a
  JOIN products AS b
    ON a.productCode = b.productCode
 GROUP BY a.productCode
 ORDER BY low_stock
 LIMIT 10
),
product_performance AS (
SELECT productCode, SUM(quantityOrdered * priceEach) AS performance
  FROM orderdetails
 GROUP BY productCode
 ORDER BY performance DESC
)

SELECT a.productCode AS product_code, productName AS product_name, productLine AS type, c.performance
  FROM products AS a
  JOIN product_low_stock AS b
    ON a.productCode = b.productCode
  JOIN product_performance AS c
    ON b.productCode = c.productCode
 ORDER BY performance DESC;

-- Category of customers using CTE
WITH
profit AS (
SELECT customerNumber, SUM(quantityOrdered * (priceEach - buyPrice)) AS profit
  FROM orders AS a
  JOIN orderdetails AS b
    ON a.orderNumber = b.orderNumber
  JOIN products AS c
    ON b.productCode = c.productCode
 GROUP BY customerNumber
 ORDER BY profit DESC
)

SELECT contactLastName AS last_name, contactFirstName AS first_name, city, country, profit
  FROM customers AS d
  JOIN profit AS e
    ON d.customerNumber = e.customerNumber
 ORDER BY profit DESC
 LIMIT 5;

-- Number of new customers arriving each month
WITH
payment_with_year_month_table AS (
SELECT *, CAST(SUBSTR(paymentDate, 1,4) AS INTEGER)*100 + CAST(SUBSTR(paymentDate, 6,7) AS INTEGER) AS year_month
  FROM payments p
),
customers_by_month_table AS (
SELECT p1.year_month, COUNT(*) AS number_of_customers, SUM(p1.amount) AS total
  FROM payment_with_year_month_table p1
 GROUP BY p1.year_month
),
new_customers_by_month_table AS (
SELECT p1.year_month, COUNT(*) AS number_of_new_customers, SUM(p1.amount) AS new_customer_total,
      (SELECT number_of_customers
         FROM customers_by_month_table c
        WHERE c.year_month = p1.year_month) AS number_of_customers,
      (SELECT total
         FROM customers_by_month_table c
        WHERE c.year_month = p1.year_month) AS total
  FROM payment_with_year_month_table p1
 WHERE p1.customerNumber NOT IN (SELECT customerNumber
                                   FROM payment_with_year_month_table p2
                                  WHERE p2.year_month < p1.year_month)
 GROUP BY p1.year_month
)

SELECT year_month,
      ROUND(number_of_new_customers*100/number_of_customers,1) AS number_of_new_customers_props,
      ROUND(new_customer_total*100/total,1) AS new_customers_total_props
  FROM new_customers_by_month_table;
  
--LTV
WITH
customer_profit AS (
SELECT customerNumber AS customer_number, SUM(quantityOrdered * (priceEach - buyPrice)) AS profit
  FROM orders AS a
  JOIN orderdetails AS b
    ON a.orderNumber = b.orderNumber
  JOIN products AS c
    ON b.productCode = c.productCode
 GROUP BY customerNumber
 ORDER BY profit DESC
)

SELECT AVG(profit) AS LTV
  FROM customer_profit;
