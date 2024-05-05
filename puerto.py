import serial


while True:
            
    ser = serial.Serial(port="COM10", baudrate=9600)
    ser.write(b'HOLA\r\n')

         