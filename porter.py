import sys
import socket
from datetime import datetime

if len(sys.argv):
    target = socket.gethostbyname(sys.argv[1])

else:
    print("Invalid amount of arguments.")
    print("python3 porter.py <ip>")

print("*"*50)
print("Scanning started")
print("*"*50)

try:
    n = int(input("Select Ports to scan (0-65535): "))

    for port in range(n):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))

        if result==0:
            print("Port {} is open".format(port))
    
        s.close()

except KeyboardInterrupt:
    print("\nExisting Program...")
    sys.exit()

except socket.gaierror:
    print("\nHostname couldnot be resolved.")
    sys.exit()
except socket.error:
    print("\nCouldnot connect to server.")
    sys.exit()

print("*"*50)