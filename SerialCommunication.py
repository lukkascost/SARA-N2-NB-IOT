import serial as sr
from Commands.AT_Commands import *

serRead = sr.Serial(
    # port='/dev/tty.usbserial-00002014A',
    port='/dev/tty.usbserial-FTDCLVDP',
    baudrate=9600,
    timeout=2
)
#
# comando = At_command("AT+CIMI\r\n", serRead)
# print comando.command, comando.execute_command()
#
# comando = At_command("AT+NCONFIG?\r\n", serRead)
# print comando.command, comando.execute_command()
#
# comando = At_command("AT+CEREG=3\r\n", serRead)
# print comando.command, comando.execute_command()
#
# comando = At_command("AT+CFUN=1\r\n", serRead)
# print comando.command, comando.execute_command()
#
# comando = At_command('AT+CGDCONT=1,"IP","JAVA.CLARO.COM.BR"\r\n', serRead)
# print comando.command, comando.execute_command()

# comando = At_command('AT+COPS=1,2,"72405"\r\n', serRead)
# print comando.command, comando.execute_command()
# #
# comando = At_command("AT+CGATT=1\r\n", serRead)
# print comando.command, comando.execute_command()
# print
#
# comando = At_command('AT+CSQ\r\n', serRead)
# print comando.command, comando.execute_command()

# comando = At_command('AT+CEREG?\r\n', serRead)
# print comando.command, comando.execute_command()
#
# comando = At_command('AT+CGPADDR\r\n', serRead)
# print comando.command, comando.execute_command()
#
# comando = At_command('AT+NSOCR=DGRAM,17,4587,1\r\n', serRead)
# print comando.command, comando.execute_command()


# comando = At_command('AT+NCDP="201.163.229.230",5683\r\n', serRead)
# print comando.command, comando.execute_command()
# print
#
#
# comando = At_command('AT+NCDP?\r\n', serRead)
# print comando.command, comando.execute_command()
# print
#
#
# comando = At_command('AT+NSOST=0,201.163.229.230,5683,18,4C12470CC301C10046000060030AFF0100E9\r\n', serRead)
# print comando.command, comando.execute_command()
# print
# comando = At_command('AT+NSORF=0,512\r\n', serRead)
# print comando.command, comando.execute_command()
# print
# print
# print

# comando = At_command('AT+NSOST=0,201.163.229.230,5683,25,400241C7B17401724D0265703D323031363038323331363438\r\n', serRead)
# print comando.command, comando.execute_command()
# print
# comando = At_command('AT+NSORF=0,512\r\n', serRead)
# print comando.command, comando.execute_command()
# print

# #
# comando = At_command('AT+NSOST=0,201.163.229.230,5683,6,AA72700001AA\r\n', serRead)
# print comando.command, comando.execute_command()
# print
# comando = At_command('AT+NSORF=0,512\r\n', serRead)
# print comando.command, comando.execute_command()
# print










