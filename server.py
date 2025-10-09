server_ip = ("192.168.17.88")
print("server ip:",server_ip)

data = input("Enter client ip address: ")
l = data.split(" ")
print("client ip:",l)

def change():
    new = input("Enter the new ip: ")
    s = new.split(" ")
    l.append(s)
    print()

change()

print("Updated configuration:")
print("Server ip:",server_ip)
print("client ip:",l)