import time
import zmq
import json


context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
	
	message = socket.recv_string()
	data_print = json.loads(message)
	
	print("Recieved requests: %s" %data_print)

	socket.send_string(b'OK')
