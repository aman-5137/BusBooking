# User Login
import mysql.connector

def connectionDB():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Aman5137@",
        database="bus_reservation_system"
    )
    return mydb
# mydb = connectionDB()
# mycursor = mydb.cursor()
# mycursor.execute("SELECT * FROM bus_detail")
#
# result = mycursor.fetchall()
#
# for x in result:
#     print(type(x))
#     print(x)

# for row in result:
#     time_of_event = row[3]
#     print("Time of event:", time_of_event)