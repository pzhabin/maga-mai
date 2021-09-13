import socket

HOST = '0.0.0.0'    # Все IP-интерфейсы
PORT = 8888         # Порт сервера


def client(host, port):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    data = b'AZAZAZ'*50
    s.connect((host, port))
    s.sendall(data)

    # Receive data from the server and shut down
    responce = str(s.recv(1024), "utf-8")

    print(f'Sent:     {data}')
    print(f'Received: {responce}')


if __name__ == '__main__':
    client(HOST, PORT)
