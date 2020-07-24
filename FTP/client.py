# import libraries
import os
from ftplib import FTP
import socket

ip = socket.gethostbyname(socket.gethostname())
ftp = FTP('')
host = ip
port = 21
# connect to the ftp server
ftp.connect(host, port)

# login with the user credentials
while True:
    try:
        username = input('enter the user name')
        password = input ('enter the password')
        ftp.login(user=username, passwd=password)
    except:
        print('Invalid username or password')
        continue
    else:
        break
print(ftp.getwelcome())
print('Current Directory ', ftp.pwd())

# display avilable files in server
ftp.dir()

# function to get file from server
def grabFile():
    while True:
        try:
            filename = input('enter file name')
            local_file = open(filename, 'wb')
            ftp.retrbinary('RETR ' + filename, local_file.write, 1024)
            ftp.quit()
            local_file.close()
        except:
            print('no such file')
            local_file.close()
            os.remove(filename)
            continue
        else:
            break

# function to add files to the server
def placeFile():
    while True:
        try:
            filename = input('Enter file name to send')
            ftp.storbinary('STOR ' + filename, open(filename, 'rb'))
            ftp.quit()
        except FileNotFoundError:
            print('no such file')
            continue
        else:
            print('file successfully sent.....')
            break

# dynamically get mode from user
mode = ''
while mode not in ('send', 'receive'):
    mode = input('Enter mode of operation (send or receive) : ')
if mode == 'send':
    placeFile()
elif mode == 'receive':
    grabFile()
