### QUESTION:

* Question 1: Which products should we order more of or less of?
* Question 2: How should we tailor marketing and communication strategies to customer behaviors?
* Question 3: How much can we spend on acquiring new customers?

![Diagram](https://user-images.githubusercontent.com/21137726/150624324-9d170437-1cf5-4873-84e0-202a1b5957c7.png)

### 1. Which Products Should We Order More of or Less of?
 
This question refers to inventory reports, including low stock and product performance. This will optimize the supply and the user experience by preventing the best-selling products from going out-of-stock.
 
* The low stock represents the quantity of each product sold divided by the quantity of product in stock. We can consider the ten lowest rates. These will be the top ten products that are (almost) out-of-stock.
* The product performance represents the sum of sales per product.
* Priority products for restocking are those with high product performance that are on the brink of being out of stock.

![Diagram_2](https://user-images.githubusercontent.com/21137726/150624370-aa57cfa4-ff10-47c9-b647-e731ea0f4805.png)

#### Low stock:
```
product _code	low_stock
S18_1984	0.09
S24_3432	0.09
S12_2823	0.1
S12_3380	0.1
S18_1589	0.1
S18_2325	0.1
S18_2870	0.1
S18_3482	0.1
S32_2206	0.1
S700_2466	0.1
```
#### Product performance:
```
product_code	performance
S18_3232	276839.98
S12_1108	190755.86
S10_1949	190017.96
S10_4698	170686.0
S12_1099	161531.48
S12_3891	152543.02
S18_1662	144959.91
S18_2238	142530.63
S18_1749	140535.6
S12_2823	135767.03
```
#### Product priority:
```
product_code	product_name				name	type		performance
S12_2823	2002 Suzuki XREO			Motorcycles		135767.03
S18_3482	1976 Ford Gran Torino			Classic Cars		121890.6
S18_1984	1995 Honda Civic			Classic Cars		119050.95
S18_2325	1932 Model A Ford J-Coupe		Vintage Cars		109992.01
S18_1589	1965 Aston Martin DB5			Classic Cars		101778.13
S18_2870	1999 Indy 500 Monte Carlo SS		Classic Cars		100770.12
S12_3380	1968 Dodge Charger			Classic Cars		98718.76
S700_2466	America West Airlines B757-200		Planes			89347.8
S24_3432	2002 Chevy Corvette			Classic Cars		87404.81
S32_2206	1982 Ducati 996 R			Motorcycles		33268.76
```

### 2. How Should We Match Marketing and Communication Strategies to Customer Behavior?

This involves categorizing customers: finding the VIP (very important person) customers and those who are less engaged.

* VIP customers bring in the most profit for the store.
* Less-engaged customers bring in less profit.

For example, we could organize some events to drive loyalty for the VIPs and launch a campaign for the less engaged.

![Diagram_3](https://user-images.githubusercontent.com/21137726/150624424-0c3e8814-7d9f-44e8-8687-0db7a107eb46.png)

**3. How Much Can We Spend on Acquiring New Customers?**

Before answer the third question, we can find the number of new customers arriving each month. That way we can check if it's worth spending money on acquiring new customers.

To determine how much money we can spend acquiring new customers, we can compute the Customer Lifetime Value (LTV), which represents the average amount of money a customer generates. We can then determine how much we can spend on marketing.

**CONCLUSION:**

* **Question 1: Which products should we order more of or less of?**

The query shows product types like classic cars are our priority due to its low stocks, especially product S12_2823 represents 2002 Suzuki XERO as one of top ten product performance.

* **Question 2: How should we tailor marketing and communication strategies to customer behaviors?**

After generating how much profit each customer generates, we start to categorize them into top five VIP customers and top five least-engaged customers. We could organize some events to drive loyalty for the VIPs and launch a campaign for the less engaged.

* **Question 3: How much can we spend on acquiring new customers?**

We can compute the Customer Lifetime Value (LTV), which represents the average amount of money a customer generates. From this data, we earn 39039.59 dollars from the customer.
