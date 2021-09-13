import socket

HOST = '192.168.99.100'  # Docker host
PORT = 6666  # Порт сервера


def client(host, port):
    for c in range(0, 1):
        # Создаем TCP-сокет
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Подключаемся к серверу
        s.connect((host, port))
        print(f'Connected to {host}:{port}')
        for i in range(0, 50):
            try:
                # Передаем блок данных
                s.sendall(b"AZAZAZ" * 5000)
                # data = s.recv(1024)
                # print(f'Echo: {data}')
            except Exception as e:
                print(f'Error: {e}')
            # Сервер закрыл соединение
            # if not data:
            #    print(f'Server {host} disconnected')
            #    break
        s.close()


if __name__ == '__main__':
    client(HOST, PORT)
