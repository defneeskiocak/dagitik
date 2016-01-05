import sys
import socket
import threading
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import Queue
import time

class ReadThread (threading.Thread):
    def __init__(self,  name, csoc, threadQueue, app):
        threading.Thread.__init__(self)
        self.name = name
        self.nickname = ""
        self.csoc = csoc
        self.threadQueue = threadQueue
        self.app =app

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
            self.app.cprint(msg)

    def run(self):
        while True:
            data = self.csoc.recv(1024)

class WriteThread (threading.Thread):
    def __init__(self,  name, csoc, threadQueue):
        threading.Thread.__init__(self)
        self.name = name
        self.csoc = csoc
        self.threadQueue = threadQueue

    def run(self):
        while True:
            if self.threadQueue.qsize() > 0:
                queue_message = self.threadQueue.get()
                try:
                    self.csoc.send(queue_message)
                except socket.error:
                    self.csoc.close()
                    break

class ClientDialog(QDialog):
    def __init__(self, threadQueue):
        self.threadQueue = threadQueue
        self.qt_app = QApplication(sys.argv)
        QDialog.__init__(self, None)
        self.setWindowTitle('IRC Client')
        self.setMinimumSize(500, 200)
        self.vbox = QVBoxLayout()
        self.sender = QLineEdit("", self)
        self.channel = QTextBrowser()
        self.send_button = QPushButton('&Send')
        self.send_button.clicked.connect(self.outgoing_parser)
        self.vbox.addWidget(self.channel)
        self.vbox.addWidget(self.sender)
        self.vbox.addWidget(self.send_button)
        self.setLayout(self.vbox)

    def cprint(self, data):
        self.channel.append(data)

    def outgoing_parser(self, data):
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
        self.show()
        self.qt_app.exec_()

s = socket.socket()
host = ...
port = ...
s.connect((host,port))
sendQueue = ...
app = ClientDialog(sendQueue)
# start threads
rt = ReadThread("ReadThread", s, sendQueue, app)
rt.start()
wt = WriteThread("WriteThread", s, sendQueue)
wt.start()
app.run()
rt.join()
wt.join()
s.close()
