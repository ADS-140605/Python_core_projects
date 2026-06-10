import socket
import os
from dotenv import load_dotenv
load_dotenv()
SECRET = os.getenv("SECRET")
if not SECRET:
    raise ValueError("SECRET not set in .env file")

with socket.socket() as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('localhost', 9090))
    s.listen(1)
    print("Server started...")

    try:
        while True:
            conn, addr = s.accept()
            with conn:
                while True:
                    data = conn.recv(1024).decode()
                    if not data:
                        break
                    if data == SECRET:
                        conn.send(b'Connection success!')
                    else:
                        conn.send(b'Wrong password!')
    except KeyboardInterrupt:
        print("\nServer stopped.")