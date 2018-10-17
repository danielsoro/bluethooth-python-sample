# simple inquiry example
import bluetooth
import mysql.connector

nearby_devices = bluetooth.discover_devices(lookup_names=True)
print("found %d devices" % len(nearby_devices))

cortina = ""

for addr, name in nearby_devices:
    print("  %s - %s" % (addr, name))
    if name == "HC-05":
        cortina = addr

print("Conectando em %s" % cortina)

sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((cortina, 1))

mydb = mysql.connector.connect(
  host="172.17.0.2",
  user="root",
  passwd="my-secret-pw",
  database="yaya"
)


print("Conectado em %s" % mydb)
mycursor = mydb.cursor()

while True:
    print("Esperando dado para ser salvo")
    data = sock.recv(1024)
    data_para_ser_salvo = str(data)
    print("Dado recebido via bluethooth foi: %s" % data_para_ser_salvo)

    mycursor.execute("INSERT INTO Luz VALUES ('%s');" % data_para_ser_salvo)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

    mycursor.execute("SELECT * FROM Luz")

