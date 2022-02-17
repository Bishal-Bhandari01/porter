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
    pro = input(">>> Select protocol (TCP/UDP): ")

    print("*"*50)
    print("\t\tScanning started")
    print("*"*50)

    if pro == "tcp" or pro == "TCP":
        for port in range(n+1):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((target, port))

            if result==0:
                print(">>> Port {} is open".format(port))
        
            s.close()
            pass
    
    if pro=="udp" or pro=="UDP":
        for port in range(n+1):
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((target, port))

            if result==0:
                print(">>> Port {} is open".format(port))

            s.close()
            pass


except KeyboardInterrupt:
    print("\n\tExisting Program...")
    sys.exit()

except socket.gaierror:
    print("\n\tHostname couldnot be resolved.")
    sys.exit()
except socket.error:
    print("\n\tCouldnot connect to server.")
    sys.exit()

print("*"*50)