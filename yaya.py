# simple inquiry example
import bluetooth

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

while True:
    data = sock.recv(1024)
    print("Data received:", str(data))
