import serial
from time import sleep

def send_msg_per_sms(msg, number):
    port = serial.Serial("/dev/serial0", 9600)
    sleep(2)    
    port.write(b'AT+CMGF=1\r')
    sleep(2)
    num = 'AT+CMGS="{}"\r'.format(number)
    port.write(num.encode('utf-8'))           
    sleep(2)
    msg += '\r'
    port.write(msg.encode('utf-8'))    
    sleep(2)        
    port.write(b'\x1A')           
    sleep(2)

def update_db_per_http(coll, doc, attr, value):
    port = serial.Serial("/dev/serial0", 9600)
    port.write(b'AT+SAPBR=3,1,Contype,GPRS\r') 
    sleep(1)    
    port.write(b'AT+SAPBR=3,1,APN,"internet.t-d1.de"\r') 
    sleep(1) 
    port.write(b'AT+SAPBR=1,1\r')
    sleep(1)  
    port.write(b'AT+SAPBR=2,1\r')
    sleep(1) 
    port.write(b'AT+HTTPINIT\r')
    sleep(1) 
    port.write(b'AT+HTTPPARA=CID,1\r')
    sleep(1)
    url =  "http://78.46.220.174:5000/coll/doc/{}?coll={}&doc={}&{}={}".format(attr, coll, doc, attr, value)
    command = 'AT+HTTPPARA=URL,' + url + '\r'
    port.write(command.encode('utf-8'))
    sleep(1)
    port.write(b'AT+HTTPDATA=192,10000\r')
    sleep(10)
    port.write(b'AT+HTTPACTION=0\r')
    sleep(1)
    port.write(b'AT+HTTPREAD\r')
    sleep(1)
    port.write(b'AT+HTTPTERM\r')
    sleep(1)
    port.write(b'AT+SAPBR=0,1\r')
