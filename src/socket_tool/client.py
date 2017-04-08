#-*- coding: utf-8 -*-
"""
说明：考试工程文件，清不要修改该文件
      使用方法请阅读“python考试工程补充说明”
"""

import socket
import sys

def socketClient():
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to the port
    server_address = ('127.0.0.1', 5555)
    print >>sys.stderr, 'client started'
    
    while True:
        try:
            input = raw_input("\nplease input cmd:")
            input.strip('\n')
            print >>sys.stderr
            length = sock.sendto(input, server_address)            

            #print >>sys.stderr, 'send %s bytes to server ' % (length)
            sock.settimeout(5)
            data, server = sock.recvfrom(4096)
            if data:
                print >>sys.stderr, data.decode('utf-8')
                
        except socket.timeout:
            print >>sys.stderr,  "wait response timeout"
            continue


    print >>sys.stderr,  "system error, exit"
    sock.close()
        
if __name__ == "__main__":
    socketClient()
