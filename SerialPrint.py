from serial import *
import requests

# ser = Serial("com3", baudrate = 9600, timeout=1)
i=510
while 1:
    # arduinoData = ser.readline().decode('ascii')
    # print("Darduinoata:", arduinoData)
    URL1 = "https://api.thingspeak.com/update?api_key=EKN4D7NVSX0BKGAP"
    
    PARAMS1 = { 'field1' : i }

    requests.get(url=URL1,params=PARAMS1)
    i = i + 1
    
    URL = "https://api.thingspeak.com/channels/635046/fields/1.json?results=2"

    PARAMS = { 'results' : 2 }

    res = requests.get(url=URL,params=PARAMS)
    print(res.content) #getting value in List and json
    resjson = res.json()
    feed = resjson['feeds']
    #print(feed[1]['field1'])
    # RES = serial.Serial("com3", 9600, timeout = 1 )
    # ser.write(b'H')
    # ser.write(b'L')
    # ser.write(b'H')
    # ser.write(b'L')
    # ser.close()
