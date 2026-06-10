import socket
import sys
import itertools
import string

ip = sys.argv[1]
port = int(sys.argv[2])

chars = string.ascii_lowercase + string.digits

with socket.socket() as s:
    s.connect((ip, port))
    
    length = 1
    while True:
        for combo in itertools.product(chars, repeat=length):
            password = ''.join(combo)
            s.send(password.encode())
            response = s.recv(1024).decode()
            if response == 'Connection success!':
                print(password)
                sys.exit()
        length += 1