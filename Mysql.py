import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password ="Telefons9048" 
)
# print(mydb)

mycursor = mydb.cursor()

sql = "SELECT * FROM world.city"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)