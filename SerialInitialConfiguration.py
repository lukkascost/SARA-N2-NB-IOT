import serial as sr
from Commands.AT_Commands import *

serRead = sr.Serial(
    # port='/dev/tty.usbserial-00002014A',
    port='/dev/tty.usbserial-00001014A',
    # port='/dev/tty.usbserial-FTDCLVDP',
    baudrate=9600,
    timeout=2
)

#ativar codigo de erro
comando = At_command('AT+CMEE=1\r\n', serRead)
print comando.command, comando.execute_command()
print

#modo online
comando = At_command("AT+CFUN=1\r\n", serRead)
print comando.command, comando.execute_command()

#ismi do chip
comando = At_command("AT+CIMI\r\n", serRead)
print comando.command, comando.execute_command()

#pergunta qual a freq (pode ser necessario modificar)
comando = At_command("AT+NBAND?\r\n", serRead)
print comando.command, comando.execute_command()

#pergunta a apn
comando = At_command('AT+CGDCONT?\r\n', serRead)
print comando.command, comando.execute_command()

#seta a apn
comando = At_command('AT+CGDCONT=1,"IP","JAVA.CLARO.COM.BR"\r\n', serRead)
print comando.command, comando.execute_command()

comando = At_command('AT+CSCON=1\r\n', serRead)
print comando.command, comando.execute_command()

#atach
comando = At_command("AT+CGATT=1\r\n", serRead)
print comando.command, comando.execute_command()

#rssi
comando = At_command('AT+CSQ\r\n', serRead)
print comando.command, comando.execute_command()

#status da rede
comando = At_command('AT+NUESTATS\r\n', serRead)
print comando.command, comando.execute_command()


comando = At_command('AT+CSCON?\r\n', serRead)
print comando.command, comando.execute_command()


# comando = At_command('AT+NRB\r\n', serRead)
# print comando.command, comando.execute_command()  