# -*- coding: utf-8 -*-

import websocket
import json
import ssl

token = "robotapi:xxxxxxxxxxxxx" 

url = "wss://qatradee33e690ab2de05dc.bitbitduo.com/ws/"
ws = websocket.create_connection(url, sslopt={"cert_reqs": ssl.CERT_NONE})

ws.send(json.dumps({"method":"depth.subscribe","params":["BBD/ETH", "1x", 10],"id":0}))
ws.send(json.dumps({"method":"deals.subscribe","params":["BBD/ETH"],"id":0}))
ws.send(json.dumps({"method":"orders.subscribe","params":[token],"id":0}))
ws.send(json.dumps({"method":"balance.subscribe","params":[token],"id":0}))

print "Reeiving..."
while True:
    result =  ws.recv()
    print "*********************************"
    print result

