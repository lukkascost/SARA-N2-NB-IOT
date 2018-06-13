import SocketServer
import socket


class TCPHandler(SocketServer.BaseRequestHandler):
    """
    The request handler class server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """
    DEFAULT_PORT = 4506
    DESTINY_PORT = 4065
    DEFAULT_HOST = "127.0.0.1"
    DESTINY_HOST = "127.0.0.1"

    def handle(self):
        pass


class Server_TCP(SocketServer.TCPServer):
    def __init__(self, server_address, handler_class=TCPHandler):
        SocketServer.TCPServer.__init__(self, server_address, handler_class)
        return

    def server_activate(self):
        SocketServer.TCPServer.server_activate(self)
        return

    def serve_forever(self):
        while True:
            self.handle_request()
        return

    def handle_request(self):
        return SocketServer.TCPServer.handle_request(self)

    def verify_request(self, request, client_address):
        return SocketServer.TCPServer.verify_request(self, request, client_address)

    def process_request(self, request, client_address):
        return SocketServer.TCPServer.process_request(self, request, client_address)

    def server_close(self):
        return SocketServer.TCPServer.server_close(self)

    def finish_request(self, request, client_address):
        print ["%02X" % ord(x) for x in request.recv(1024)]
        return SocketServer.TCPServer.finish_request(self, request, client_address)

    def close_request(self, request_address):
        return SocketServer.TCPServer.close_request(self, request_address)


if __name__ == "__main__":
    # Create the server
    server = Server_TCP((TCPHandler.DEFAULT_HOST, TCPHandler.DEFAULT_PORT), TCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
