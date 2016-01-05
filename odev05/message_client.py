import threading
import Queue
import socket
import sys

class ReadThread (threading.Thread):
    def __init__(self, name, cSocket, address, lQueue, tQueue, fihrist):
        threading.Thread.__init__(self)
        self.nickname=None
        self.name = name
        self.cSocket = cSocket
        self.address = address
        self.lQueue = lQueue
        self.tQueue = tQueue
        self.fihrist = fihrist

    def csend(self,data):
        self.cSocket.sendall(data)

    def incoming_parser(self, data):
        if len(data) == 0:
            return
        if len(data) > 3 and not data[3] == "":
            response = "ERR"
            self.csoc.send(response)
            return

        rest = data[4:]

        if data[0:3] == "BYE":
            ...
        if data[0:3] == "ERL":
            ...
        if data[0:3] == "HEL":
            ...
        if data[0:3] == "REJ":
            ...
        if data[0:3] == "MNO":
            ...
        if data[0:3] == "MSG":
            ...
        if data[0:3] == "SAY":
            ...
        if data[0:3] == "SYS":
            ...
        if data[0:3] == "LSA":
            splitted = rest.split(" ")
            msg = "<Server>: Registered nicks: "
            for i in splitted:
            	msg += i + ","
            msg = msg[:-1]
			...
            self.app.cprint(msg)

    def run(self):
        while True:
           ...

class WriteThread (threading.Thread):
    def __init__(self, name, cSocket, address, tQueue, lQueue):
        threading.Thread.__init__(self)
        self.name = name
        self.cSocket = cSocket
        self.address = address
        self.lQueue = lQueue
        self.tQueue = tQueue

    def incoming_parser(self, data):
        data=self.sender.text()
        if len(data) == 0:
            return
        if data[0] == "/":

            if command == "list":
                
            elif command == "quit":

            elif command == "msg":

            else:
                self.cprint("Local: Command Error.")
        else:
            self.threadQueue.put("SAY " + data)
        self.sender.clear()

    def run(self):
        while True:
            ...

