import socket
import sys
import psutil
import time

class Client:
    """Client"""
    address = 'localhost'
    port = 11000

    def __init__(self, a = 'localhost', p = 11000):
        self.address = a
        self.port = p

    def send(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        server_address = ('localhost', 11000)
        sock.connect(server_address)

        try:
            for p in psutil.process_iter(['pid', 'name', 'username']):
                sock.send(str(p.info).encode())

        finally:
            print ('Closing')
            sock.close()


if __name__ == "__main__":
    client = Client()
    while True:
        client.send()
        time.sleep(5)
