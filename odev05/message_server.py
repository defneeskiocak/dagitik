import threading
import Queue
import socket


class ReadThread (threading.Thread):
    def __init__(self, name, cSocket, address, logQueue):
    threading.Thread.__init__(self)
    self.nickname=None
    self.name = name
    self.cSocket = cSocket
    self.address = address
    self.lQueue = logQueue
    self.fihrist = fihrist
    self.tQueue = threadQueue

    def csend(self,data):
        self.cSocket.sendall(data)

    def parser(self, data):
        data = data.strip()
        protocol = data[0:3]
        parameter = data[4:].strip()

        if not self.nickname and not protocol == "USR":
            response="ERL"
            self.csend(response)

        return 1
        # data sekli bozuksa
        if ...
            response = "ERR"
            self.csend(response)
            return 0
        if protocol == "USR":
            nickname = parameter
        if ...
            # kullanici yoksa
            response = "HEL " + nickname
            ...
            ...
            # fihristi guncelle
            self.fihrist.update(...)
            ...
            ...
            self.lQueue.put(self.nickname + " has joined.")
            return 0
        else:
            # kullanici reddedilecek
            response = "REJ " + nickname
            self.csend(response)
            ....
            # baglantiyi kapat
            self.csoc.close()
            return 1
        elif protocol == "QUI":
            response = "BYE " + self.nickname
            ...
            ...
            # fihristten sil
            ...
            ...
            # log gonder
            ...
            # baglantiyi sil
            ...
            ...
        elif protocol == "LSQ":
            response = "LSA "
            ...
            ...
        elif protocol == "TIC":
            ...
            ...
        elif protocol == "SAY":
            ...
            ...
        elif protocol == "MSG":
            ...
            ...
            ...
            if not to_nickname in self.fihrist.keys():
                response = "MNO"
            else:
                queue_message = (to_nickname, self.nickname, message)
                # gonderilecek threadQueueyu fihristten alip icine yaz
                self.fihrist[to_nickname].put(queue_message)
                response = "MOK"
            self.csend(response)
        else:
        # bir seye uymadiysa protokol hatasi verilecek
            response = "ERR"
            ...
            ...
            ...

    

class WriteThread (threading.Thread):
    def __init__(self, name, cSocket, address, threadQueue, logQueue ):
        threading.Thread.__init__(self)
        self.name = name
        self.cSocket = cSocket
        self.address = address
        self.lQueue = logQueue
        self.tQueue = threadQueue

    def run(self):
        self.lQueue.put("Starting " + self.name)
    while True:
        ...
        ...
        ...
        # burasi kuyrukta sirasi gelen mesajlari
        # gondermek icin kullanilacak
        if self.threadQueue.qsize() > 0:
            queue_message = self.threadQueue.get()
            # gonderilen ozel mesajsa
        if ...
            message_to_send = "MSG " + ...
        # genel mesajsa
        elif queue_message[1]:
            message_to_send = "SAY " + ...
        # hicbiri degilse sistem mesajidir
        else:
            message_to_send = "SYS " + ...
            ...
            ...
            ...
    self.lQueue.put("Exiting " + self.name)
