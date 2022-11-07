import socket

c = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM)

c.connect(('localhost', 5678))
i = 10
while i > 0:
    c.sendall('Hello world')
    data = c.recv(1024)
    print('Received', repr(data))
    i = i - 1
c.close()