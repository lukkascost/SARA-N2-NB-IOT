import serial as sr

serRead = sr.Serial(
        port='COM5',
        baudrate = 9600,
        timeout=0.2
)

Runi = True
j = 0
while Runi:
    cmd = "AT\r"
    serRead.write(cmd.encode())
    x = serRead.read(2)
    if(len(x)>0):
        print x
    j+=1
