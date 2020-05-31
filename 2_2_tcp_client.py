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

target_host = "www.google.com"
target_port = 80

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_host, target_port))

    message = "GET / HTTP/1.1\r\nHost: google.com\r\n\r\n"

    client.send(message.encode('utf-8'))

    response = client.recv(4096)

    print(response)

if __name__ == '__main__':
    main()
