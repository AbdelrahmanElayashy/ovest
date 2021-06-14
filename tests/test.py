import serial
from time import sleep

port = serial.Serial("/dev/serial0", 9600)
# sleep(2)    
# port.write(b'AT+CMGF=1\r')
# sleep(2)           
# port.write(b'AT+CMGS="+4915229954839"\r')           
# sleep(2)
# port.write(b'Hallo Abdo, i am talking from raspberry\r')    
# sleep(2)        
# port.write(b'\x1A')           
# sleep(2)