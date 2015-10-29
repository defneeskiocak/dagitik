import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12345

s.connect((host, port))

while 1:
    data = s.recv(1024)
    if ( data == 'Bitir'):
        s.close()
        break
    else:
        print "GELEN MESAJ:" , data
        data = raw_input ( "GONDER (Cikmak icin Bitir yazin): " )
        if (data != 'Bitir'):
            s.send(data)
        else:
            s.send(data)
            s.close()
            break
