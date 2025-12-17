# import mysql connector
import mysql.connector

# establish connection with mysql server
connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = "iot_etc",
    use_pure = True
)

# form a query to be executed
name = input("Enter name whose email to be updated : ")
email = input("Enter new email : ")

query = f"update students SET email = '{email}' where name = '{name}';"

# create a cursor to execute a query
cursor = connection.cursor()

# execute a query
cursor.execute(query)

# commit your changes on mysql server
connection.commit()

# close the cursor
cursor.close()

# close the connection with mysql server
connection.close()

