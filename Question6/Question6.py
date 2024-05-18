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
	p.ProductID,
    p.ProductName,
    SUM(o.quantity) as orderCount
FROM orderItems o
JOIN orders ord
on o.OrderID = ord.OrderID
JOIN customers c
on ord.CustomerID = c.CustomerID
JOIN products p
on p.ProductID = o.ProductID
Group by
    p.ProductID,
    p.ProductName
Order by
	orderCount DESC
LIMIT 1

    
"""

mycursor.execute(query)

results = mycursor.fetchall()


for row in results:
    print(row)

mydb.close()
