# server并发接受client的请求

import socketserver

class Myserver(socketserver.BaseRequestHandler):

    def handle(self):
        print("服务启动中..........")
        while True:
            conn = self.request
            print(self.client_address)
            while True:
                client_data = conn.recv(1024)
                print(str(client_data, 'utf8'))
                print('waiting......')
                conn.sendall(client_data)
            conn.close()


if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 8009), Myserver)
    server.serve_forever()

