# Establish a connection to the MySQL database using the provided credentials

import mysql.connector
connection = mysql.connector.connect(
    host="138.68.140.83",   
    user="reshma", 
    password="Reshma@123",
    database="dbReshma"     )
print("Connected to MySQL DB:", connection.is_connected())
cursor = connection.cursor()
cursor.execute("select * from Item")
data = cursor.fetchall()
print(data)
cursor.close()
connection.close()
