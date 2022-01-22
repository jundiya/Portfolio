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
