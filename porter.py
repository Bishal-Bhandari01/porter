import sys
import socket

if len(sys.argv):
    target = socket.gethostbyname(sys.argv[1])

else:
    print("==> Invalid amount of arguments.")
    print("==> python3 porter.py ipaddress")
    print("==> python3 porter.py domain.com")



try:
    n = int(input(">>> Select Ports to scan (0-65535): "))
    print("*"*50)
    print("*\t\tScanning started\t\t *")
    print("*"*50)

    for port in range(n+1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))

        if result==0: 
            print(">>> Port {} is open".format(port))
    
        s.close()
        pass


except KeyboardInterrupt:
    print("\n")
    print("*"*50)
    print("*\t\tExisting Program...\t\t *")
    print("*"*50)
    sys.exit()

except socket.gaierror:
    print("*"*50)
    print("\n\tHostname couldnot be resolved.\t *")
    print("*"*50)
    sys.exit()
except socket.error:
    print("*"*50)
    print("\n\tCouldnot connect to server.\t *")
    print("*"*50)
    sys.exit()

print("*"*50)
print("*\t\tScanning Completed\t\t *")
print("*"*50)
