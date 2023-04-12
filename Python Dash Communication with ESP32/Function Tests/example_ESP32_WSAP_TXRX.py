import websocket
from time import sleep
 
ws = websocket.WebSocket()
ws.connect("ws://192.168.4.1/")
 
i = 0
nrOfMessages = 15


while(1):
    str = input("Prompt:\t")

    if str == "":
        break
    else:
        ws.send(str)
        result = ws.recv()
        print(result)


"""
while i<nrOfMessages:
    ws.send("HIGH,21")
    result = ws.recv()
    print(result)
    sleep(1)
    ws.send("LOW,21")
    result = ws.recv()
    print(result)
    sleep(1)

    ws.send("READ,21")
    result = ws.recv()
    print(result)

    sleep(1)
    i=i+1
"""
 
ws.close()
