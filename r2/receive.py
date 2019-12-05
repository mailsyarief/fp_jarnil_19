# -*- coding: utf-8 -*-
import socket
import struct
import sys
import pickle

port = 10002
lat_to = -7.265441
long_to = 112.797662

def sendPosition():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(20)
    client.connect(('127.0.0.1', 35))
    data = {
        'port' : port,
        'lat' : lat_to,
        'long' : long_to
    }
    client.send(pickle.dumps(data))
    print 'sukses mengirim lokasi !'
    return client.close()


def multicast():
    multicast_group = '224.3.29.71'
    server_address = ('', port)

    # Create the socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind to the server address
    sock.bind(server_address)

    # Tell the operating system to add the socket to the multicast group
    # on all interfaces.
    group = socket.inet_aton(multicast_group)
    mreq = struct.pack('4sL', group, socket.INADDR_ANY)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    # Receive/respond loop
    while True:
        print >>sys.stderr, '\nwaiting to receive message'
        data, address = sock.recvfrom(1024)
        
        print >>sys.stderr, 'received %s bytes from %s' % (len(data), address)
        print >>sys.stderr, data

        print >>sys.stderr, 'sending acknowledgement to', address
        sock.sendto('ack', address)

if __name__ == '__main__':
    print "receiver 1, port " + str(port) + ": "
    print "=============="
    while 1:
        print "1. mengirimkan posisi ke sender"
        print "2. receive data"
        print "3. keluar"
        inputan = raw_input('Pilihan > ')
        if(inputan == '1'):
            sendPosition()
        elif(inputan == '2'):
            multicast()
        elif(inputan == '3'):
            exit()
        else :
            print 'inputan salah'