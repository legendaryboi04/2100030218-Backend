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
    DATE_FORMAT(ord.OrderDate, '%Y-%m') AS OrderMonth,
    monthname(ord.OrderDate) as MonthName,
    COUNT(ord.OrderID) AS TotalOrders,
    SUM(o.quantity * p.price) AS TotalSales
FROM orders ord
JOIN orderItems o
    ON ord.OrderID = o.OrderID
JOIN products p
    ON o.ProductID = p.ProductID
WHERE YEAR(ord.OrderDate) = 2023
GROUP BY OrderMonth,MonthName
ORDER BY OrderMonth

    
"""

mycursor.execute(query)

results = mycursor.fetchall()


for row in results:
    print(row)

mydb.close()
