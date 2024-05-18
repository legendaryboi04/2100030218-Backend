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
SELECT * from customers
"""

mycursor.execute(query)

results = mycursor.fetchall()


for row in results:
    print(row)

mydb.close()
