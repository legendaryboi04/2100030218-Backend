import mysql.connector

# Connect to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Tarun@143",
    database="sys"
)

mycursor = mydb.cursor()


query = """

SELECT
	o.OrderID,
    o.CustomerID,
    o.orderDate,
    c.FirstName,
    c.LastName,
    c.Email
FROM orders o 
JOIN customers c
on o.customerID = c.customerID

"""

mycursor.execute(query)

results = mycursor.fetchall()


for row in results:
    print(row)

mydb.close()
