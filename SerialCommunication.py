import serial as sr
from Commands.AT_Commands import *

serRead = sr.Serial(
    port='/dev/tty.usbserial-00002014A',
    baudrate=9600,
    timeout=10
)

comando = At_command("AT+NBAND?", serRead)
for i in comando.execute_command():
    print i

