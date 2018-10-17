import mysql.connector

mydb = mysql.connector.connect(
  host="172.17.0.2",
  user="root",
  passwd="my-secret-pw",
  database="yaya"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM Luz")
myresult = mycursor.fetchall()

for x in myresult:
  print(x) 