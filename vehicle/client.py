import socket
import time
import sys

HOST, PORT = "localhost", 9002
data = " ".join(sys.argv[1:])

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

i = 0

    

try:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    i = 2.5
    sock.sendall(str(data)+'\n')
    # Receive data from the server and shut down
finally:
    sock.close()

