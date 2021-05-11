#!/bin/python3

import socket

HOST = '127.0.0.1'
PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET is like IPv4, and SOCK_STREAM is like the port
s.connect((HOST, PORT))