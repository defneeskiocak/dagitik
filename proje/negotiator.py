import threading
import Queue
import socket
import time
import sys

connect_point_list = {}

class serverReadThread (threading.Thread):
    def __init__(self, socket, queue, connect_point_list, ip, port):
        threading.Thread.__init__(self)
        self.socket = socket
        self.queue = queue
        self.connect_point_list = connect_point_list
        self.ip = ip
        self.port = port

    def parser(self, data):
        data = data.strip()
        protocol = data[0:5]

        if protocol == "REGME":
            parameter = (data[6:].strip()).split(":")
            ip = parameter[0]
            port = parameter[1]
            if(connect_point_list.has_key((ip,port))):
                connect_point_list[(ip, port)] = time.time()
                self.socket.send("REGOK")
            else:
                connect_point_list[(ip, port)] = time.time()
                self.socket.send("REGWA")

        elif protocol == "GETNL":
            parameter = data[6:].strip()
            self.socket.send("NLIST BEGIN")
            nodeList = connect_point_list.items()
            self.socket.send(nodeList)
            self.socket.send("NLIST END")

        elif protocol == "HELLO":
           self.socket.send("SALUT")

        elif protocol == "CLOSE":
            self.socket.send("BUBYE")
            del connect_point_list[(self.ip, self.port)]

        else:
            self.socket.send("CMDER")

    def run(self):
        print "Starting negotiator's server read thread"
        data = self.socket.recv(1024)
        self.parser(data)


host = "127.0.0.1"
port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "Soket olusturuldu"

try:
    s.bind((host, port))
except socket.error as msg:
    print "Bind basarisiz. Hata kodu: " + str(msg[0]) + " Message " + msg[1]
    sys.exit()

print "Soket bind basarili"

s.listen(10)
print "Soket dinlemede"
