
class At_command(object):
    def __init__(self, command, serial):
        self.command = command+"\r"
        self.serial = serial
        self.__name__ = "Comando " + command + ": "

    def execute_command(self):
        self.serial.write(self.command.encode())
        x = self.serial.read(10000000)
        x = filter(None, x.split("\r\n"))
        return x
