class At_command(object):
    def __init__(self, command, serial):
        self.command = command + "\r"
        self.serial = serial
        self.__name__ = "Comando " + command + ": "

    def execute_command(self, command=None):
        if command is None:
            command = self.command
        self.serial.write(command.encode())
        x = self.serial.read(10000000)
        x = filter(None, x.split("\r\n"))
        return x

    def get_bytes_from_n_m_g_r(self):
        # result = self.execute_command(command="AT+NMGR\r")
        result = '12,"7EA00A000200030393A0627E"\r\n \r\nOK\r\n'
        result = filter(None, result.split("\r\n"))
        result = result[0].split(",")
        result[1] = result[1].replace("\"", "")
        charArray = ""
        for i in range(int(result[0])):
            charArray += chr(int(result[1][2 * i:(2 * i) + 2], 16))
        return charArray

    def send_to_meter(self, bytes, meter_serial):
        # meter_serial.write(bytes)
        # result = meter_serial.read(100000000)
        result = "7E A0 22 03 00 02 00 03 73 26 F4 81 80 13 05 02 00 80 06 01 3E 07 04 00 00 00 01 08 04 00 00 00 01 " \
                 "B3 D3 7E"
        result = [chr(int(x, 16)) for x in result.split(" ")]
        result = reduce(lambda old, y: old + y, result)

        result = ["%02X" % ord(x) for x in result]
        result = 'AT+NMGS={},"{}"'.format(len(result), reduce(lambda old, y: old + y, result))
        print result
