# -*- coding: utf-8 -*-
import socket
import struct
import sys


def send(message,port):
    multicast_group = ('224.3.29.71', port)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(0.2)
    ttl = struct.pack('b', 1)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

    print 'mengirimkan pesan berisi : %s' % message
    sock.sendto(message, multicast_group)

    while True:
        try:
            data, server = sock.recvfrom(16)
        except:
            print 'tidak ada respon dari port %s' % port
            sock.close()
            return 0
        else:
            print 'menerima "%s" dari %s' % (data, server)
            sock.close()
            return 1

if __name__ == '__main__':
    port = [10000,10001,10002]
    message = raw_input("input pesan > ")
    for p in port:
        hasil = send(message, p)
        while(hasil == 0):
            hasil = send(message, p)

    print 'pengiriman berhasil'