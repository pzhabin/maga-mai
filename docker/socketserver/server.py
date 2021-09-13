import socketserver

HOST = '0.0.0.0'    # Все IP-интерфейсы
PORT = 8888         # Порт сервера


class TCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        # В self.request находится актуальный экхемпляр сокета
        self.data = self.request.recv(1024).strip()
        # self.data = self.rfile.readline().strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        # Отправляем Эхо
        self.request.sendall(self.data)


if __name__ == "__main__":

    # Создаем сервер
    server = socketserver.TCPServer((HOST, PORT), TCPHandler)

    # И запускаем его
    server.serve_forever()
