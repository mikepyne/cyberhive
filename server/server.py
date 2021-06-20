import socket
import sys
import pickle

class Server:
    """Server"""
    address = 'localhost'
    port = 11000

    def __init__(self, a = 'localhost', p = 11000):
        self.address = a
        self.port = p

    def listen(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        server_address = ('localhost', 11000)
        sock.bind(server_address)
        sock.listen(1)

        print ('Listening')
        while True:
            connection, client_address = sock.accept()

            try:
                print ('Connected')
                while True:
                    data = connection.recv(1024)
                    if data:
                        self.save(data.decode())
                    else:
                        break

            finally:
                print ('Disconnected')
                connection.close()

    def save(self, data):
        # print('{}'.format(data))
        with open('processes.txt', 'a') as f:
            f.write(data)



if __name__ == "__main__":
    server = Server()
    server.listen()
