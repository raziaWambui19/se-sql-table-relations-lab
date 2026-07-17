# STEP 0

# SQL Library and Pandas Library
import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('data.sqlite')

pd.read_sql("""SELECT * FROM sqlite_master""", conn)

# STEP 1
# Replace None with your code
df_boston = pd.read_sql( """
SELECT lastName, firstName, jobTitle
FROM employees
INNER JOIN offices
ON employees.officeCode = offices.officeCode
WHERE offices.city = 'Boston';
""" ,conn
)
# STEP 2
# Replace None with your code
df_zero_emp = pd.read_sql("""
SELECT offices.officeCode, offices.city
FROM offices
LEFT JOIN employees
ON offices.officeCode = employees.officeCode
WHERE employees.employeeNumber is NULL; 
""" ,conn)

# STEP 3
# Replace None with your code
df_employee = pd.read_sql("""
SELECT firstName, lastName, city ,state
FROM employees
LEFT JOIN offices
ON  employees.officeCode = offices.officeCode
ORDER BY firstName, LastName;
""" ,conn
)
# STEP 4
# Replace None with your code
df_contacts = pd.read_sql("""
SELECT contactFirstName, contactLastName, phone, salesRepEmployeeNumber
FROM customers
LEFT JOIN orders
ON customers.customerNumber = orders.customerNumber
WHERE orders.orderNumber IS NULL
ORDER BY contactLastName;
""" ,conn)

# STEP 5
# Replace None with your code
df_payment = pd.read_sql("""
SELECT contactFirstName, contactLastName, amount, paymentDate
FROM customers
INNER JOIN payments
ON customers.customerNumber = payments.customerNumber
ORDER BY CAST(payments.amount AS REAL) DESC;
""" ,conn)

# STEP 6
# Replace None with your code
df_credit =pd.read_sql( """
SELECT employeeNumber, firstName, lastName, COUNT(customers.customerNumber) AS numberOfCustomers
FROM employees
INNER JOIN customers
ON employees.employeeNumber = customers.salesRepEmployeeNumber
GROUP BY employees.employeeNumber, employees.firstName, employees.lastName
HAVING AVG(customers.creditLimit) > 90000
ORDER BY numberOfCustomers DESC;
""" ,conn )

# STEP 7
# Replace None with your code
df_product_sold = pd.read_sql("""
SELECT products.productName,
       COUNT (orderdetails.orderNumber) AS numorders,
       SUM (orderdetails.quantityOrdered) AS totalunits
FROM products
INNER JOIN orderdetails
On products.productCode = orderdetails.productCode
GROUP BY products.productName
ORDER BY totalunits DESC;
 """ ,conn) 

# STEP 8
# Replace None with your code
df_total_customers = pd.read_sql("""
SELECT products.productName, products.productCode, COUNT(orders.customerNumber) AS numpurchasers
FROM products
INNER JOIN orderdetails
ON products.productCode = orderdetails.productCode
INNER JOIN orders
ON orderdetails.orderNumber = orders.orderNumber
GROUP BY products.productName, products.productCode
ORDER BY numpurchasers DESC;
""" ,conn)

# STEP 9
# Replace None with your code
df_customers = pd.read_sql("""
SELECT offices.officeCode, offices.city, COUNT (customers.customerNumber) AS n_customers
FROM offices
LEFT JOIN employees
ON offices.officeCode = employees.officeCode
LEFT JOIN customers
On employees.employeeNumber = customers.salesRepEmployeeNumber

GROUP BY  offices.officeCode, offices.city;

""" ,conn)

# STEP 10
# Replace None with your code
df_under_20 = pd.read_sql("""
SELECT DISTINCT e.employeeNumber, e.firstName, e.lastName, o.city, o.officeCode
FROM employees e
INNER JOIN offices o
ON e.officeCode = o.officeCode
INNER JOIN customers c
ON e.employeeNumber = c.salesRepEmployeeNumber
INNER JOIN orders ord
ON c.customerNumber = ord.orderNumber
INNER JOIN orderdetails od
ON ord.orderNumber = od.orderNumber
WHERE od.productCode IN ( 
     SELECT od.productCode
     FROM orderdetails od
     INNER JOIN orders ord
        ON od.orderNumber = ord.orderNumber
    GROUP BY od.productcode
    HAVING COUNT(DISTINCT ord.customerNumber) < 20
);
""" ,conn)

conn.close()