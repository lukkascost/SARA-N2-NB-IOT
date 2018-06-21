import SocketServer

import serial as sr
import time

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

class CommandsAT():
    ser = sr.Serial(
        port='COM5',
        baudrate=9600,
        timeout=1
    )

    def __init__(self):
        response = self.command("AT")
        print response
        response = self.command("AT+CFUN=1")
        print response
        response = self.command("AT+CIMI")
        print response
        response = self.command("AT+NCONFIG")
        print response
        response = self.command('AT+CGDCONT=1,"IP","REDUCEBT.CLARO.COM.BR"')
        print response
        response = self.command("AT+CGDCONT?")
        print response
        response = self.command("AT+NBAND=8")
        print response
        response = self.command("AT+NBAND?")
        print response
        response = self.command("AT+NEARFCN=0,3767")
        print response
        response = self.command('AT+COPS=1,2,"72405"')
        print response
        response = self.command("AT+CGATT=1")
        print response
        response = self.command("AT+CEREG?")
        print response
        response = self.command("AT+CSCON?")
        print response
        response = self.command("AT+CGPADDR")
        print response
        response = self.command("AT+COPS?")
        print response
        response = self.command("AT+CSQ")
        print response
        response = self.command("AT+NUESTATS")
        print response
        response = self.command("AT+CFUN=0")
        print response
        response = self.command('AT+NCDP="10.224.217.148",5684')
        print response
        response = self.command("AT+NRB")
        print response
        time.sleep(5)
        response = self.command("AT+NCDP?")
        print response
        response = self.command("AT+NSMI=1")
        print response
        response = self.command("AT+NNMI=2")
        print response
        return

    def command(self, cmd):
        print "Enviando comando: ",cmd
        cmd = cmd+"\r"
        cmd = cmd.encode()
        self.ser.write(cmd)
        time.sleep(1)
        x = ""
        x = self.ser.read(250)
        return x

    def testMode(self):

        pass

    def sendMode(self):
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
    #server = Server_TCP((TCPHandler.DEFAULT_HOST, TCPHandler.DEFAULT_PORT), TCPHandler)
    CommandsAT()
    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    #server.serve_forever()
