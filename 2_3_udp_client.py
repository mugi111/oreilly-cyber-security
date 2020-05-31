#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      mugi
#
# Created:     31/05/2020
# Copyright:   (c) mugi 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import socket

target_host = "127.0.0.1"
target_port = 80

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    message = "AAABBBCCC"

    client.sendto(message.encode('utf-8'), (target_host, target_port))

    (data, addr) = client.recv(4096)

    print(data)

if __name__ == '__main__':
    main()
