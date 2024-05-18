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
    o.orderID,
	p.ProductID,
    p.ProductName,
    p.price,
    o.quantity
from products p
INNER JOIN orderitems o
on p.ProductID = o.ProductID
ORDER BY o.orderID ASC

"""

mycursor.execute(query)

results = mycursor.fetchall()


for row in results:
    print(row)

mydb.close()
