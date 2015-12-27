import threading
import Queue
import socket

connect_point_list = {}

class serverReadThread (threading.Thread):
    def __init__(self, socket, queue, connect_point_list):
        threading.Thread.__init__(self)
        self.socket = socket
        self.queue = queue
        self.connect_point_list = connect_point_list

    def parser(self, data):
        data = data.strip()
        protocol = data[0:5]

        if protocol == "REGME":
            parameter = (data[6:].strip()).split(":")
            ip = parameter[0]
            port = parameter[1]
            if(connect_point_list.has_key((ip,port))):
                print "REGOK"
            else:
                print "REGWA"

        elif protocol == "GETNL":
            parameter = data[6:].strip()
            print "NLIST BEGIN"

        else:
            print "CMDER"

    def run(self):
        print "Starting negotiator's server read thread"
        data = self.socket.recv()
        self.parser(data)


