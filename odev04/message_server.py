import random
import socket
import time
import sys
from thread import *

host = ''
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


def clientThread(conn):
    conn.send("Baglandiginiz icin tesekkurler!\n")
    while True:
        data = conn.recv(1024)
        reply = "Peki " + addr[0]
        flag = int(random.uniform(0,20))
        if flag == 9:
            currentTime = time.ctime(time.time()) + "\r\n"
            conn.send(currentTime.encode('ascii'))
        if not data:
            break
        conn.sendall(reply)
    conn.close()

while 1:
    conn, addr = s.accept()
    print "Baglanildi " + addr[0] + ":" + str(addr[1])
    start_new_thread(clientThread ,(conn,))

s.close()
