import Queue
import threading
import thread
import time

exitFlag = 0


class myThread (threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q

    def run(self):
        print "Starting " + self.name
        process_data(self.name, self.q)
        print "Exiting " + self.name


def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print "%s processing %s" % (threadName, data)
        else:
            queueLock.release()
        time.sleep(1)

threadList = []
nameList = []
queueLock = threading.Lock()
workQueue = Queue.Queue(10)
threads = []
threadID = 1


def anahtarAlfabe(s):
    alfabe = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    anahtar = ['']*24
    for n in range(0, 24):
        anahtar[((n+s-1) % 24)] = alfabe[n]
    dictAnahtar = dict(zip(alfabe, anahtar))
    return dictAnahtar

s = int(raw_input("anahtar alfabe olusturmak icin kaydirma parametresi girin\ns: "))
n = int(raw_input("thread sayisi girin\nn: "))
l = int(raw_input("blok uzunlugu girin\nl: "))
key = anahtarAlfabe(int(s))

for x in range(0, n):
    threadList.append("Thread-%d" % x)

# Create new threads
for tName in threadList:
    thread = myThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

# Fill the queue
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

# Wait for queue to empty
while not workQueue.empty():
    pass

f = open("metin.txt", "r")
metin = f.read()
metin = metin.lower()

step = l
start = 0
end = l
for n in range(0, len(metin)/step):
    nameList.append(metin[start:end])
    start += step
    end += step

crypted = ''
str = ''
str = key[metin[0]]
crypted = str.upper()
for n in range(1, len(metin)):
    if metin[n] in key:
        str = key[metin[n]]
        crypted += str.upper()
    else:
        crypted += metin[n].upper()

f.close()

filename = "crypted_"+str(s)+"_"+str(n)+"_"+str(l)+".txt"
fC = open(filename, "w")
fC.write(crypted)
fC.close()

# Notify threads it's time to exit
exitFlag = 1

# Wait for all threads to complete
for t in threads:
    t.join()
print "Exiting Main Thread"
