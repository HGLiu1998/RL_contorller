import zmq
import json 


context = zmq.Context()
socket = context.socket(zmq.REQ)
data = [{'a': 'hello json'}]
msg = json.dumps(data)
print(type(msg))
print(msg)
socket.connect("tcp://192.168.50.161:5555")

print("Send")
socket.send_string(msg)

reply = socket.recv_string()
print(reply)