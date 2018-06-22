import serial as sr
from Commands.AT_Commands import *

serRead = sr.Serial(
    # port='/dev/tty.usbserial-00002014A',
    port='/dev/tty.usbserial',
    baudrate=9600,
    timeout=10
)

comando = At_command("AT+NBAND?", serRead)
print comando.get_bytes_from_n_m_g_r()
comando.send_to_meter([],[])
