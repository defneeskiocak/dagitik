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

    def parser(self, data):
        data = data.strip()
        protocol = data[0:3]

        if not self.nickname and not protocol == "USR":
            response="ERL"
            self.csend(response)
            return 1

        if protocol == "USR":
            nickname = data[4:].strip()
            if(not self.fihrist.has_key(nickname)):
                # kullanici yoksa
                response = "HEL " + nickname
                self.csend(response)
                # fihristi guncelle
                self.fihrist[nickname] = self.tQueue
                self.lQueue.put(self.nickname + " has joined.")
                return 0
            else:
                # kullanici reddedilecek
                response = "REJ " + nickname
                self.csend(response)
                # baglantiyi kapat
                self.csoc.close()
                return 1

        elif protocol == "QUI":
            response = "BYE " + self.nickname
            self.csend(response)
            # fihristten sil
            del self.fihrist[self.nickname]
            # log gonder
            self.lQueue.put(self.nickname + " has left.")
            # baglantiyi sil
            self.csoc.close()

        elif protocol == "LSQ":
            response = "LSA "
            userList = ""
            for nickname in self.fihrist.keys():
                userList += "," + nickname
            self.csend(response + userList[1:])

        elif protocol == "TIC":
            self.csend("TOC")

        elif protocol == "SAY":
            message = data[4:].strip()
            self.csend(message)
        elif protocol == "MSG":
            userMessage = data[4:].strip().split(':')
            to_nickname = userMessage[0]
            message = userMessage[1]
            if not to_nickname in self.fihrist.keys():
                response = "MNO"
            else:
                queue_message = (to_nickname, self.nickname, message)
                # gonderilecek threadQueueyu fihristten alip icine yaz
                self.fihrist[to_nickname].put(queue_message)
                response = "MOK"
            self.csend(response)

        # data sekli bozuksa
        else:
            response = "ERR"
            self.csend(response)
            return 0

    def run(self):
        self.lQueue.put("Starting " + self.name)
        while True:
            data = self.cSocket.recv(1024)
            response = self.parser(data)
            self.tQueue.put(response)
        self.lQueue.put("Exiting " + self.name)

class WriteThread (threading.Thread):
    def __init__(self, name, cSocket, address, tQueue, lQueue):
        threading.Thread.__init__(self)
        self.name = name
        self.cSocket = cSocket
        self.address = address
        self.lQueue = lQueue
        self.tQueue = tQueue

    def run(self):
        self.lQueue.put("Starting " + self.name)
        while True:
            # burasi kuyrukta sirasi gelen mesajlari
            # gondermek icin kullanilacak
            if self.threadQueue.qsize() > 0:
                queue_message = self.threadQueue.get()
                # gonderilen ozel mesajsa
            if queue_message[1] == 'MSG':
                message_to_send = "MSG " + queue_message[2]
            # genel mesajsa
            elif queue_message[1] == 'SAY':
                message_to_send = "SAY " + queue_message[2]
            # hicbiri degilse sistem mesajidir
            else:
                message_to_send = "SYS " + queue_message[2]
            self.cSocket.sendall(message_to_send)
        self.lQueue.put("Exiting " + self.name)

host = ''
port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tQueue = Queue.Queue()
lQueue = Queue.Queue()
fihrist = {}
print "Soket olusturuldu"

try:
    s.bind((host, port))
except socket.error as msg:
    print "Bind basarisiz. Hata kodu: " + str(msg[0]) + " Message " + msg[1]
    sys.exit()

print "Soket bind basarili"

s.listen(10)
print "Soket dinlemede"


while 1:

    conn, addr = s.accept()
    print "Baglanildi " + addr[0] + ":" + str(addr[1])
    try:
        readThread = ReadThread('ReadThread',conn,addr,tQueue,lQueue,fihrist)
        writeThread = WriteThread('WriteThread',conn,addr,tQueue,lQueue)
        readThread.start()
        writeThread.start()
    except:
        sys.exit()

s.close()
