import socket

HOST = '127.0.0.1'  # Localhost
PORT = 6666         # Порт сервера


def client():
    for c in range(0, 1):
        # Создаем TCP-сокет
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Подключаемся к серверу
        s.connect((HOST, PORT))
        print(f'Connected to {HOST}:{PORT}')
        for i in range(0, 5):
            try:
                # Передаем блок данных
                s.sendall(b"AZAZAZ" * 10)
                data = s.recv(1024)
                print(f'Echo: {data}')
            except Exception as e:
                print(f'Error: {e}')
            # Сервер закрыл соединение
            if not data:
                break
            print(f'Server {HOST} disconnected')
            break
        s.close()


if __name__ == '__main__':
    client()
