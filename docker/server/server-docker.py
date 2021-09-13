#! /usr/local/bin/python

import socket

HOST = '0.0.0.0'    # Все IP-интерфейсы
PORT = 6666         # Порт сервера


def server():
    # Создаем TCP-сокет
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Привязываем его к IP и порту
    s.bind((HOST, PORT))
    # Начинаем слушать сокет
    s.listen()
    while True:
        print("Server started")
        # Принимаем входящее соединение
        (conn, addr) = s.accept()
        print(f'Connect from {addr}')
        while True:
            # Получаем данные до 1К длиной
            try:
                data = conn.recv(32768)
            except Exception as e:
                print(f'Error: {e}')
                break
            if not data:
                # Клиент закрыл соединение
                print(f'Client {addr} disconnected')
                break
            # Возвращаем обратно эхо
            # conn.sendall(data)
            print(f'Received {len(data)} bytes')


if __name__ == '__main__':
    server()
