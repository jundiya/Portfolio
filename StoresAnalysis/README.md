**QUESTION:**

* Question 1: Which products should we order more of or less of?
* Question 2: How should we tailor marketing and communication strategies to customer behaviors?
* Question 3: How much can we spend on acquiring new customers?

![Diagram](https://user-images.githubusercontent.com/21137726/150624324-9d170437-1cf5-4873-84e0-202a1b5957c7.png)

**1. Which Products Should We Order More of or Less of?**
 
This question refers to inventory reports, including low stock and product performance. This will optimize the supply and the user experience by preventing the best-selling products from going out-of-stock.
 
* The low stock represents the quantity of each product sold divided by the quantity of product in stock. We can consider the ten lowest rates. These will be the top ten products that are (almost) out-of-stock.
* The product performance represents the sum of sales per product.
* Priority products for restocking are those with high product performance that are on the brink of being out of stock.
 
low_stock = SUM(**orderdetails**.quantityOrdered) / **products**.quantityInStock
 
product_performance = SUM(**orderdetails**.quantityOrdered * **orderdetails**.priceEach)

![Diagram_2](https://user-images.githubusercontent.com/21137726/150624370-aa57cfa4-ff10-47c9-b647-e731ea0f4805.png)

**2. How Should We Match Marketing and Communication Strategies to Customer Behavior?**

This involves categorizing customers: finding the VIP (very important person) customers and those who are less engaged.

* VIP customers bring in the most profit for the store.
* Less-engaged customers bring in less profit.

For example, we could organize some events to drive loyalty for the VIPs and launch a campaign for the less engaged.

![Diagram_3](https://user-images.githubusercontent.com/21137726/150624424-0c3e8814-7d9f-44e8-8687-0db7a107eb46.png)

**3. How Much Can We Spend on Acquiring New Customers?**

Before answer the third question, we can find the number of new customers arriving each month. That way we can check if it's worth spending money on acquiring new customers.

To determine how much money we can spend acquiring new customers, we can compute the Customer Lifetime Value (LTV), which represents the average amount of money a customer generates. We can then determine how much we can spend on marketing.

**CONCLUSION:**

* Question 1: Which products should we order more of or less of?

The query shows product types like classic cars are our priority due to its low stocks, especially product S12_2823 represents 2002 Suzuki XERO as one of top ten product performance.

* Question 2: How should we tailor marketing and communication strategies to customer behaviors?

After generating how much profit each customer generates, we start to categorize them into top five VIP customers and top five least-engaged customers. We could organize some events to drive loyalty for the VIPs and launch a campaign for the less engaged.

* Question 3: How much can we spend on acquiring new customers?

We can compute the Customer Lifetime Value (LTV), which represents the average amount of money a customer generates. From this data, we earn 39039.59 dollars from the customer.
